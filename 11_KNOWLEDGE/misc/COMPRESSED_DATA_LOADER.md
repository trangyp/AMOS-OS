---
title: COMPRESSED DATA LOADER
tags: [misc]
type: note
source: 11_KNOWLEDGE/misc
---


"""
Compressed Data Loader — Load .gz compressed JSON files

This module provides functions to load and work with compressed JSON datasets.
"""

import json
import gzip
from typing import Dict, Optional, Any
from pathlib import Path


class CompressedDataLoader:
    """
    Load compressed (.gz) JSON datasets.
    """
    
    def __init__(self, data_dir: Optional[str] = None):
        """Initialize loader."""
        if data_dir is None:
            data_dir = Path(__file__).parent
        else:
            data_dir = Path(data_dir)
        
        self.data_dir = data_dir
        self._cache = {}
        
        # Define compressed files
        self.compressed_files = {
            'ai_equation_architecture_25000_gz':
                'hierarchical_ai_architecture_generator/ai_equation_architecture_25000.json.gz',
        }
    
    def load_compressed(self, key: str) -> Dict:
        """Load compressed JSON file."""
        if key in self._cache:
            return self._cache[key]
        
        if key not in self.compressed_files:
            raise ValueError(f"Unknown compressed file: {key}")
        
        filepath = self.data_dir / self.compressed_files[key]
        
        if not filepath.exists():
            print(f"[WARNING] Compressed file not found: {filepath}")
            return {}
        
        try:
            with gzip.open(filepath, 'rt', encoding='utf-8') as f:
                data = json.load(f)
            self._cache[key] = data
            return data
        except Exception as e:
            print(f"[ERROR] Failed to load compressed file {filepath}: {e}")
            return {}
    
    def get_available_files(self) -> list:
        """Get list of available compressed files."""
        return list(self.compressed_files.keys())
    
    def get_status(self) -> Dict[str, Any]:
        """Get loader status."""
        return {
            'data_dir': str(self.data_dir),
            'available_files': len(self.compressed_files),
            'cached_files': len(self._cache),
            'files': list(self.compressed_files.keys())
        }


def create_compressed_data_loader(data_dir: Optional[str] = None) -> CompressedDataLoader:
    """Factory function to create compressed data loader."""
    return CompressedDataLoader(data_dir)

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]
