---
title: FRACTAL LOADER
tags:
- fractal
- math
- self-similarity
- canon/knowledge
type: document
source: 11_KNOWLEDGE/fractal
rscf:
  state: AMOS_MODEL
  claim_class: AMOS_MODEL
  provenance: AMOS_corpus
  scope: fractal_system
---
# FRACTAL LOADER

"""
Fractal Data Loader — Load and Query Fractal Architecture JSON

This module provides functions to load and work with the 25,000 entry
fractal architecture JSON files in the _math directory.
"""

import json
import numpy as np
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from pathlib import Path


@dataclass
class FractalEntry:
    """Single fractal family entry"""
    id: str
    name: str
    formula: str
    class_type: str
    strictness: str
    parameters: Optional[Dict] = None
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'FractalEntry':
        return cls(
            id=data.get('id', ''),
            name=data.get('name', ''),
            formula=data.get('formula', ''),
            class_type=data.get('class', ''),
            strictness=data.get('strictness', ''),
            parameters=data.get('parameters')
        )


class FractalArchitectureLoader:
    """
    Load and query the 25,000 entry fractal architecture database.
    
    Files:
        - math_fractal_architecture_25000.json: Core math architecture
        - all_domain_fractal_architecture_master_25000.json: All domains
        - x25000_hierarchical_fractal.json: Hierarchical structure
        - x25000_strict_fractal_equations_only.json: Strict equations only
    """
    
    def __init__(self, data_dir: Optional[str] = None):
        """
        Initialize loader.
        
        Args:
            data_dir: Directory containing JSON files (default: same as this file)
        """
        if data_dir is None:
            data_dir = Path(__file__).parent
        else:
            data_dir = Path(data_dir)
        
        self.data_dir = data_dir
        self._cache = {}
        
    def _load_json(self, filename: str) -> Dict:
        """Load and cache JSON file"""
        if filename in self._cache:
            return self._cache[filename]
        
        filepath = self.data_dir / filename
        if not filepath.exists():
            raise FileNotFoundError(f"Fractal data file not found: {filepath}")
        
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        self._cache[filename] = data
        return data
    
    def load_math_architecture(self) -> Dict:
        """Load the core math fractal architecture"""
        return self._load_json('math_fractal_architecture_25000.json')
    
    def load_all_domain_architecture(self) -> Dict:
        """Load the all-domain fractal architecture"""
        return self._load_json('all_domain_fractal_architecture_master_25000.json')
    
    def load_hierarchical_fractal(self) -> Dict:
        """Load the hierarchical fractal structure"""
        return self._load_json('x25000_hierarchical_fractal.json')
    
    def load_strict_equations(self) -> Dict:
        """Load the strict fractal equations only"""
        return self._load_json('x25000_strict_fractal_equations_only.json')
    
    def get_canonical_families(self, file: str = 'math') -> List[FractalEntry]:
        """
        Get canonical fractal families.
        
        Args:
            file: Which file to load ('math', 'all_domain', 'hierarchical', 'strict')
            
        Returns:
            List of FractalEntry objects
        """
        file_map = {
            'math': 'math_fractal_architecture_25000.json',
            'all_domain': 'all_domain_fractal_architecture_master_25000.json',
            'hierarchical': 'x25000_hierarchical_fractal.json',
            'strict': 'x25000_strict_fractal_equations_only.json'
        }
        
        data = self._load_json(file_map.get(file, file_map['math']))
        
        entries = data.get('entries', [])
        # Also support 'canonical_families' for other file formats
        if not entries and 'canonical_families' in data:
            entries = data.get('canonical_families', [])
        return [FractalEntry.from_dict(f) for f in entries]
    
    def search_by_class(self, class_type: str) -> List[FractalEntry]:
        """Search fractals by class type"""
        all_entries = self.get_canonical_families('all_domain')
        return [e for e in all_entries if e.class_type == class_type]
    
    def search_by_name(self, name: str) -> List[FractalEntry]:
        """Search fractals by name (partial match)"""
        all_entries = self.get_canonical_families('all_domain')
        return [e for e in all_entries if name.lower() in e.name.lower()]
    
    def get_strict_fractals(self) -> List[FractalEntry]:
        """Get only strict fractals (not fractal-like)"""
        all_entries = self.get_canonical_families('all_domain')
        return [e for e in all_entries if e.strictness == 'strict_fractal']
    
    def get_statistics(self) -> Dict:
        """Get statistics about the fractal database"""
        try:
            data = self._load_json('all_domain_fractal_architecture_master_25000.json')
            metadata = data.get('metadata', {})
            total_entries = metadata.get('entry_count', 0)
            
            # Get entries for detailed stats
            all_entries = self.get_canonical_families('all_domain')
            
            return {
                'total_entries': total_entries or len(all_entries),
                'loaded_entries': len(all_entries),
                'domain_count': metadata.get('domain_count', 0),
                'metadata': metadata,
            }
        except Exception as e:
            return {'error': str(e), 'total_entries': 0}


def get_fractal_by_formula(formula_query: str) -> Optional[FractalEntry]:
    """
    Quick search for a fractal by formula.
    
    Args:
        formula_query: Formula to search for (e.g., "z^2+c")
        
    Returns:
        Matching FractalEntry or None
    """
    loader = FractalArchitectureLoader()
    all_entries = loader.get_canonical_families('all_domain')
    
    for entry in all_entries:
        if formula_query.lower() in entry.formula.lower():
            return entry
    
    return None


def list_fractal_classes() -> List[str]:
    """List all available fractal class types"""
    loader = FractalArchitectureLoader()
    stats = loader.get_statistics()
    return list(stats['class_distribution'].keys())


def create_fractal_from_entry(entry: FractalEntry, 
                               width: int = 512, 
                               height: int = 512,
                               max_iter: int = 100) -> np.ndarray:
    """
    Generate fractal image from entry specification.
    
    Args:
        entry: FractalEntry with formula
        width: Image width
        height: Image height
        max_iter: Maximum iterations
        
    Returns:
        2D numpy array with fractal values
    """
    # Simple fractal generators based on class
    
    if entry.class_type == 'complex_iteration':
        # Mandelbrot or Julia
        if 'c fixed' in entry.formula or entry.name == 'Julia':
            return _generate_julia(width, height, max_iter)
        else:
            return _generate_mandelbrot(width, height, max_iter)
    
    elif entry.class_type == 'dimension_measure':
        # Return a simple pattern
        return _generate_noise_pattern(width, height)
    
    elif entry.class_type == 'subtractive':
        # Cantor-like
        return _generate_cantor_dust(width, height, max_iter)
    
    else:
        # Default to noise pattern
        return _generate_noise_pattern(width, height)


def _generate_mandelbrot(width: int, height: int, max_iter: int) -> np.ndarray:
    """Generate Mandelbrot set"""
    x_min, x_max = -2.5, 1.5
    y_min, y_max = -2.0, 2.0
    
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    
    C = X + 1j * Y
    Z = np.zeros_like(C)
    M = np.zeros(C.shape, dtype=int)
    
    for i in range(max_iter):
        mask = np.abs(Z) <= 2
        Z[mask] = Z[mask]**2 + C[mask]
        M[~mask & (M == 0)] = i
    
    M[M == 0] = max_iter
    return M


def _generate_julia(width: int, height: int, max_iter: int, 
                   c: complex = -0.7 + 0.27015j) -> np.ndarray:
    """Generate Julia set"""
    x_min, x_max = -2.0, 2.0
    y_min, y_max = -2.0, 2.0
    
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    
    Z = X + 1j * Y
    M = np.zeros(Z.shape, dtype=int)
    
    for i in range(max_iter):
        mask = np.abs(Z) <= 2
        Z[mask] = Z[mask]**2 + c
        M[~mask & (M == 0)] = i
    
    M[M == 0] = max_iter
    return M


def _generate_cantor_dust(width: int, height: int, iterations: int) -> np.ndarray:
    """Generate Cantor dust pattern"""
    # Start with filled square
    img = np.ones((height, width))
    
    # Iteratively remove middle thirds
    for _ in range(min(iterations, 5)):
        h, w = img.shape
        # Remove middle third in both dimensions
        img[h//3:2*h//3, :] = 0
        img[:, w//3:2*w//3] = 0
    
    return img


def _generate_noise_pattern(width: int, height: int) -> np.ndarray:
    """Generate fractal-like noise pattern"""
    # Simple fractional Brownian motion approximation
    noise = np.random.randn(height, width)
    
    # Apply power law filtering in frequency domain
    fft_noise = np.fft.fft2(noise)
    
    # Create frequency grid
    freq_x = np.fft.fftfreq(width)
    freq_y = np.fft.fftfreq(height)
    FX, FY = np.meshgrid(freq_x, freq_y)
    
    # Frequency magnitude
    freq_mag = np.sqrt(FX**2 + FY**2)
    freq_mag[0, 0] = 1e-10  # Avoid division by zero
    
    # 1/f filtering (pink noise)
    pink_filter = 1.0 / np.sqrt(freq_mag)
    fft_noise *= pink_filter
    
    result = np.real(np.fft.ifft2(fft_noise))
    return (result - result.min()) / (result.max() - result.min())


# Convenience exports
__all__ = [
    'FractalEntry',
    'FractalArchitectureLoader',
    'get_fractal_by_formula',
    'list_fractal_classes',
    'create_fractal_from_entry',
]

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[FRACTAL_MOC]]
