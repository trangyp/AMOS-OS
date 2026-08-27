---
title: "Vault Domain Knowledge — Amos Strict Fractal Equation Rscf Registry"
type: reference
source: 07_SKILLS/amos-strict-fractal-equation-rscf-registry/references
tags: [reference, amos-strict-fractal-equation-rscf-registry, canon/skill]
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---


# Vault-Sourced Domain Knowledge

> Source: AMOS_OS Obsidian vault (`_00_Cosmo brain/`)
> Epistemic class: SOURCE_CLAIM
> Extracted from skill: `amos-strict-fractal-equation-rscf-registry`

## Vault-Sourced Content

### Source 1: fractal_loader

> Path: `fractal/fractal_loader.md` | Size: 10176 chars | Match score: 15

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
    
    def get_canonical_families(self, file: str = '

---

### Source 2: X25000_STRICT_FRACTAL_EQUATIONS_ONLY

> Path: `_reference/FRACTAL/X25000_STRICT_FRACTAL_EQUATIONS_ONLY.md` | Size: 23558210 chars | Match score: 13

{"metadata":{"title":"x25000 Strict Fractal Equations Only","created_utc":"2026-05-05T09:50:14.651246+00:00","entry_count":25000,"base_family_count":30,"core":"strict fractal entry = accepted fractal-generating family + formal parameters + validation condition","limit":"This is not 25,000 fundamentally unique equations; it is 25,000 strict-family parameterized/formal equation entries."},"strict_base_families":[{"id":"SFR001","name":"Mandelbrot power family","formula":"z_{n+1}=z_n^p+c","family":"complex_escape_time","strictness":"strict"},{"id":"SFR002","name":"Julia power family","formula":"z_{n+1}=z_n^p+c, c fixed","family":"complex_escape_time","strictness":"strict"},{"id":"SFR003","name":"Multibrot","formula":"z_{n+1}=z_n^d+c","family":"complex_escape_time","strictness":"strict"},{"id":"SFR004","name":"Burning Ship generalized","formula":"z_{n+1}=(|Re(z_n)|+i|Im(z_n)|)^p+c","family":"complex_escape_time","strictness":"strict"},{"id":"SFR005","name":"Tricorn generalized","formula":"z_{n+1}=conj(z_n)^p+c","family":"anti_holomorphic","strictness":"strict"},{"id":"SFR006","name":"Phoenix family","formula":"z_{n+1}=z_n^p+c+qz_{n-1}","family":"memory_complex_iteration","strictness":"strict"},{"id":"SFR007","name":"Newton fractal","formula":"z_{n+1}=z_n-f(z_n)/f'(z_n)","family":"root_basin","strictness":"strict"},{"id":"SFR008","name":"Halley fractal","formula":"z_{n+1}=z_n-2f f'/(2(f')^2-f f'')","family":"root_basin","strictness":"strict"},{"id":"SFR009","name":"Rational map","formula":"z_{n+1}=P(z_n)/Q(z_n)","family":"complex_dynamics","strictness":"strict"},{"id":"SFR010","name":"IFS attractor","formula":"A=∪_{i=1}^m w_i(A), |w_i|<1","family":"IFS","strictness":"strict"},{"id":"SFR011","name":"Affine IFS","formula":"w_i(x)=A_i x+b_i, ||A_i||<1","family":"IFS","strictness":"strict"},{"id":"SFR012","name":"Cantor generalized","formula":"C_{n+1}=keep m scaled intervals of ratio r","family":"subtractive_self_similar","strictness":"strict"},{"id":"SFR013","name":"Koch 
generalized","formula":"segment -> N segments scaled by r","family":"replacement_curve","strictness":"strict"},{"id":"SFR014","name":"Sierpinski generalized","formula":"D=log(N)/log(1/r)","family":"subdivision","strictness":"strict"},{"id":"SFR015","name":"Menger generalized","formula":"D=log(N_keep)/log(s)","family":"3d_subdivision","strictness":"strict"},{"id":"SFR016","name":"Apollonian gasket","formula":"2Σk_i²=(Σk_i)²","family":"circle_packing","strictness":"strict"},{"id":"SFR017","name":"L-system deterministic","formula":"G=(V,ω,P), apply P recursively","family":"grammar_fractal","strictness":"strict"},{"id":"SFR018","name":"Barnsley fern IFS","formula":"x_{n+1}=a_i x_n+b_i y_n+e_i; y_{n+1}=c_i x_n+d_i y_n+f_i","family":"IFS","strictness":"strict"},{"id":"SFR019","name":"Weierstrass function","formula":"W(x)=Σa^n cos(b^nπx), 0<a<1, ab>1","family":"fractal_function","strictness":"strict"},{"id":"SFR020","name":"Takagi function","formula":"T(x)=Σ2^{-n}dist(2^nx,Z)","family":"fractal_

---

### Source 3: ALL_DOMAIN_FRACTAL_ARCHITECTURE_MASTER_25000

> Path: `_reference/FRACTAL/ALL_DOMAIN_FRACTAL_ARCHITECTURE_MASTER_25000.md` | Size: 20287426 chars | Match score: 13

{"metadata":{"title":"All-Domain Fractal / Recursive / Scaling Architecture Master Map","created_utc":"2026-05-05T09:51:30.382877+00:00","entry_count":25000,"domain_count":76,"purpose":"One unified file mapping fractal, recursive, scaling, feedback, network, and control architectures across all major domains.","important_limit":"This is an all-domain architecture map, not proof that every domain is strictly fractal.","core_compression":"Everything maps as object + operator + scale + invariant + validation."},"domains":["mathematics","physics","cosmology","chemistry","materials_science","biology","genetics","neuroscience","cognition","psychology","medicine","public_health","ecology","climate","geology","hydrology","oceanography","agriculture","microbiome","human_body","AI","machine_learning","software_architecture","cybersecurity","robotics","data_systems","networks","internet","social_media","economics","finance","markets","business","operations","supply_chain","governance","law","policy","education","language","linguistics","music","sound","art","design","architecture","urbanism","transport","energy","power_grids","culture","religion","myth","ritual","history","civilization","warfare","security","ethics","philosophy","logic","symbol_systems","family_systems","relationships","organizations","teams","sports","games","media","attention_systems","pollution","noise","bots","synthetic_media","planetary_systems","space_systems"],"equation_library":[{"name":"recursive_state","formula":"S_{t+1}=C(F(S_t,U_t))"},{"name":"fractal_iteration","formula":"x_{n+1}=f(x_n)"},{"name":"scale_law","formula":"Y=kX^α"},{"name":"box_dimension","formula":"D=lim logN(ε)/log(1/ε)"},{"name":"network_fractal","formula":"N_B(l_B)∼l_B^{-d_B}"},{"name":"branching","formula":"N_l=N_0b^l; 
r_l=r_0a^l"},{"name":"multifractal","formula":"Z(q,ε)=Σμ_i(ε)^q∼ε^{τ(q)}"},{"name":"cascade","formula":"μ_{n+1}=W_iμ_n"},{"name":"attractor","formula":"X_{t+1}=F(X_t)"},{"name":"signal_noise","formula":"SNR=Signal/Noise"},{"name":"control_gate","formula":"allow=true iff Risk<θ"},{"name":"renormalization","formula":"g'=R(g)"},{"name":"substitution","formula":"T_{n+1}=σ(T_n)"},{"name":"memory_decay","formula":"M_{t+1}=ρM_t+η"},{"name":"feedback","formula":"L_{t+1}=L_t+Input-Repair"}],"architecture_modes":["recursive","hierarchical","branching","network","cascade","boundary","porous","self_affine","multifractal","rank_size","spiral","tiling","attractor","feedback","control","ecosystem","symbolic","temporal","spatial","social"],"validation_methods":["box_counting","power_law_fit","hurst_exponent","lacunarity","graph_cover","multifractal_spectrum","branch_ratio","attractor_dimension","lyapunov","scaling_collapse","source_support","schema_parse","risk_check","anti_overclaim","domain_expert_review"],"entries":[{"id":"ADF-00001","dataset":"all_domain_fractal_architecture_master","domain":"mathematics","scale":"meso","architecture_mode":"boundary","equation_name":"box_dimension","equation_formula":"D=lim

---
**MOC:** [[references_MOC]]

## Related

- [[07_SKILLS_MOC]]
