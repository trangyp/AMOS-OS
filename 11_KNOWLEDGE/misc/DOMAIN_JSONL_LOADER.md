---
title: DOMAIN JSONL LOADER
tags: [misc, reference, general, canon/knowledge]
type: note
source: 11_KNOWLEDGE/misc
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---


# DOMAIN JSONL LOADER

"""
Domain JSONL Loader — Load and Query 500,000 Entry Domain-Specific Datasets

This module provides functions to load and work with the 500,000 entry
domain-specific JSONL files in the ai_non_overlap directory.

Domains:
    - AI Entropy
    - Ancient Math
    - Coding Programming
    - Cognition AI
    - Design Visual
    - Electromagnetic
    - Energy
    - Forex Fractal Equations
    - Fractal Architecture
    - Human Biology
    - Information
    - Language
    - Learning Memory
    - Light
    - Money
    - Quantum
    - Time
    - TLGE (Time Light Gravity Electromagnetic)
"""

import json
import numpy as np
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from pathlib import Path
import gzip


@dataclass
class DomainEntry:
    """Single domain entry from JSONL"""
    id: str
    domain: str
    data: Dict[str, Any]
    
    @classmethod
    def from_dict(cls, data: Dict, domain: str) -> 'DomainEntry':
        return cls(
            id=data.get('id', ''),
            domain=domain,
            data=data
        )


class DomainJSONLLoader:
    """
    Load and query domain-specific 500,000 entry JSONL datasets.
    
    Supports lazy loading for large files to avoid memory issues.
    """
    
    def __init__(self, data_dir: Optional[str] = None):
        """
        Initialize loader.
        
        Args:
            data_dir: Path to ai_non_overlap directory
        """
        if data_dir is None:
            data_dir = Path(__file__).parent
        else:
            data_dir = Path(data_dir)
        
        self.data_dir = data_dir
        self.loaded_domains: Dict[str, List[Dict]] = {}
        self.domain_files = {
            'ai_entropy': 'ai_entropy_500000.jsonl',
            'ancient_math': 'ancient_math_500000.jsonl',
            'coding_programming': 'coding_programming_500000.jsonl',
            'cognition_ai': 'cognition_ai_500000.jsonl',
            'design_visual': 'design_visual_500000.jsonl',
            'deterministic_logic': 'deterministic_logic_500000.jsonl',
            'dna_gene': 'dna_gene_500000.jsonl',
            'electromagnetic': 'electromagnetic_500000.jsonl',
            'energy': 'energy_500000.jsonl',
            'forex_fractal': 'forex_fractal_equations_500000.jsonl',
            'fractal_architecture': 'fractal_architecture_500000.jsonl',
            'gravity': 'hierarchical_ai_architecture_generator/gravity_500000.jsonl',
            'information': 'information_500000.jsonl',
            'language': 'language_500000.jsonl',
            'learning_memory': 'learning_memory_500000.jsonl',
            'light': 'light_500000.jsonl',
            'money': 'money_500000.jsonl',
            'nuclear_proton_micro': 'nuclear_proton_micro_500000.jsonl',
            'prediction': 'prediction_500000.jsonl',
            'prediction_v2': 'prediction_500000_v2_no_overlap.jsonl',
            'prediction_v3': 'prediction_500000_v3_no_overlap.jsonl',
            'prediction_v4': 'prediction_500000_v4_no_overlap.jsonl',
            'prediction_v5': 'prediction_500000_v5.jsonl',
            'prediction_v6': 'prediction_500000_v6_no_overlap.jsonl',
            'prediction_v7': 'prediction_500000_v7_no_overlap.jsonl',
            'prediction_v8': 'prediction_500000_v8_no_overlap.jsonl',
            'prediction_v9': 'prediction_500000_v9_no_overlap.jsonl',
            'prediction_v10': 'prediction_500000_v10_no_overlap.jsonl',
            'prediction_v11': 'prediction_500000_v11_no_overlap.jsonl',
            'prediction_v12': 'prediction_500000_v12_no_overlap.jsonl',
            'prediction_v13': 'prediction_500000_v13_no_overlap.jsonl',
            'prediction_v14': 'prediction_500000_v14_no_overlap.jsonl',
            'prediction_v15': 'prediction_500000_v15_no_overlap.jsonl',
            'prediction_v16': 'prediction_500000_v16_no_overlap.jsonl',
            'prediction_v17': 'prediction_500000_v17_no_overlap.jsonl',
            'prediction_v18': 'prediction_500000_v18_no_overlap.jsonl',
            'prediction_v19': 'prediction_500000_v19_no_overlap.jsonl',
            'prediction_v20': 'prediction_500000_v20_no_overlap.jsonl',
            'chemistry_v2': 'chemistry_500000_v2.jsonl',
            'deterministic_logic_v2':
                'fractal_cognitive_architecture_v2/deterministic_logic_500000_v2.jsonl',
            'language_fractal_states':
                'language_fractal_architecture_500000/language_fractal_states_500000.jsonl',
            'quantum': 'quantum_500000.jsonl',
            'time': 'time_500000.jsonl',
            'tlge': 'tlge_500000.jsonl',
            'ui_ux': 'ui_ux_500000.jsonl',
        }
    
    def load_domain(self, domain: str, limit: Optional[int] = None) -> List[Dict]:
        """
        Load entries from a specific domain JSONL file.
        
        Args:
            domain: Domain name (e.g., 'ai_entropy', 'quantum')
            limit: Maximum number of entries to load (None = all)
        
        Returns:
            List of entry dictionaries
        """
        if domain not in self.domain_files:
            raise ValueError(f"Unknown domain: {domain}")
        
        file_path = self.data_dir / self.domain_files[domain]
        
        if not file_path.exists():
            print(f"[WARNING] Domain file not found: {file_path}")
            return []
        
        entries = []
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for i, line in enumerate(f):
                    if limit and i >= limit:
                        break
                    try:
                        entry = json.loads(line.strip())
                        entries.append(entry)
                    except json.JSONDecodeError:
                        continue
        except Exception as e:
            print(f"[ERROR] Failed to load {domain}: {e}")
            return []
        
        self.loaded_domains[domain] = entries
        return entries
    
    def get_domain_sample(self, domain: str, n: int = 10) -> List[Dict]:
        """
        Get a sample of entries from a domain (lazy loading).
        
        Args:
            domain: Domain name
            n: Number of samples to return
        
        Returns:
            List of entry dictionaries
        """
        if domain not in self.loaded_domains:
            self.load_domain(domain, limit=n * 2)  # Load a bit more for filtering
        
        return self.loaded_domains.get(domain, [])[:n]
    
    def search_domain(self, domain: str, query: str, field: str = 'formula') -> List[Dict]:
        """
        Search for entries in a domain.
        
        Args:
            domain: Domain name
            query: Search string
            field: Field to search in
        
        Returns:
            List of matching entries
        """
        if domain not in self.loaded_domains:
            self.load_domain(domain, limit=1000)  # Load subset for search
        
        query_lower = query.lower()
        results = []
        
        for entry in self.loaded_domains.get(domain, []):
            value = str(entry.get(field, ''))
            if query_lower in value.lower():
                results.append(entry)
        
        return results
    
    def get_domain_stats(self, domain: str) -> Dict[str, Any]:
        """
        Get statistics for a domain.
        
        Args:
            domain: Domain name
        
        Returns:
            Dictionary with statistics
        """
        if domain not in self.loaded_domains:
            self.load_domain(domain, limit=1000)  # Load subset for stats
        
        entries = self.loaded_domains.get(domain, [])
        
        return {
            'domain': domain,
            'loaded_entries': len(entries),
            'file': self.domain_files.get(domain, ''),
            'sample_fields': list(entries[0].keys()) if entries else []
        }
    
    def get_all_domains(self) -> List[str]:
        """Get list of available domains."""
        return list(self.domain_files.keys())
    
    def get_status(self) -> Dict[str, Any]:
        """Get loader status."""
        return {
            'data_dir': str(self.data_dir),
            'available_domains': len(self.domain_files),
            'loaded_domains': len(self.loaded_domains),
            'domains': list(self.domain_files.keys())
        }


def create_domain_jsonl_loader(data_dir: Optional[str] = None) -> DomainJSONLLoader:
    """Factory function to create a DomainJSONLLoader instance."""
    return DomainJSONLLoader(data_dir=data_dir)


if __name__ == "__main__":
    loader = create_domain_jsonl_loader()
    print("Domain JSONL Loader Status:")
    print(json.dumps(loader.get_status(), indent=2))
    
    # Test loading a domain
    print("\nTesting quantum domain sample:")
    quantum_sample = loader.get_domain_sample('quantum', n=3)
    print(f"Loaded {len(quantum_sample)} entries")
    if quantum_sample:
        print(f"Sample entry keys: {quantum_sample[0].keys()}")

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]