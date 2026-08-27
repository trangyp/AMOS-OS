---
title: AMOS BRIDGE API
tags: [amos-general, amos, general, canon/knowledge]
type: document
source: 11_KNOWLEDGE/amos-general
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: AMOS_architecture

---


# amos_omega_bridge_api

```python
#!/usr/bin/env python3
"""
AMOS OMEGA Bridge API
Single public entrypoint with authentication, rate limiting, and schema validation
"""

import asyncio
import hashlib
import json
import time
from datetime import datetime, timezone
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
import logging
from fastapi import FastAPI, HTTPException, Depends, Security, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import uvicorn
from collections import defaultdict, deque
import threading

from amos_omega_ultimate_integration import amos_omega, SystemMode

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("AMOS_OMEGA_BRIDGE")

# Security
security = HTTPBearer()
API_KEY = "amos_omega_2026_secure_key"

# Rate limiting
@dataclass
class RateLimiter:
    requests_per_minute: int = 60
    requests_per_hour: int = 1000
    
    def __init__(self):
        self.minute_requests = defaultdict(deque)
        self.hour_requests = defaultdict(deque)
        self.lock = threading.Lock()
    
    def is_allowed(self, client_id: str) -> bool:
        now = time.time()
        
        with self.lock:
            # Clean old requests
            self._clean_old_requests(now)
            
            # Check minute limit
            minute_count = len(self.minute_requests[client_id])
            if minute_count >= self.requests_per_minute:
                return False
            
            # Check hour limit
            hour_count = len(self.hour_requests[client_id])
            if hour_count >= self.requests_per_hour:
                return False
            
            # Record request
            self.minute_requests[client_id].append(now)
            self.hour_requests[client_id].append(now)
            
            return True
    
    def _clean_old_requests(self, now: float):
        """Clean old request records"""
        # Clean minute requests (older than 60 seconds)
        for client_id in list(self.minute_requests.keys()):
            while (self.minute_requests[client_id] and 
                   now - self.minute_requests[client_id][0] > 60):
                self.minute_requests[client_id].popleft()
        
        # Clean hour requests (older than 3600 seconds)
        for client_id in list(self.hour_requests.keys()):
            while (self.hour_requests[client_id] and 
                   now - self.hour_requests[client_id][0] > 3600):
                self.hour_requests[client_id].popleft()

rate_limiter = RateLimiter()

# Pydantic models for schema validation
class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=10000)
    context: Optional[Dict[str, Any]] = Field(default_factory=dict)
    trace_id: Optional[str] = None

class SignalRequest(BaseModel):
    signal_type: str = Field(..., min_length=1, max_length=100)
    signal_data: Dict[str, Any] = Field(..., min_items=1)
    source: str = Field(..., min_length=1, max_length=100)
    timestamp: Optional[float] = None

class JobRequest(BaseModel):
    job_type: str = Field(..., min_length=1, max_length=100)
    job_parameters: Dict[str, Any] = Field(..., min_items=1)
    priority: Optional[int] = Field(default=5, ge=1, le=10)

class ChatResponse(BaseModel):
    trace_id: str
    determinism_hash: str
    response: str
    system_state: Dict[str, Any]
    mode: str
    timestamp: float
    processing_time_ms: float

class HealthResponse(BaseModel):
    status: str
    system_mode: str
    uptime: float
    version: str
    capabilities: List[str]

class StatusResponse(BaseModel):
    system_state: Dict[str, Any]
    regime: str
    mode: str
    telemetry: Dict[str, Any]
    invariants: Dict[str, Any]
    loops: Dict[str, Any]
    capabilities: Dict[str, Any]

class CapabilitiesResponse(BaseModel):
    capabilities: Dict[str, Any]
    available_endpoints: List[str]
    supported_signal_types: List[str]
    supported_job_types: List[str]

# FastAPI app
app = FastAPI(
    title="AMOS OMEGA Bridge API",
    description="Unified Brain-Body-Bridge Integration System",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Authentication
async def verify_api_key(credentials: HTTPAuthorizationCredentials = Security(security)):
    if credentials.credentials != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return credentials.credentials

# Rate limiting dependency
async def check_rate_limit(api_key: str = Depends(verify_api_key)):
    client_id = hashlib.sha256(api_key.encode()).hexdigest()[:16]
    if not rate_limiter.is_allowed(client_id):
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Rate limit exceeded"
        )
    return client_id

# Helper functions
def generate_trace_id() -> str:
    """Generate unique trace ID"""
    timestamp = time.time()
    return hashlib.sha256(f"BRIDGE_{timestamp}".encode()).hexdigest()[:16]

def calculate_processing_time(start_time: float) -> float:
    """Calculate processing time in milliseconds"""
    return (time.time() - start_time) * 1000

# API endpoints
@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(
    request: ChatRequest,
    api_key: str = Depends(verify_api_key),
    client_id: str = Depends(check_rate_limit)
):
    """Process chat messages through AMOS OMEGA cognitive loop"""
    start_time = time.time()
    trace_id = request.trace_id or generate_trace_id()
    
    try:
        # Prepare observation for cognitive loop
        observation = {
            "type": "chat_message",
            "message": request.message,
            "context": request.context,
            "trace_id": trace_id
        }
        
        # Process through AMOS OMEGA
        result = amos_omega.cognitive_loop(observation)
        
        # Extract response
        response_text = result.get("result", {}).get("response", "System processing complete")
        
        chat_response = ChatResponse(
            trace_id=trace_id,
            determinism_hash=result.get("determinism_hash", ""),
            response=response_text,
            system_state=result.get("system_state", {}),
            mode=result.get("mode", "NORMAL"),
            timestamp=result.get("timestamp", time.time()),
            processing_time_ms=calculate_processing_time(start_time)
        )
        
        logger.info(f"Chat processed: {trace_id} in {chat_response.processing_time_ms:.2f}ms")
        return chat_response
        
    except Exception as e:
        logger.error(f"Chat processing error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Processing failed: {str(e)}"
        )

@app.get("/health", response_model=HealthResponse)
async def health_endpoint(api_key: str = Depends(verify_api_key)):
    """System health check"""
    try:
        system_status = amos_omega.get_system_status()
        
        health_response = HealthResponse(
            status="healthy" if amos_omega.system_mode != SystemMode.COOL_DOWN else "degraded",
            system_mode=amos_omega.system_mode.value,
            uptime=time.time() - system_status.get("system_state", {}).get("timestamp", time.time()),
            version="1.0.0",
            capabilities=[
                "cognitive_processing",
                "telemetry_monitoring",
                "invariant_verification",
                "loop_analysis",
                "regime_detection",
                "collapse_assessment"
            ]
        )
        
        return health_response
        
    except Exception as e:
        logger.error(f"Health check error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Health check failed: {str(e)}"
        )

@app.get("/status", response_model=StatusResponse)
async def status_endpoint(api_key: str = Depends(verify_api_key)):
    """Comprehensive system status"""
    try:
        system_status = amos_omega.get_system_status()
        
        status_response = StatusResponse(
            system_state=system_status.get("system_state", {}),
            regime=system_status.get("regime", "unknown"),
            mode=system_status.get("mode", "NORMAL"),
            telemetry=system_status.get("telemetry", {}),
            invariants=system_status.get("invariants", {}),
            loops=system_status.get("loops", {}),
            capabilities=system_status.get("capabilities", {})
        )
        
        return status_response
        
    except Exception as e:
        logger.error(f"Status endpoint error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Status retrieval failed: {str(e)}"
        )

@app.get("/capabilities", response_model=CapabilitiesResponse)
async def capabilities_endpoint(api_key: str = Depends(verify_api_key)):
    """System capabilities and available endpoints"""
    try:
        system_status = amos_omega.get_system_status()
        
        capabilities_response = CapabilitiesResponse(
            capabilities=system_status.get("capabilities", {}),
            available_endpoints=[
                "/chat",
                "/health",
                "/status",
                "/capabilities",
                "/signals",
                "/jobs"
            ],
            supported_signal_types=[
                "market_stress",
                "system_failure",
                "stabilization",
                "volatility_spike",
                "liquidity_crunch",
                "policy_change",
                "external_shock"
            ],
            supported_job_types=[
                "analysis",
                "simulation",
                "verification",
                "optimization",
                "monitoring",
                "reporting"
            ]
        )
        
        return capabilities_response
        
    except Exception as e:
        logger.error(f"Capabilities endpoint error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Capabilities retrieval failed: {str(e)}"
        )

@app.post("/signals")
async def signals_endpoint(
    request: SignalRequest,
    api_key: str = Depends(verify_api_key),
    client_id: str = Depends(check_rate_limit)
):
    """Process external signals"""
    trace_id = generate_trace_id()
    
    try:
        # Validate signal type
        supported_signals = [
            "market_stress", "system_failure", "stabilization",
            "volatility_spike", "liquidity_crunch", "policy_change", "external_shock"
        ]
        
        if request.signal_type not in supported_signals:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Unsupported signal type: {request.signal_type}"
            )
        
        # Prepare observation for cognitive loop
        observation = {
            "type": request.signal_type,
            "signal_data": request.signal_data,
            "source": request.source,
            "timestamp": request.timestamp or time.time(),
            "trace_id": trace_id
        }
        
        # Process through AMOS OMEGA
        result = amos_omega.cognitive_loop(observation)
        
        logger.info(f"Signal processed: {request.signal_type} from {request.source}")
        
        return {
            "trace_id": trace_id,
            "status": "processed",
            "result": result,
            "timestamp": time.time()
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Signal processing error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Signal processing failed: {str(e)}"
        )

@app.post("/jobs")
async def jobs_endpoint(
    request: JobRequest,
    api_key: str = Depends(verify_api_key),
    client_id: str = Depends(check_rate_limit)
):
    """Submit and process jobs"""
    trace_id = generate_trace_id()
    
    try:
        # Validate job type
        supported_jobs = [
            "analysis", "simulation", "verification",
            "optimization", "monitoring", "reporting"
        ]
        
        if request.job_type not in supported_jobs:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Unsupported job type: {request.job_type}"
            )
        
        # Prepare observation for cognitive loop
        observation = {
            "type": "job_submission",
            "job_type": request.job_type,
            "job_parameters": request.job_parameters,
            "priority": request.priority,
            "trace_id": trace_id
        }
        
        # Process through AMOS OMEGA
        result = amos_omega.cognitive_loop(observation)
        
        logger.info(f"Job submitted: {request.job_type} with priority {request.priority}")
        
        return {
            "trace_id": trace_id,
            "job_id": f"job_{trace_id}",
            "status": "submitted",
            "result": result,
            "timestamp": time.time()
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Job submission error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Job submission failed: {str(e)}"
        )

# Middleware for request logging
@app.middleware("http")
async def log_requests(request, call_next):
    start_time = time.time()
    
    response = await call_next(request)
    
    process_time = time.time() - start_time
    
    logger.info(
        f"{request.method} {request.url.path} - "
        f"Status: {response.status_code} - "
        f"Time: {process_time:.3f}s"
    )
    
    return response

# Startup and shutdown events
@app.on_event("startup")
async def startup_event():
    logger.info("AMOS OMEGA Bridge API starting up...")
    logger.info(f"System mode: {amos_omega.system_mode.value}")
    logger.info(f"Registered invariants: {len(amos_omega.invariant_ledger)}")
    logger.info(f"Active loops: {len(amos_omega.loop_registry)}")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("AMOS OMEGA Bridge API shutting down...")
    amos_omega.shutdown()

# Main execution
if __name__ == "__main__":
    uvicorn.run(
        "amos_omega_bridge_api:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )


```

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[AMOS-GENERAL_MOC]]

---
**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]
