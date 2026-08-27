---
title: deployment guide
type: reference
source: 07_SKILLS/amos-c10-tech-engineering-master/references
tags: [reference, amos-c10-tech-engineering-master, canon/skill]
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---


# Deployment Guide

> Source: `_00_Cosmo brain/specs/DEPLOYMENT_GUIDE.md`
> Epistemic class: SOURCE_DERIVED

---
tags: [specs]
---
# AMOS Production Deployment Guide

## Overview

This guide provides comprehensive instructions for deploying the AMOS self-healing repository system in production environments.

## Prerequisites

### System Requirements

- **Operating System**: Linux (Ubuntu 20.04+, CentOS 8+, RHEL 8+)
- **Python**: 3.8 or higher
- **Memory**: Minimum 1GB RAM (recommended 2GB+)
- **Disk Space**: Minimum 5GB free space (recommended 10GB+)
- **Permissions**: Read/write access to repository directory

### Python Dependencies

The following Python packages are required:

```bash
pip3 install numpy scipy scikit-learn aiohttp psutil
```

### System Commands

Ensure these system commands are available:
- `python3`
- `pip3`
- `chmod`
- `kill`
- `ps`

## Quick Start

### 1. Environment Validation

```bash
python3 /Users/trangphan/AMOS/01_BRAIN/deploy_amos_production.py validate
```

### 2. Full Deployment

```bash
python3 /Users/trangphan/AMOS/01_BRAIN/deploy_amos_production.py deploy
```

### 3. Service Status Check

```bash
python3 /Users/trangphan/AMOS/01_BRAIN/deploy_amos_production.py status
```

## Detailed Deployment

### Step 1: Repository Preparation

1. **Clone/Update Repository**
   ```bash
   cd /path/to/amos
   git pull origin main
   ```

2. **Verify Repository Structure**
   ```bash
   ls -la 01_BRAIN/
   ls -la 01_KERNEL/
   ls -la 17_OS/audits/
   ```

### Step 2: Environment Setup

1. **Create AMOS User (Optional)**
   ```bash
   sudo useradd -r -s /bin/false amos
   sudo usermod -L amos
   ```

2. **Set Permissions**
   ```bash
   sudo chown -R $USER:$USER /path/to/amos
   chmod 755 /path/to/amos
   ```

### Step 3: Configuration

1. **Production Configuration**
   The deployment script automatically creates production configuration at:
   ```
   ~/.amos/config/production_config.json
   ```

2. **Custom Configuration**
   Edit the configuration file to customize:
   - Scan intervals
   - Threat thresholds
   - Cache settings
   - Monitoring parameters

### Step 4: Service Installation

#### Option A: Systemd Service (Recommended)

1. **Create Service File**
   ```bash
   python3 /Users/trangphan/AMOS/01_BRAIN/deploy_amos_production.py deploy
   ```

2. **Enable and Start Service**
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable amos
   sudo systemctl start amos
   ```

3. **Check Service Status**
   ```bash
   sudo systemctl status amos
   ```

#### Option B: Manual Process

1. **Start Service Manually**
   ```bash
   python3 /Users/trangphan/AMOS/01_BRAIN/deploy_amos_production.py start
   ```

2. **Check Process**
   ```bash
   ps aux | grep amos_integrated_system
   ```

### Step 5: Monitoring Setup

1. **Log Monitoring**
   Logs are written to:
   ```
   ~/.amos/logs/amos_production.log
   ```

2. **Health Checks**
   ```bash
   python3 /Users/trangphan/AMOS/01_BRAIN/deploy_amos_production.py health
   ```

3. **Audit Files**
   Audit reports are generated in:
   ```
   17_OS/audits/
   ```

## Configuration Reference

### Production Config Structure

```json
{
  "deployment": {
    "environment": "production",
    "deployed_at": "2026-03-02T00:00:00Z",
    "deployed_by": "user",
    "version": "1.0.0"
  },
  "system": {
    "scan_interval": 60,
    "threat_threshold": 0.7,
    "auto_freeze_enabled": true,
    "cache_optimization_interval": 300,
    "log_level": "INFO"
  },
  "performance": {
    "cache_max_size": 1000,
    "cache_ttl": 3600,
    "max_concurrent_scans": 5,
    "memory_limit_mb": 1024
  },
  "monitoring": {
    "health_check_interval": 30,
    "metrics_retention_days": 7,
    "alert_thresholds": {
      "threat_level": 0.8,
      "memory_usage": 0.9,
      "disk_usage": 0.9
    }
  },
  "security": {
    "freeze_zone_auto_activate": true,
    "evidence_integrity_threshold": 0.8,
    "audit_retention_days": 30
  }
}
```

### Key Parameters

| Parameter | Description | Default | Recommended |
|------------|-------------|---------|-------------|
| `scan_interval` | Repositor

---
**MOC:** [[references_MOC]]

## Related

- [[07_SKILLS_MOC]]
