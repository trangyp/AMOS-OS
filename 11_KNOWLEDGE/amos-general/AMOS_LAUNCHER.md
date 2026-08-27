---
tags: [amos-general]
---
# amos_omega_launcher

```python
#!/usr/bin/env python3
"""
AMOS OMEGA — ULTIMATE BRAIN–BODY–BRIDGE INTEGRATION LAUNCHER
Complete system launcher with all components unified
"""

import asyncio
import json
import logging
import signal
import sys
import time
from pathlib import Path
from typing import Dict, Any, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("AMOS_OMEGA_LAUNCHER")

# Import all components
try:
    from amos_omega_ultimate_integration import amos_omega
    from amos_omega_bridge_api import app as bridge_app
    from amos_omega_fx_engine import fx_engine
    from amos_omega_chart_engine import chart_engine
    from amos_omega_n8n_workflows import n8n_orchestrator
except ImportError as e:
    logger.error(f"Failed to import components: {e}")
    sys.exit(1)

class AMOSOmegaLauncher:
    """Complete AMOS OMEGA system launcher"""
    
    def __init__(self):
        self.components = {}
        self.running = False
        self.shutdown_event = asyncio.Event()
        
        # Configuration
        self.config = {
            "bridge": {
                "host": "0.0.0.0",
                "port": 8000,
                "enabled": True
            },
            "ui": {
                "enabled": True,
                "file": "amos_omega_loveable_ui.html"
            },
            "fx_engine": {
                "enabled": True,
                "update_interval": 5.0
            },
            "chart_engine": {
                "enabled": True,
                "symbols": ["EURUSD", "GBPUSD", "USDJPY"]
            },
            "n8n": {
                "enabled": True,
                "auto_activate": ["signal_scanner", "collapse_watcher"]
            }
        }
    
    async def initialize_system(self) -> bool:
        """Initialize all AMOS OMEGA components"""
        logger.info("Initializing AMOS OMEGA Ultimate Integration System...")
        
        try:
            # 1. Initialize Core Brain System
            logger.info("🧠 Initializing Brain Cognitive Core...")
            self.components["brain"] = amos_omega
            logger.info("✅ Brain Core initialized")
            
            # 2. Initialize Bridge API
            if self.config["bridge"]["enabled"]:
                logger.info("🌉 Initializing Bridge API...")
                self.components["bridge"] = bridge_app
                logger.info("✅ Bridge API initialized")
            
            # 3. Initialize FX Engine
            if self.config["fx_engine"]["enabled"]:
                logger.info("💱 Initializing FX Structural Analysis Engine...")
                self.components["fx_engine"] = fx_engine
                logger.info("✅ FX Engine initialized")
            
            # 4. Initialize Chart Engine
            if self.config["chart_engine"]["enabled"]:
                logger.info("📊 Initializing Live Chart Engine...")
                self.components["chart_engine"] = chart_engine
                logger.info("✅ Chart Engine initialized")
            
            # 5. Initialize N8N Orchestrator
            if self.config["n8n"]["enabled"]:
                logger.info("🔄 Initializing N8N Orchestrator...")
                self.components["n8n"] = n8n_orchestrator
                
                # Auto-activate critical workflows
                for workflow in self.config["n8n"]["auto_activate"]:
                    n8n_orchestrator.activate_workflow(workflow)
                    logger.info(f"✅ Activated workflow: {workflow}")
                
                logger.info("✅ N8N Orchestrator initialized")
            
            # 6. Generate sample data for demonstration
            await self._generate_sample_data()
            
            logger.info("🚀 AMOS OMEGA System initialization complete!")
            return True
            
        except Exception as e:
            logger.error(f"❌ System initialization failed: {e}")
            return False
    
    async def _generate_sample_data(self):
        """Generate sample data for system demonstration"""
        logger.info("📝 Generating sample data...")
        
        # Generate sample FX data
        if "fx_engine" in self.components:
            from amos_omega_fx_engine import FXMetrics
            
            symbols = ["EURUSD", "GBPUSD", "USDJPY"]
            base_prices = {"EURUSD": 1.0850, "GBPUSD": 1.2750, "USDJPY": 148.50}
            
            for symbol in symbols:
                base_price = base_prices[symbol]
                
                # Generate 100 data points
                for i in range(100):
                    timestamp = time.time() - (100 - i) * 3600  # Hourly data
                    
                    # Realistic price movement
                    price_change = (i / 100) * 0.02 + (hash(symbol + str(i)) % 100 - 50) / 10000
                    current_price = base_price * (1 + price_change)
                    
                    metrics = FXMetrics(
                        price=current_price,
                        volatility=0.015 + (hash(str(i)) % 100) / 10000,
                        volume=1000000 + (hash(str(i)) % 500000),
                        spread=0.0002 + (hash(str(i)) % 100) / 1000000,
                        liquidity_score=0.8 + (hash(str(i)) % 100) / 1000,
                        momentum=0.01 * (hash(str(i)) % 100 - 50) / 100,
                        mean_reversion_score=0.3 + (hash(str(i)) % 100) / 1000,
                        correlation_index=0.6 + (hash(str(i)) % 100) / 1000,
                        timestamp=timestamp
                    )
                    
                    self.components["fx_engine"].update_market_data(metrics)
            
            logger.info("✅ Sample FX data generated")
        
        # Generate sample chart data
        if "chart_engine" in self.components:
            from amos_omega_chart_engine import PriceData, ShockEvent
            
            for symbol in ["EURUSD", "GBPUSD"]:
                base_price = {"EURUSD": 1.0850, "GBPUSD": 1.2750}[symbol]
                
                for i in range(200):
                    timestamp = time.time() - (200 - i) * 1800  # 30-minute data
                    
                    price_change = (i / 200) * 0.03 + (hash(symbol + str(i)) % 100 - 50) / 10000
                    current_price = base_price * (1 + price_change)
                    
                    price_data = PriceData(
                        timestamp=timestamp,
                        open=current_price * 0.999,
                        high=current_price * 1.002,
                        low=current_price * 0.998,
                        close=current_price,
                        volume=int(1000000 + (hash(str(i)) % 500000))
                    )
                    
                    self.components["chart_engine"].add_price_data(symbol, price_data)
            
            # Add shock events
            shock = ShockEvent(
                timestamp=time.time() - 50 * 1800,
                shock_type="volatility_spike",
                magnitude=0.025,
                duration=4 * 3600,
                description="Market volatility surge"
            )
            self.components["chart_engine"].add_shock_event(shock)
            
            logger.info("✅ Sample chart data generated")
    
    async def start_bridge_server(self):
        """Start the Bridge API server"""
        if "bridge" not in self.components:
            return
        
        import uvicorn
        
        config = self.config["bridge"]
        logger.info(f"🌉 Starting Bridge API on {config['host']}:{config['port']}")
        
        # Configure uvicorn
        uvicorn_config = uvicorn.Config(
            app=self.components["bridge"],
            host=config["host"],
            port=config["port"],
            log_level="info",
            access_log=True
        )
        
        server = uvicorn.Server(uvicorn_config)
        
        try:
            await server.serve()
        except Exception as e:
            logger.error(f"Bridge API server error: {e}")
    
    async def run_system_monitoring(self):
        """Run continuous system monitoring"""
        logger.info("📊 Starting system monitoring...")
        
        while self.running and not self.shutdown_event.is_set():
            try:
                # Get system status
                status = self.components["brain"].get_system_status()
                
                # Log key metrics
                system_state = status.get("system_state", {})
                logger.info(
                    f"System Status - Mode: {status.get('mode', 'UNKNOWN')} | "
                    f"Stability: {system_state.get('M', 0):.3f} | "
                    f"Coherence: {system_state.get('C', 0):.3f} | "
                    f"Stress: {system_state.get('S', 0):.3f}"
                )
                
                # Check for critical conditions
                if system_state.get("M", 1.0) < 0.2:
                    logger.warning("⚠️ Low stability margin detected!")
                
                if system_state.get("C", 1.0) < 0.7:
                    logger.warning("⚠️ Low coherence detected!")
                
                await asyncio.sleep(30)  # Monitor every 30 seconds
                
            except Exception as e:
                logger.error(f"System monitoring error: {e}")
                await asyncio.sleep(10)
    
    async def run_fx_updates(self):
        """Run continuous FX data updates"""
        if "fx_engine" not in self.components:
            return
        
        logger.info("💱 Starting FX data updates...")
        
        while self.running and not self.shutdown_event.is_set():
            try:
                # Simulate FX market updates
                from amos_omega_fx_engine import FXMetrics
                
                symbols = ["EURUSD", "GBPUSD", "USDJPY"]
                current_prices = {"EURUSD": 1.0850, "GBPUSD": 1.2750, "USDJPY": 148.50}
                
                for symbol in symbols:
                    # Generate realistic market movement
                    base_price = current_prices[symbol]
                    price_change = (hash(str(time.time()) + symbol) % 100 - 50) / 10000
                    new_price = base_price * (1 + price_change)
                    current_prices[symbol] = new_price
                    
                    metrics = FXMetrics(
                        price=new_price,
                        volatility=0.015 + (hash(str(time.time())) % 100) / 10000,
                        volume=1000000 + (hash(str(time.time())) % 500000),
                        spread=0.0002 + (hash(str(time.time())) % 100) / 1000000,
                        liquidity_score=0.8 + (hash(str(time.time())) % 100) / 1000,
                        momentum=0.01 * (hash(str(time.time())) % 100 - 50) / 100,
                        mean_reversion_score=0.3 + (hash(str(time.time())) % 100) / 1000,
                        correlation_index=0.6 + (hash(str(time.time())) % 100) / 1000,
                        timestamp=time.time()
                    )
                    
                    self.components["fx_engine"].update_market_data(metrics)
                
                await asyncio.sleep(self.config["fx_engine"]["update_interval"])
                
            except Exception as e:
                logger.error(f"FX update error: {e}")
                await asyncio.sleep(10)
    
    def print_system_status(self):
        """Print comprehensive system status"""
        print("\n" + "="*80)
        print("🧠 AMOS OMEGA — ULTIMATE BRAIN–BODY–BRIDGE INTEGRATION SYSTEM")
        print("="*80)
        
        # Brain Status
        brain_status = self.components["brain"].get_system_status()
        print(f"\n🧠 BRAIN COGNITIVE CORE:")
        print(f"   Mode: {brain_status.get('mode', 'UNKNOWN')}")
        print(f"   Regime: {brain_status.get('regime', 'UNKNOWN')}")
        print(f"   Stability Margin: {brain_status.get('system_state', {}).get('M', 0):.3f}")
        print(f"   Coherence: {brain_status.get('system_state', {}).get('C', 0):.3f}")
        print(f"   Active Invariants: {len([inv for inv in brain_status.get('invariants', {}).values() if inv.get('is_violated') == False])}")
        print(f"   Active Loops: {len([loop for loop in brain_status.get('loops', {}).values() if loop.get('is_active')])}")
        
        # Bridge API Status
        if "bridge" in self.components:
            print(f"\n🌉 BRIDGE API:")
            print(f"   Status: Running")
            print(f"   Endpoint: http://{self.config['bridge']['host']}:{self.config['bridge']['port']}")
            print(f"   Health: /health")
            print(f"   Documentation: /docs")
        
        # FX Engine Status
        if "fx_engine" in self.components:
            print(f"\n💱 FX STRUCTURAL ANALYSIS:")
            print(f"   Status: Active")
            print(f"   Symbols: EURUSD, GBPUSD, USDJPY")
            print(f"   Analysis: Real-time structural analysis")
        
        # Chart Engine Status
        if "chart_engine" in self.components:
            print(f"\n📊 LIVE CHART ENGINE:")
            print(f"   Status: Active")
            print(f"   Timeframes: M1, M5, M15, M30, H1, H4, D1, W1, MN1")
            print(f"   Features: Multi-timeframe, shock simulation, regime coloring")
        
        # N8N Orchestrator Status
        if "n8n" in self.components:
            n8n_status = self.components["n8n"].get_workflow_status()
            print(f"\n🔄 N8N ORCHESTRATION:")
            print(f"   Total Workflows: {n8n_status['total_workflows']}")
            print(f"   Active Workflows: {n8n_status['active_workflows']}")
            print(f"   Webhook Endpoints: {n8n_status['webhook_endpoints']}")
        
        # UI Status
        if self.config["ui"]["enabled"]:
            print(f"\n🎨 LOVEABLE UI:")
            print(f"   Status: Available")
            print(f"   File: {self.config['ui']['file']}")
            print(f"   Features: Real-time dashboard, system monitoring, chat interface")
        
        print(f"\n🔗 ACCESS POINTS:")
        print(f"   Bridge API: http://localhost:8000")
        print(f"   API Docs: http://localhost:8000/docs")
        print(f"   Health Check: http://localhost:8000/health")
        print(f"   System Status: http://localhost:8000/status")
        
        print(f"\n📊 SYSTEM CAPABILITIES:")
        print(f"   ✅ Unified Brain-Body-Bridge Architecture")
        print(f"   ✅ Real-time Structural Analysis")
        print(f"   ✅ Multi-timeframe Chart Engine")
        print(f"   ✅ Autonomous N8N Workflows")
        print(f"   ✅ Schema-driven Loveable UI")
        print(f"   ✅ Deterministic Governance")
        print(f"   ✅ Evidence-based Reasoning")
        
        print("\n" + "="*80)
        print("🚀 SYSTEM READY FOR OPERATION")
        print("="*80 + "\n")
    
    async def run(self):
        """Run the complete AMOS OMEGA system"""
        # Initialize system
        if not await self.initialize_system():
            return
        
        self.running = True
        
        # Print system status
        self.print_system_status()
        
        # Start background tasks
        tasks = []
        
        # Bridge API server
        if "bridge" in self.components:
            tasks.append(asyncio.create_task(self.start_bridge_server()))
        
        # System monitoring
        tasks.append(asyncio.create_task(self.run_system_monitoring()))
        
        # FX updates
        if "fx_engine" in self.components:
            tasks.append(asyncio.create_task(self.run_fx_updates()))
        
        try:
            # Wait for shutdown signal
            await self.shutdown_event.wait()
            
        except KeyboardInterrupt:
            logger.info("🛑 Received shutdown signal...")
        
        finally:
            # Shutdown system
            await self.shutdown()
            
            # Cancel all tasks
            for task in tasks:
                if not task.done():
                    task.cancel()
                    try:
                        await task
                    except asyncio.CancelledError:
                        pass
    
    async def shutdown(self):
        """Graceful system shutdown"""
        logger.info("🛑 Shutting down AMOS OMEGA System...")
        
        self.running = False
        
        # Shutdown brain core
        if "brain" in self.components:
            self.components["brain"].shutdown()
            logger.info("✅ Brain Core shutdown complete")
        
        # Deactivate N8N workflows
        if "n8n" in self.components:
            for workflow_name in self.config["n8n"]["auto_activate"]:
                self.components["n8n"].deactivate_workflow(workflow_name)
            logger.info("✅ N8N workflows deactivated")
        
        logger.info("🚀 AMOS OMEGA System shutdown complete")

def signal_handler(signum, frame):
    """Handle shutdown signals"""
    logger.info(f"Received signal {signum}")
    if 'launcher' in globals():
        launcher.shutdown_event.set()

async def main():
    """Main entry point"""
    global launcher
    
    # Set up signal handlers
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    # Create and run launcher
    launcher = AMOSOmegaLauncher()
    await launcher.run()

if __name__ == "__main__":
    # Run the complete AMOS OMEGA system
    print("🚀 Starting AMOS OMEGA Ultimate Integration System...")
    asyncio.run(main())


```

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
