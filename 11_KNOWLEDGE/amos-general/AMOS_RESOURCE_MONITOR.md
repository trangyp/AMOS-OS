---
title: AMOS RESOURCE MONITOR
tags: [amos-general, amos, general]
type: document
source: 11_KNOWLEDGE/amos-general
---




# amos_resource_monitor

```python
#!/usr/bin/env python3
"""
AMOS BRAIN - RESOURCE MONITOR AND OPTIMIZER
MODE: MINIMAL FOOTPRINT • MAXIMUM EFFICIENCY • CPU/RAM OPTIMIZATION
"""

import os
import psutil
import time
import gc
import threading
from typing import Dict, List, Optional
from dataclasses import dataclass
import logging

# Configure minimal logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger("AMOS_MONITOR")

@dataclass
class ResourceMetrics:
    """Resource usage metrics"""
    cpu_percent: float
    memory_percent: float
    memory_mb: float
    disk_percent: float
    process_count: int
    thread_count: int
    timestamp: float

class AMOSResourceMonitor:
    """AMOS BRAIN Resource Monitor and Optimizer"""
    
    def __init__(self):
        self.monitoring = False
        self.monitor_thread = None
        self.metrics_history = []
        self.max_history = 100
        self.alert_thresholds = {
            "cpu_percent": 80.0,
            "memory_percent": 80.0,
            "disk_percent": 90.0
        }
        self.optimization_enabled = True
        
    def start_monitoring(self, interval: float = 5.0):
        """Start resource monitoring"""
        if self.monitoring:
            return
        
        self.monitoring = True
        self.monitor_thread = threading.Thread(target=self._monitor_loop, args=(interval,))
        self.monitor_thread.daemon = True
        self.monitor_thread.start()
        print("📊 Resource monitoring started")
    
    def stop_monitoring(self):
        """Stop resource monitoring"""
        self.monitoring = False
        if self.monitor_thread:
            self.monitor_thread.join(timeout=1.0)
        print("📊 Resource monitoring stopped")
    
    def _monitor_loop(self, interval: float):
        """Monitoring loop"""
        while self.monitoring:
            try:
                metrics = self._collect_metrics()
                self.metrics_history.append(metrics)
                
                # Keep history limited
                if len(self.metrics_history) > self.max_history:
                    self.metrics_history.pop(0)
                
                # Check for alerts
                self._check_alerts(metrics)
                
                # Auto-optimize if needed
                if self.optimization_enabled:
                    self._auto_optimize(metrics)
                
                time.sleep(interval)
                
            except Exception as e:
                logger.error(f"Monitor loop error: {e}")
                time.sleep(interval)
    
    def _collect_metrics(self) -> ResourceMetrics:
        """Collect current resource metrics"""
        # CPU metrics
        cpu_percent = psutil.cpu_percent(interval=0.1)
        
        # Memory metrics
        memory = psutil.virtual_memory()
        memory_mb = memory.used / (1024 * 1024)
        
        # Disk metrics
        disk = psutil.disk_usage('/')
        disk_percent = disk.percent
        
        # Process and thread counts (with error handling)
        process_count = len(psutil.pids())
        thread_count = 0
        try:
            thread_count = sum(p.num_threads() for p in psutil.process_iter() if hasattr(p, 'num_threads'))
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            # Fallback: estimate thread count
            thread_count = process_count * 2  # Rough estimate
        
        return ResourceMetrics(
            cpu_percent=cpu_percent,
            memory_percent=memory.percent,
            memory_mb=memory_mb,
            disk_percent=disk_percent,
            process_count=process_count,
            thread_count=thread_count,
            timestamp=time.time()
        )
    
    def _check_alerts(self, metrics: ResourceMetrics):
        """Check for resource alerts"""
        alerts = []
        
        if metrics.cpu_percent > self.alert_thresholds["cpu_percent"]:
            alerts.append(f"⚠️ High CPU usage: {metrics.cpu_percent:.1f}%")
        
        if metrics.memory_percent > self.alert_thresholds["memory_percent"]:
            alerts.append(f"⚠️ High memory usage: {metrics.memory_percent:.1f}%")
        
        if metrics.disk_percent > self.alert_thresholds["disk_percent"]:
            alerts.append(f"⚠️ High disk usage: {metrics.disk_percent:.1f}%")
        
        if alerts:
            for alert in alerts:
                print(alert)
    
    def _auto_optimize(self, metrics: ResourceMetrics):
        """Auto-optimize based on metrics"""
        # Force garbage collection if memory is high
        if metrics.memory_percent > 70:
            gc.collect()
            print("🧹 Auto garbage collection triggered")
        
        # Alert about high process count
        if metrics.process_count > 500:
            print(f"📈 High process count: {metrics.process_count}")
    
    def get_current_metrics(self) -> ResourceMetrics:
        """Get current resource metrics"""
        return self._collect_metrics()
    
    def get_metrics_summary(self) -> Dict:
        """Get metrics summary"""
        if not self.metrics_history:
            current = self._collect_metrics()
            return {
                "current": current,
                "average": current,
                "peak": current,
                "samples": 1
            }
        
        # Calculate averages and peaks
        current = self.metrics_history[-1]
        
        avg_cpu = sum(m.cpu_percent for m in self.metrics_history) / len(self.metrics_history)
        avg_memory = sum(m.memory_percent for m in self.metrics_history) / len(self.metrics_history)
        avg_disk = sum(m.disk_percent for m in self.metrics_history) / len(self.metrics_history)
        
        peak_cpu = max(m.cpu_percent for m in self.metrics_history)
        peak_memory = max(m.memory_percent for m in self.metrics_history)
        peak_disk = max(m.disk_percent for m in self.metrics_history)
        
        return {
            "current": current,
            "average": ResourceMetrics(
                cpu_percent=avg_cpu,
                memory_percent=avg_memory,
                memory_mb=current.memory_mb,
                disk_percent=avg_disk,
                process_count=current.process_count,
                thread_count=current.thread_count,
                timestamp=current.timestamp
            ),
            "peak": ResourceMetrics(
                cpu_percent=peak_cpu,
                memory_percent=peak_memory,
                memory_mb=current.memory_mb,
                disk_percent=peak_disk,
                process_count=current.process_count,
                thread_count=current.thread_count,
                timestamp=current.timestamp
            ),
            "samples": len(self.metrics_history)
        }
    
    def optimize_system(self) -> Dict:
        """Manual system optimization"""
        print("🔧 Performing system optimization...")
        
        # Force garbage collection
        collected = gc.collect()
        
        # Get current metrics
        current = self._collect_metrics()
        
        optimization_results = {
            "garbage_collected": collected,
            "memory_before": current.memory_mb,
            "memory_after": current.memory_mb,  # Will be updated after GC
            "optimization_time": time.time()
        }
        
        # Get metrics after optimization
        time.sleep(0.1)  # Small delay for metrics to update
        after_metrics = self._collect_metrics()
        optimization_results["memory_after"] = after_metrics.memory_mb
        optimization_results["memory_saved"] = optimization_results["memory_before"] - optimization_results["memory_after"]
        
        print(f"✅ Optimization complete: {collected} objects collected, {optimization_results['memory_saved']:.1f}MB saved")
        
        return optimization_results
    
    def set_alert_thresholds(self, cpu: float = 80.0, memory: float = 80.0, disk: float = 90.0):
        """Set alert thresholds"""
        self.alert_thresholds = {
            "cpu_percent": cpu,
            "memory_percent": memory,
            "disk_percent": disk
        }
        print(f"📊 Alert thresholds set: CPU={cpu}%, Memory={memory}%, Disk={disk}%")
    
    def enable_optimization(self, enabled: bool = True):
        """Enable or disable auto-optimization"""
        self.optimization_enabled = enabled
        print(f"🔧 Auto-optimization {'enabled' if enabled else 'disabled'}")

# Global resource monitor instance
resource_monitor = AMOSResourceMonitor()

if __name__ == "__main__":
    print("📊 AMOS BRAIN - RESOURCE MONITOR AND OPTIMIZER")
    print("="*60)
    
    # Start monitoring
    resource_monitor.start_monitoring(interval=2.0)
    
    # Show current metrics
    current = resource_monitor.get_current_metrics()
    print(f"\n📈 Current Resource Usage:")
    print(f"   CPU: {current.cpu_percent:.1f}%")
    print(f"   Memory: {current.memory_percent:.1f}% ({current.memory_mb:.1f}MB)")
    print(f"   Disk: {current.disk_percent:.1f}%")
    print(f"   Processes: {current.process_count}")
    print(f"   Threads: {current.thread_count}")
    
    # Monitor for 10 seconds
    print(f"\n⏱️ Monitoring for 10 seconds...")
    time.sleep(10)
    
    # Show summary
    summary = resource_monitor.get_metrics_summary()
    print(f"\n📊 Monitoring Summary:")
    print(f"   Samples: {summary['samples']}")
    print(f"   Average CPU: {summary['average'].cpu_percent:.1f}%")
    print(f"   Average Memory: {summary['average'].memory_percent:.1f}%")
    print(f"   Peak CPU: {summary['peak'].cpu_percent:.1f}%")
    print(f"   Peak Memory: {summary['peak'].memory_percent:.1f}%")
    
    # Perform optimization
    optimization = resource_monitor.optimize_system()
    print(f"\n🔧 Optimization Results:")
    print(f"   Objects Collected: {optimization['garbage_collected']}")
    print(f"   Memory Saved: {optimization['memory_saved']:.1f}MB")
    
    # Stop monitoring
    resource_monitor.stop_monitoring()
    
    print(f"\n🚀 Resource monitoring complete")


```

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[AMOS-GENERAL_MOC]]
