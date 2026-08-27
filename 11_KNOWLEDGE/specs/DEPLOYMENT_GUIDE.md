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
| `scan_interval` | Repository scan frequency (seconds) | 60 | 60-300 |
| `threat_threshold` | Threat level for FreezeZone activation | 0.7 | 0.6-0.8 |
| `cache_max_size` | Maximum cache entries | 1000 | 500-2000 |
| `cache_ttl` | Cache TTL (seconds) | 3600 | 1800-7200 |
| `memory_limit_mb` | Memory limit (MB) | 1024 | 512-2048 |

## Service Management

### Systemd Commands

```bash
# Start service
sudo systemctl start amos

# Stop service
sudo systemctl stop amos

# Restart service
sudo systemctl restart amos

# Enable auto-start
sudo systemctl enable amos

# Disable auto-start
sudo systemctl disable amos

# View logs
sudo journalctl -u amos -f
```

### Manual Commands

```bash
# Start service
python3 /Users/trangphan/AMOS/01_BRAIN/deploy_amos_production.py start

# Stop service
python3 /Users/trangphan/AMOS/01_BRAIN/deploy_amos_production.py stop

# Restart service
python3 /Users/trangphan/AMOS/01_BRAIN/deploy_amos_production.py restart

# Check status
python3 /Users/trangphan/AMOS/01_BRAIN/deploy_amos_production.py status

# Health check
python3 /Users/trangphan/AMOS/01_BRAIN/deploy_amos_production.py health
```

## Monitoring and Maintenance

### Health Monitoring

1. **System Health**
   ```bash
   python3 /Users/trangphan/AMOS/01_BRAIN/deploy_amos_production.py health
   ```

2. **Log Monitoring**
   ```bash
   tail -f ~/.amos/logs/amos_production.log
   ```

3. **Audit Review**
   ```bash
   ls -la 17_OS/audits/
   cat 17_OS/audits/current_system_status.json
   ```

### Performance Monitoring

1. **Cache Performance**
   Check cache hit rates and optimization in audit files.

2. **Memory Usage**
   Monitor memory consumption and adjust `memory_limit_mb` if needed.

3. **Disk Usage**
   Ensure adequate disk space for logs and cache files.

### Maintenance Tasks

1. **Log Rotation**
   Automatic log rotation is configured. Check `/etc/logrotate.d/amos`.

2. **Cache Cleanup**
   Cache automatically optimizes. Manual cleanup available if needed.

3. **Audit Cleanup**
   Old audit files are automatically pruned based on retention settings.

## Troubleshooting

### Common Issues

#### Service Won't Start

1. **Check Dependencies**
   ```bash
   python3 /Users/trangphan/AMOS/01_BRAIN/deploy_amos_production.py validate
   ```

2. **Check Permissions**
   ```bash
   ls -la ~/.amos/
   chmod 755 ~/.amos/
   ```

3. **Check Logs**
   ```bash
   cat ~/.amos/logs/amos_production.log
   ```

#### High Memory Usage

1. **Reduce Cache Size**
   Edit `production_config.json`:
   ```json
   "performance": {
     "cache_max_size": 500,
     "memory_limit_mb": 512
   }
   ```

2. **Restart Service**
   ```bash
   python3 /Users/trangphan/AMOS/01_BRAIN/deploy_amos_production.py restart
   ```

#### FreezeZone Activation

1. **Check Threat Level**
   ```bash
   cat 17_OS/audits/latest_immune_response.json
   ```

2. **Adjust Threshold**
   Edit `production_config.json`:
   ```json
   "system": {
     "threat_threshold": 0.8
   }
   ```

3. **Manual Deactivation**
   ```bash
   python3 /Users/trangphan/AMOS/01_BRAIN/deploy_amos_production.py restart
   ```

### Debug Mode

Enable debug logging by editing the configuration:

```json
{
  "system": {
    "log_level": "DEBUG"
  }
}
```

## Security Considerations

### File Permissions

- Repository directory: 755
- Configuration files: 644
- Log files: 644
- PID file: 644

### Network Security

- AMOS does not require network access for basic operation
- Internet features can be disabled in configuration

### Access Control

- Run as non-root user when possible
- Restrict access to configuration files
- Monitor audit logs for security events

## Performance Tuning

### Cache Optimization

1. **Monitor Hit Rates**
   Check cache performance in audit files.

2. **Adjust Cache Size**
   Based on available memory and hit rates.

3. **TTL Optimization**
   Balance freshness with performance.

### Scan Frequency

1. **Active Repositories**: 60-300 seconds
2. **Inactive Repositories**: 300-900 seconds
3. **Large Repositories**: Consider longer intervals

### Memory Management

1. **Monitor Usage**
   Regular health checks include memory monitoring.

2. **Set Limits**
   Configure `memory_limit_mb` appropriately.

3. **Cache Tuning**
   Reduce cache size if memory is constrained.

## Integration Examples

### CI/CD Integration

```yaml
# GitHub Actions example
- name: Deploy AMOS
  run: |
    python3 deploy_amos_production.py deploy
    python3 deploy_amos_production.py health
```

### Docker Integration

```dockerfile
FROM python:3.9-slim

# Install dependencies
RUN pip3 install numpy scipy scikit-learn aiohttp psutil

# Copy AMOS
COPY . /amos
WORKDIR /amos

# Deploy
RUN python3 01_BRAIN/deploy_amos_production.py deploy

# Run
CMD ["python3", "01_BRAIN/deploy_amos_production.py", "start"]
```

### Monitoring Integration

```bash
# Prometheus exporter example
curl -s http://localhost:8080/health | jq '.overall_status'
```

## Support

### Getting Help

1. **Check Logs**: `~/.amos/logs/amos_production.log`
2. **Health Check**: `python3 deploy_amos_production.py health`
3. **Status**: `python3 deploy_amos_production.py status`

### Reporting Issues

Include:
- System information
- Configuration file
- Log files
- Health check results
- Error messages

### Community Resources

- Repository: `/Users/trangphan/AMOS`
- Documentation: `01_BRAIN/` directory
- Audit files: `17_OS/audits/`

## Version History

- **v1.0.0**: Initial production deployment
- **v1.1.0**: Added health monitoring
- **v1.2.0**: Performance optimizations
- **v1.3.0**: Enhanced security features

---

**Note**: This guide is for the AMOS self-healing repository system. Ensure you have the correct version and follow all security best practices.
