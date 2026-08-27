---
tags: [brain]
---
# amos_brain_governor_enhanced

```python
#!/usr/bin/env python3
"""
AMOS Brain Omega Ultimate Git Safety + Performance + Coherence Governor
Phase B: Incremental Scan Ledger + File Watcher - Enhanced with Strongest AMOS Brain
"""

import ast
import hashlib
import json
import os
import sys
import time
import numpy as np
from pathlib import Path
from typing import Dict, List, Set, Tuple, Optional, Any
from dataclasses import dataclass, asdict
from datetime import datetime
import logging
from collections import defaultdict
import threading
import sqlite3

# Import strongest AMOS Brain Omega Ultimate
sys.path.insert(0, str(Path(__file__).parent / "01_BRAIN"))
try:
    from amos_brain_omega_ultimate_2025 import AMOSBrainOmegaUltimate
except ImportError:
    logging.warning("Could not import AMOS Brain Omega Ultimate - using fallback")
    AMOSBrainOmegaUltimate = None

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class LedgerEntry:
    """Deterministic ledger entry for incremental scanning"""
    file_path: str
    file_hash: str
    parse_version: str
    imports: List[Dict[str, Any]]
    symbols: List[Dict[str, Any]]
    write_sites: List[Dict[str, Any]]
    last_modified: float
    size: int

@dataclass
class FileChangeEvent:
    """File system change event"""
    path: str
    event_type: str  # created, modified, deleted, moved
    timestamp: float
    old_path: Optional[str] = None

class IncrementalLedger:
    """Deterministic incremental scan ledger with AMOS Brain enhancement"""
    
    def __init__(self, repo_root: Path, ledger_path: Optional[Path] = None):
        self.repo_root = repo_root
        self.ledger_path = ledger_path or repo_root / ".amos" / "incremental_ledger.db"
        self.ledger_path.parent.mkdir(parents=True, exist_ok=True)
        
        # AMOS Brain integration
        self.amos_brain = None
        self.session_id = hashlib.sha256(str(time.time()).encode()).hexdigest()[:16]
        
        # Initialize database
        self._init_database()
        
        # Parse version for cache invalidation
        self.parse_version = "1.0.0"
        
        logger.info(f"📚 Incremental Ledger initialized: {self.ledger_path}")
    
    def _init_database(self):
        """Initialize SQLite database for ledger storage"""
        with sqlite3.connect(self.ledger_path) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS ledger (
                    file_path TEXT PRIMARY KEY,
                    file_hash TEXT NOT NULL,
                    parse_version TEXT NOT NULL,
                    imports TEXT NOT NULL,
                    symbols TEXT NOT NULL,
                    write_sites TEXT NOT NULL,
                    last_modified REAL NOT NULL,
                    size INTEGER NOT NULL,
                    scan_timestamp REAL NOT NULL
                )
            ''')
            
            conn.execute('''
                CREATE INDEX IF NOT EXISTS idx_file_hash ON ledger(file_hash)
            ''')
            
            conn.execute('''
                CREATE INDEX IF NOT EXISTS idx_last_modified ON ledger(last_modified)
            ''')
    
    def compute_file_hash(self, file_path: Path) -> str:
        """Compute SHA256 hash of file content"""
        hasher = hashlib.sha256()
        try:
            with open(file_path, 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hasher.update(chunk)
            return hasher.hexdigest()
        except Exception as e:
            logger.warning(f"Could not hash {file_path}: {e}")
            return ""
    
    def parse_file_content(self, file_path: Path) -> Dict[str, Any]:
        """Parse file content for imports, symbols, and write sites"""
        result = {
            'imports': [],
            'symbols': [],
            'write_sites': []
        }
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            tree = ast.parse(content, filename=str(file_path))
            
            # Parse imports
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        result['imports'].append({
                            'module': alias.name,
                            'name': alias.name,
                            'alias': alias.asname,
                            'line': node.lineno,
                            'level': 1
                        })
                elif isinstance(node, ast.ImportFrom):
                    module = node.module or ""
                    for alias in node.names:
                        result['imports'].append({
                            'module': module,
                            'name': alias.name,
                            'alias': alias.asname,
                            'line': node.lineno,
                            'level': node.level
                        })
                
                # Parse symbols
                if isinstance(node, ast.ClassDef):
                    result['symbols'].append({
                        'name': node.name,
                        'kind': 'class',
                        'line_start': node.lineno,
                        'line_end': node.end_lineno or node.lineno
                    })
                elif isinstance(node, ast.FunctionDef):
                    result['symbols'].append({
                        'name': node.name,
                        'kind': 'function',
                        'line_start': node.lineno,
                        'line_end': node.end_lineno or node.lineno
                    })
            
            # Parse write sites (simplified)
            lines = content.split('\n')
            for i, line in enumerate(lines, 1):
                if any(api in line for api in ['open(', 'write(', 'mkdir(', 'shutil.', 'subprocess.']):
                    result['write_sites'].append({
                        'line': i,
                        'api_type': 'write',
                        'target': line[:100].strip()
                    })
        
        except Exception as e:
            logger.warning(f"Could not parse {file_path}: {e}")
        
        return result
    
    def get_file_info(self, file_path: Path) -> Optional[Dict[str, Any]]:
        """Get file information from ledger"""
        try:
            stat_info = file_path.stat()
            return {
                'path': str(file_path.relative_to(self.repo_root)),
                'hash': self.compute_file_hash(file_path),
                'size': stat_info.st_size,
                'last_modified': stat_info.st_mtime
            }
        except (OSError, FileNotFoundError):
            return None
    
    def update_ledger_entry(self, file_path: Path, force: bool = False) -> Optional[LedgerEntry]:
        """Update or create ledger entry for a file"""
        file_info = self.get_file_info(file_path)
        if not file_info:
            return None
        
        rel_path = file_info['path']
        
        # Check if update is needed
        if not force:
            with sqlite3.connect(self.ledger_path) as conn:
                cursor = conn.execute(
                    'SELECT file_hash, last_modified FROM ledger WHERE file_path = ?',
                    (rel_path,)
                )
                existing = cursor.fetchone()
                
                if existing and existing[0] == file_info['hash'] and existing[1] == file_info['last_modified']:
                    return None  # No update needed
        
        # Parse file content
        parsed = self.parse_file_content(file_path)
        
        # Create ledger entry
        entry = LedgerEntry(
            file_path=rel_path,
            file_hash=file_info['hash'],
            parse_version=self.parse_version,
            imports=parsed['imports'],
            symbols=parsed['symbols'],
            write_sites=parsed['write_sites'],
            last_modified=file_info['last_modified'],
            size=file_info['size']
        )
        
        # Store in database
        with sqlite3.connect(self.ledger_path) as conn:
            conn.execute('''
                INSERT OR REPLACE INTO ledger 
                (file_path, file_hash, parse_version, imports, symbols, write_sites, last_modified, size, scan_timestamp)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                entry.file_path,
                entry.file_hash,
                entry.parse_version,
                json.dumps(entry.imports),
                json.dumps(entry.symbols),
                json.dumps(entry.write_sites),
                entry.last_modified,
                entry.size,
                time.time()
            ))
        
        return entry
    
    def get_changed_files(self, since: Optional[float] = None) -> List[str]:
        """Get list of files changed since timestamp"""
        if since is None:
            since = time.time() - 3600  # Default to last hour
        
        with sqlite3.connect(self.ledger_path) as conn:
            cursor = conn.execute(
                'SELECT file_path FROM ledger WHERE last_modified > ? ORDER BY last_modified',
                (since,)
            )
            return [row[0] for row in cursor.fetchall()]
    
    def get_all_entries(self) -> List[LedgerEntry]:
        """Get all ledger entries"""
        with sqlite3.connect(self.ledger_path) as conn:
            cursor = conn.execute('SELECT * FROM ledger ORDER BY file_path')
            entries = []
            for row in cursor.fetchall():
                entries.append(LedgerEntry(
                    file_path=row[0],
                    file_hash=row[1],
                    parse_version=row[2],
                    imports=json.loads(row[3]),
                    symbols=json.loads(row[4]),
                    write_sites=json.loads(row[5]),
                    last_modified=row[6],
                    size=row[7]
                ))
            return entries
    
    def remove_entry(self, file_path: str):
        """Remove entry from ledger (for deleted files)"""
        with sqlite3.connect(self.ledger_path) as conn:
            conn.execute('DELETE FROM ledger WHERE file_path = ?', (file_path,))
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get ledger statistics"""
        with sqlite3.connect(self.ledger_path) as conn:
            cursor = conn.execute('''
                SELECT 
                    COUNT(*) as total_files,
                    SUM(size) as total_size,
                    AVG(size) as avg_size,
                    MAX(last_modified) as last_scan
                FROM ledger
            ''')
            stats = cursor.fetchone()
            
            cursor = conn.execute('''
                SELECT parse_version, COUNT(*) as count 
                FROM ledger 
                GROUP BY parse_version
            ''')
            versions = dict(cursor.fetchall())
            
            return {
                'total_files': stats[0] or 0,
                'total_size': stats[1] or 0,
                'avg_size': stats[2] or 0,
                'last_scan': stats[3] or 0,
                'parse_versions': versions,
                'current_version': self.parse_version
            }

class FileWatcher:
    """File system watcher with AMOS Brain enhancement"""
    
    def __init__(self, repo_root: Path, ledger: IncrementalLedger):
        self.repo_root = repo_root
        self.ledger = ledger
        self.running = False
        self.callbacks = []
        self.debounce_time = 1.0  # 1 second debounce
        self.pending_changes = {}
        self.lock = threading.Lock()
        
        # AMOS Brain integration
        self.amos_brain = None
        if AMOSBrainOmegaUltimate:
            try:
                self.amos_brain = AMOSBrainOmegaUltimate(repo_root)
                logger.info("🧠 FileWatcher enhanced with AMOS Brain Omega Ultimate")
            except Exception as e:
                logger.warning(f"Could not initialize AMOS Brain for FileWatcher: {e}")
    
    def add_callback(self, callback):
        """Add callback for file changes"""
        self.callbacks.append(callback)
    
    def _process_change(self, file_path: Path, event_type: str):
        """Process file system change"""
        with self.lock:
            rel_path = str(file_path.relative_to(self.repo_root))
            self.pending_changes[rel_path] = {
                'path': rel_path,
                'event_type': event_type,
                'timestamp': time.time()
            }
    
    def _debounce_changes(self):
        """Debounce and batch process changes"""
        while self.running:
            time.sleep(self.debounce_time)
            
            with self.lock:
                if not self.pending_changes:
                    continue
                
                # Process pending changes
                changes = list(self.pending_changes.values())
                self.pending_changes.clear()
            
            # Sort changes deterministically
            changes.sort(key=lambda x: x['path'])
            
            # Process each change
            for change in changes:
                file_path = self.repo_root / change['path']
                
                if change['event_type'] == 'deleted':
                    self.ledger.remove_entry(change['path'])
                elif file_path.exists():
                    self.ledger.update_ledger_entry(file_path, force=True)
                
                # Notify callbacks
                for callback in self.callbacks:
                    try:
                        callback(change)
                    except Exception as e:
                        logger.error(f"Callback error: {e}")
    
    def start(self):
        """Start file watcher (simplified polling version)"""
        self.running = True
        self.thread = threading.Thread(target=self._debounce_changes, daemon=True)
        self.thread.start()
        logger.info("👁️ FileWatcher started")
    
    def stop(self):
        """Stop file watcher"""
        self.running = False
        if hasattr(self, 'thread'):
            self.thread.join()
        logger.info("👁️ FileWatcher stopped")
    
    def scan_changes(self) -> List[FileChangeEvent]:
        """Scan for changes since last scan"""
        changes = []
        last_scan = time.time() - 300  # 5 minutes ago
        
        for file_path in self.repo_root.rglob("*.py"):
            if file_path.is_file():
                try:
                    stat_info = file_path.stat()
                    if stat_info.st_mtime > last_scan:
                        rel_path = str(file_path.relative_to(self.repo_root))
                        changes.append(FileChangeEvent(
                            path=rel_path,
                            event_type='modified',
                            timestamp=stat_info.st_mtime
                        ))
                except (OSError, FileNotFoundError):
                    continue
        
        return changes

class AMOSBrainGovernorEnhanced:
    """Enhanced AMOS Brain Governor with Incremental Ledger and File Watcher"""
    
    def __init__(self, repo_root: str):
        self.repo_root = Path(repo_root).resolve()
        self.session_id = hashlib.sha256(str(time.time()).encode()).hexdigest()[:16]
        
        # Initialize components
        self.ledger = IncrementalLedger(self.repo_root)
        self.watcher = FileWatcher(self.repo_root, self.ledger)
        
        # AMOS Brain integration
        self.amos_brain = None
        if AMOSBrainOmegaUltimate:
            try:
                self.amos_brain = AMOSBrainOmegaUltimate(self.repo_root)
                logger.info(f"🧠 AMOS Brain Omega Ultimate ACTIVATED - Session: {self.session_id}")
            except Exception as e:
                logger.warning(f"Could not initialize AMOS Brain Omega Ultimate: {e}")
        
        # Governance components
        self.risk_score = 0.0
        self.freeze_zone_active = False
        self.evidence_integrity_threshold = 0.80
        
        logger.info(f"🚀 AMOS Brain Governor Enhanced initialized - Session: {self.session_id}")
    
    def build_initial_ledger(self) -> Dict[str, Any]:
        """Build initial ledger (Phase A equivalent)"""
        logger.info("📚 Building initial incremental ledger...")
        start_time = time.time()
        
        python_files = list(self.repo_root.rglob("*.py"))
        processed = 0
        errors = 0
        
        for py_file in python_files:
            if py_file.name.startswith('.') or py_file.suffix == '.pyc':
                continue
            
            try:
                entry = self.ledger.update_ledger_entry(py_file, force=True)
                if entry:
                    processed += 1
            except Exception as e:
                logger.warning(f"Error processing {py_file}: {e}")
                errors += 1
        
        scan_time = time.time() - start_time
        stats = self.ledger.get_statistics()
        
        result = {
            'session_id': self.session_id,
            'scan_time': scan_time,
            'files_processed': processed,
            'errors': errors,
            'ledger_stats': stats,
            'amos_brain_active': self.amos_brain is not None
        }
        
        logger.info(f"📚 Initial ledger built: {processed} files in {scan_time:.2f}s")
        return result
    
    def incremental_scan(self, since: Optional[float] = None) -> Dict[str, Any]:
        """Perform incremental scan"""
        logger.info("🔄 Performing incremental scan...")
        start_time = time.time()
        
        changed_files = self.ledger.get_changed_files(since)
        processed = 0
        
        for rel_path in changed_files:
            file_path = self.repo_root / rel_path
            if file_path.exists():
                try:
                    entry = self.ledger.update_ledger_entry(file_path, force=True)
                    if entry:
                        processed += 1
                except Exception as e:
                    logger.warning(f"Error processing {rel_path}: {e}")
        
        scan_time = time.time() - start_time
        
        result = {
            'session_id': self.session_id,
            'scan_time': scan_time,
            'changed_files': len(changed_files),
            'files_processed': processed,
            'incremental': True
        }
        
        logger.info(f"🔄 Incremental scan complete: {processed} files in {scan_time:.2f}s")
        return result
    
    def start_watcher(self):
        """Start file watcher"""
        self.watcher.start()
        logger.info("👁️ File watcher started")
    
    def stop_watcher(self):
        """Stop file watcher"""
        self.watcher.stop()
        logger.info("👁️ File watcher stopped")
    
    def get_system_status(self) -> Dict[str, Any]:
        """Get comprehensive system status"""
        stats = self.ledger.get_statistics()
        
        return {
            'session_id': self.session_id,
            'ledger_stats': stats,
            'watcher_running': self.watcher.running,
            'amos_brain_active': self.amos_brain is not None,
            'risk_score': self.risk_score,
            'freeze_zone_active': self.freeze_zone_active,
            'evidence_integrity': 1.0 - self.risk_score
        }

def main():
    """Main entrypoint"""
    if len(sys.argv) < 2:
        print("Usage: python amos_brain_governor_enhanced.py <repo_root> [command]")
        print("Commands: build-ledger, incremental-scan, start-watcher, status")
        sys.exit(1)
    
    repo_root = sys.argv[1]
    command = sys.argv[2] if len(sys.argv) > 2 else "status"
    
    governor = AMOSBrainGovernorEnhanced(repo_root)
    
    if command == "build-ledger":
        result = governor.build_initial_ledger()
        print(f"LEDGER_BUILT: {result['files_processed']} files, {result['scan_time']:.2f}s")
    
    elif command == "incremental-scan":
        result = governor.incremental_scan()
        print(f"INCREMENTAL_SCAN: {result['files_processed']} files, {result['scan_time']:.2f}s")
    
    elif command == "start-watcher":
        governor.start_watcher()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            governor.stop_watcher()
            print("WATCHER_STOPPED")
    
    elif command == "status":
        status = governor.get_system_status()
        print(f"STATUS: {json.dumps(status, indent=2)}")
    
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()


```

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
