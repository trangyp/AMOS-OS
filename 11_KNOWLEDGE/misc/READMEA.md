---
title: READMEA
tags:
- misc
- reference
- general
- canon/knowledge
type: document
source: 11_KNOWLEDGE/misc
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---


# AMOS Brain Service - Complete Architecture

## Overview

AMOS Brain Service is a standalone AI operating system that runs as a persistent background service. It provides multi-model LLM routing, tool orchestration, memory management, and task processing through a clean FastAPI architecture.

## ️ Architecture

```
Dashboard (Claws/WebUI/Open WebUI)
        │
        ▼
AMOS Brain Service (FastAPI + AsyncIO)
        │
┌───────┼─────────────┐
│       │             │
ModelRouter   ToolRegistry   MemorySystem
│       │             │
│       ▼             ▼
│   Ollama LLM    MCP Tools   Neo4j/Qdrant
│
└───────┼─────────────┘
        ▼
    Task Queue (Redis)
```

## Core Components

### 1. Model Router
- **Multi-model routing** for optimal model selection
- **Model types**: Coding (DeepSeek), Reasoning (Qwen), Fast (Mistral), Math (WizardMath)
- **Auto-selection** based on request type and content analysis
- **Fallback handling** for unavailable models

### 2. Tool Registry
- **MCP integration** for external tools (GitHub, Zapier)
- **Local tools**: Filesystem, Browser, Calculator, Python Sandbox
- **ActionGate** security layer for permission checking
- **Tool capabilities** and authentication management

### 3. Memory System
- **Graph Memory** (Neo4j): Knowledge graphs, relationships, reasoning
- **Vector Memory** (Qdrant): Embeddings, retrieval, semantic search
- **Memory search** with context awareness
- **Automatic memory storage** from task results

### 4. Task Queue
- **Redis-based** task queuing for background processing
- **Async task processing** with priority handling
- **Task lifecycle management** (pending → processing → completed)
- **Result caching** and cleanup

### 5. API Layer
- **FastAPI** with async support
- **RESTful endpoints** for task management
- **WebSocket** for real-time chat
- **CORS middleware** for dashboard integration

## File Structure

```
/Users/trangphan/AMOS/39_BRAIN_SERVICE/
├── amos_brain_service.py      # Main service application
├── requirements.txt           # Python dependencies
├── setup.sh                  # Setup script
├── Dockerfile                # Docker configuration
├── docker-compose.yml        # Full stack deployment
├── amos-brain.service        # Systemd service file
└── README.md                 # This documentation
```

## Quick Start

### Option 1: Direct Setup

```bash
# Clone and setup
cd /Users/trangphan/AMOS/39_BRAIN_SERVICE
chmod +x setup.sh
./setup.sh

# Start services (in separate terminals)
ollama serve &
redis-server &

# Start AMOS
source amos_env/bin/activate
python3 amos_brain_service.py
```

### Option 2: Docker Setup

```bash
# Full stack deployment
docker-compose up -d

# Check status
docker-compose ps
```

### Option 3: Systemd Service

```bash
# Install as system service
sudo cp amos-brain.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable amos-brain
sudo systemctl start amos-brain
```

## External Services

### Required Services
- **Ollama**: `ollama serve` (http://localhost:11434)
- **Redis**: `redis-server` (localhost:6379)

### Optional Services
- **Neo4j**: Graph database for memory (http://localhost:7474)
- **Qdrant**: Vector database for memory (http://localhost:6333)

### Model Setup
```bash
# Download models for Ollama
ollama pull deepseek-coder
ollama pull qwen-72b
ollama pull mistral-7b
ollama pull wizardmath
ollama pull llama3
```

## API Endpoints

### Core Endpoints
- `POST /api/task` - Create new task
- `GET /api/task/{task_id}` - Get task status
- `POST /api/chat` - Direct chat endpoint
- `GET /api/models` - List available models
- `GET /api/tools` - List available tools
- `GET /api/status` - Service status

### WebSocket
- `ws://localhost:8000/ws/chat` - Real-time chat

### Documentation
- `http://localhost:8000/docs` - Interactive API docs
- `http://localhost:8000/redoc` - ReDoc documentation

## ️ Dashboard Integration

### Open WebUI (Recommended)
```bash
# Access via Docker Compose
http://localhost:3000
```

### Custom Dashboard
- Connect to `http://localhost:8000/api/chat`
- Use WebSocket for real-time updates
- Integrate with existing frontend frameworks

## Configuration

### Environment Variables
- `AMOS_OLLAMA_URL`: Ollama endpoint (default: http://localhost:11434)
- `AMOS_REDIS_URL`: Redis endpoint (default: redis://localhost:6379)
- `AMOS_NEO4J_URL`: Neo4j endpoint (default: bolt://localhost:7687)
- `AMOS_QDRANT_URL`: Qdrant endpoint (default: localhost:6333)

### Model Configuration
Edit `ModelRouter._initialize_models()` to add/remove models or adjust priorities.

### Tool Configuration
Edit `ToolRegistry._initialize_tools()` to add/remove tools or change capabilities.

## Security

### ActionGate
- **Permission checking** for all tool executions
- **Dangerous action filtering** (delete, remove, format, exec, system)
- **Protected path blocking** (/, /usr, /etc, /var)
- **Code injection prevention**

### Authentication
- **User ID tracking** for task isolation
- **API key support** for external integrations
- **Session management** for dashboard connections

## Monitoring

### Service Status
```bash
curl http://localhost:8000/api/status
```

### Health Checks
- **Service health**: `/api/status`
- **Model availability**: `/api/models`
- **Tool status**: `/api/tools`
- **Active tasks**: Included in status response

### Logging
- **Structured logging** with JSON format
- **Task execution logs** with timing
- **Error tracking** with stack traces
- **Performance metrics** collection

## Performance

### Async Processing
- **FastAPI + AsyncIO** for concurrent request handling
- **Background task processor** for queue management
- **Connection pooling** for database access
- **Caching** for frequently accessed data

### Optimization
- **Model selection** based on request complexity
- **Memory retrieval** with context filtering
- **Tool execution** with timeout handling
- **Result caching** for repeated requests

## Development

### Local Development
```bash
# Setup development environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run with auto-reload
uvicorn amos_brain_service:app --reload --host 0.0.0.0 --port 8000
```

### Testing
```bash
# Install test dependencies
pip install pytest pytest-asyncio

# Run tests
pytest tests/
```

### Code Structure
- **Modular design** with clear separation of concerns
- **Async/await** patterns throughout
- **Type hints** with Pydantic models
- **Error handling** with proper HTTP status codes

## Scaling

### Horizontal Scaling
- **Multiple instances** behind load balancer
- **Redis cluster** for distributed task queue
- **Database sharding** for memory systems
- **Model service** for dedicated LLM serving

### Vertical Scaling
- **Memory optimization** with connection pooling
- **CPU utilization** with async processing
- **I/O optimization** with streaming responses
- **Resource monitoring** with metrics collection

## Maintenance

### Updates
- **Rolling updates** with zero downtime
- **Configuration reload** without service restart
- **Model updates** with graceful fallback
- **Tool updates** with version management

### Backups
- **Database backups** for memory systems
- **Configuration backups** for service settings
- **Log rotation** for storage management
- **State persistence** for active tasks

## Use Cases

### AI Assistant
- **Multi-model routing** for optimal responses
- **Tool integration** for real-world actions
- **Memory system** for context awareness
- **Task queue** for background processing

### Code Generation
- **DeepSeek Coder** for code-specific tasks
- **File system tools** for code management
- **Python sandbox** for code execution
- **GitHub integration** for repository operations

### Research Assistant
- **Qwen 72B** for complex reasoning
- **Web search tools** for information gathering
- **Vector memory** for semantic search
- **Graph memory** for knowledge relationships

### Automation
- **Tool orchestration** for complex workflows
- **Zapier integration** for external services
- **Task queue** for reliable execution
- **Error handling** for robust automation

## Benefits

### Over Windsurf/VSCode
- **Persistent brain** that runs 24/7
- **Better performance** with dedicated resources
- **More control** over model selection and tools
- **Scalability** for multiple users and applications
- **Integration** with any dashboard or frontend

### Over Agent Frameworks
- **Deterministic execution** with clear state management
- **No chaos spawning** with controlled task processing
- **Real tool integration** with security boundaries
- **Memory persistence** with graph and vector capabilities
- **Production ready** with monitoring and observability

## Next Steps

1. **Install and configure** external services (Ollama, Redis)
2. **Deploy AMOS Brain Service** using preferred method
3. **Connect dashboard** (Open WebUI or custom)
4. **Test functionality** with sample tasks
5. **Configure models** and tools for specific use cases
6. **Monitor performance** and optimize as needed

## Support

### Documentation
- **API docs**: http://localhost:8000/docs
- **Code comments**: Inline documentation
- **README files**: Component-specific documentation

### Troubleshooting
- **Service logs**: Check service output for errors
- **External services**: Verify Ollama and Redis are running
- **Network**: Check port availability and firewall settings
- **Dependencies**: Verify all required packages are installed

---

**AMOS Brain Service** is now ready to run as a persistent AI operating system, providing superior performance, control, and scalability compared to editor-based solutions.

---
**Links:** [[MISC_MOC]] | [[KNOWLEDGE_MOC]]
