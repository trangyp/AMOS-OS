---
title: CONFIGURATION LOADER
tags: [misc, reference, general]
type: note
source: 11_KNOWLEDGE/misc
---


# CONFIGURATION LOADER

"""
Configuration Loader — Load TOML configuration files

This module provides functions to load and work with TOML configuration files.
"""

import tomli
from typing import Dict, Optional, Any
from pathlib import Path


class ConfigurationLoader:
    """
    Load TOML configuration files.
    """
    
    def __init__(self, data_dir: Optional[str] = None):
        """Initialize loader."""
        if data_dir is None:
            data_dir = Path(__file__).parent
        else:
            data_dir = Path(data_dir)
        
        self.data_dir = data_dir
        self._cache = {}
        
        # Define configuration files
        self.config_files = {
            'fractal_cognitive_architecture_v2':
                'fractal_cognitive_architecture_v2/pyproject.toml',
        }
    
    def load_config(self, key: str) -> Dict:
        """Load TOML configuration file."""
        if key in self._cache:
            return self._cache[key]
        
        if key not in self.config_files:
            raise ValueError(f"Unknown configuration file: {key}")
        
        filepath = self.data_dir / self.config_files[key]
        
        if not filepath.exists():
            print(f"[WARNING] Configuration file not found: {filepath}")
            return {}
        
        try:
            with open(filepath, 'rb') as f:
                data = tomli.load(f)
            self._cache[key] = data
            return data
        except Exception as e:
            print(f"[ERROR] Failed to load configuration file {filepath}: {e}")
            return {}
    
    def get_available_files(self) -> list:
        """Get list of available configuration files."""
        return list(self.config_files.keys())
    
    def get_status(self) -> Dict[str, Any]:
        """Get loader status."""
        return {
            'data_dir': str(self.data_dir),
            'available_files': len(self.config_files),
            'cached_files': len(self._cache),
            'files': list(self.config_files.keys())
        }


def create_configuration_loader(data_dir: Optional[str] = None) -> ConfigurationLoader:
    """Factory function to create configuration loader."""
    return ConfigurationLoader(data_dir)

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]