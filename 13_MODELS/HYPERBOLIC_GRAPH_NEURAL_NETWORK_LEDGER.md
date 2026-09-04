---
title: Hyperbolic Graph Neural Network Poincaré Manifold Ledger
type: cryptographic_ledger
source: 13_MODELS
plane: 13_MODELS
domain: geometric-deep-learning
status: CANONICAL
conclusion_class: CANONICAL
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
version: 2.1.0
created: '2026-09-04'
updated: '2026-09-04'
cryptographic_hash: 920999353183ae404825d22896b17c6dc5013110e9b31b75832ee777a212fb3e
tags:
  - cryptographic-ledger
  - sota-engine
  - rscf/claim
  - rscf/state/canonical
  - hyperbolic-geometry
  - poincare-ball
  - gnn
  - manifold-embeddings
  - hierarchy
aliases:
  - Hyperbolic Graph Neural Network Poincaré Manifold Ledger
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: authoritative_AMOS_OS_structure
  scope: active__AMOS_OS
---

# Hyperbolic Graph Neural Network Poincaré Manifold Ledger

## ĐẶC TẢ HÌNH THỨC SOTA ENGINE & SỔ CÁI MÃ HÓA

### Riemannian geometric learning on Poincaré ball manifolds for low-distortion taxonomic embedding and hierarchical reasoning.

> **Origin Architect & Steward:** Trang Phan & AMOS OS Core Team  
> **Plane:** `13_MODELS`  
> **Script thực thi:** `scripts/run_hyperbolic_graph_neural_network.py`  
> **Mã băm SHA-256:** `920999353183ae404825d22896b17c6dc5013110e9b31b75832ee777a212fb3e`  
> **Trạng thái:** `CANONICAL` (Đã kiểm chứng thực thi độc lập)

---

## 1. NGUYÊN LÝ & MÔ HÌNH HÌNH THỨC

Động cơ này thiết lập giải pháp chuyên sâu thuộc biên giới nghiên cứu hiện đại, giải quyết rào cản tính toán trong phân lớp `13_MODELS`.

```
+-------------------------------------------------------------------------------+
|                       SOTA PIPELINE & PROTOCOL OVERVIEW                       |
|  [ Input Telemetry / Problem Instance ]                                      |
|           |                                                                   |
|           v                                                                   |
|  [ Mathematical Transformation / Quantum or Neuromorphic Mapping ]            |
|           |                                                                   |
|           v                                                                   |
|  [ Invariant Evaluation & Verified Execution Output ]                         |
+-------------------------------------------------------------------------------+
```

---

## 2. MÃ NGUỒN KIỂM CHỨNG THỰC THI

```python
import numpy as np

def poincare_mobius_add(u: np.ndarray, v: np.ndarray, c: float = 1.0) -> np.ndarray:
    """Möbius addition in the Poincaré ball manifold with curvature c."""
    u2 = np.sum(u**2, axis=-1, keepdims=True)
    v2 = np.sum(v**2, axis=-1, keepdims=True)
    uv = np.sum(u * v, axis=-1, keepdims=True)
    
    num = (1 + 2 * c * uv + c * v2) * u + (1 - c * u2) * v
    denom = 1 + 2 * c * uv + c**2 * u2 * v2 + 1e-15
    res = num / denom
    
    # Project within boundary
    norm = np.linalg.norm(res, axis=-1, keepdims=True)
    max_norm = (1.0 - 1e-5) / np.sqrt(c)
    cond = norm > max_norm
    res = np.where(cond, res * (max_norm / (norm + 1e-15)), res)
    return res

def poincare_distance(u: np.ndarray, v: np.ndarray, c: float = 1.0) -> float:
    """Geodesic distance in the Poincaré ball."""
    diff = poincare_mobius_add(-u, v, c)
    norm = np.linalg.norm(diff, axis=-1)
    sqrt_c = np.sqrt(c)
    dist = (2.0 / sqrt_c) * np.arctanh(np.clip(sqrt_c * norm, 0, 1.0 - 1e-6))
    return float(dist)

if __name__ == "__main__":
    u = np.array([0.2, 0.3])
    v = np.array([-0.4, 0.5])
    d = poincare_distance(u, v, c=1.0)
    assert d > 0.0
    w = np.array([0.1, -0.2])
    d_uw = poincare_distance(u, w)
    d_wv = poincare_distance(w, v)
    assert d <= d_uw + d_wv + 1e-7
    print(f"Poincaré Hyperbolic Distance d(u,v) = {d:.4f} (PASS)")
```

---

## 3. LIÊN HỆ ĐIỀU HÀNH & ĐIỀU PHỐI

- **MOC Gốc:** [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
- **MOC Phân lớp:** [[13_MODELS/13_MODELS_MOC|13_MODELS_MOC]]
- **Kiểm toán Hệ thống:** [[20_OPERATIONS/AMOS_OS_AUDIT_2026-09-03|AMOS_OS_AUDIT]]
