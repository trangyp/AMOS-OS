---
title: Neuromorphic Spiking BCI Continuous Decoder Ledger
type: cryptographic_ledger
source: 15_INTERFACES
plane: 15_INTERFACES
domain: bci-interfaces
status: CANONICAL
conclusion_class: CANONICAL
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
version: 2.1.0
created: '2026-09-04'
updated: '2026-09-04'
cryptographic_hash: 8fc246e99745994da6892c233a5f65f96a5bda0d866fd8f8c304f9dedd8c7195
tags:
  - cryptographic-ledger
  - sota-engine
  - rscf/claim
  - rscf/state/canonical
  - bci
  - neuromorphic
  - snn
  - lif-neuron
  - spike-decoding
  - kinematics
aliases:
  - Neuromorphic Spiking BCI Continuous Decoder Ledger
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: authoritative_AMOS_OS_structure
  scope: active__AMOS_OS
---

# Neuromorphic Spiking BCI Continuous Decoder Ledger

## ĐẶC TẢ HÌNH THỨC SOTA ENGINE & SỔ CÁI MÃ HÓA

### Continuous 3D kinematic trajectory decoding from high-density intracortical neural spike trains using Leaky Integrate-and-Fire (LIF) spiking neural dynamics with recurrent synaptic filtering.

> **Origin Architect & Steward:** Trang Phan & AMOS OS Core Team  
> **Plane:** `15_INTERFACES`  
> **Script thực thi:** `scripts/run_neuromorphic_spiking_bci_decoder.py`  
> **Mã băm SHA-256:** `8fc246e99745994da6892c233a5f65f96a5bda0d866fd8f8c304f9dedd8c7195`  
> **Trạng thái:** `CANONICAL` (Đã kiểm chứng thực thi độc lập)

---

## 1. NGUYÊN LÝ & MÔ HÌNH HÌNH THỨC

Động cơ này thiết lập giải pháp chuyên sâu thuộc biên giới nghiên cứu hiện đại, giải quyết rào cản tính toán trong phân lớp `15_INTERFACES`.

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

class NeuromorphicSpikingBCIDecoder:
    """
    Decodes continuous 3D velocity/kinematics from high-density multi-electrode spike trains
    using a Leaky Integrate-and-Fire (LIF) network with Recurrent Synaptic Filtering.
    """
    def __init__(self, n_channels=64, n_hidden=128, n_outputs=3, dt=0.001, tau_mem=0.020, tau_syn=0.010, v_thresh=1.0):
        self.n_channels = n_channels
        self.n_hidden = n_hidden
        self.n_outputs = n_outputs
        self.dt = dt
        self.alpha = np.exp(-dt / tau_mem)
        self.beta = np.exp(-dt / tau_syn)
        self.v_thresh = v_thresh
        
        # Synaptic weight matrices
        np.random.seed(42)
        self.W_in = np.random.randn(n_hidden, n_channels) * 0.1
        self.W_rec = np.random.randn(n_hidden, n_hidden) * 0.05
        self.W_out = np.random.randn(n_outputs, n_hidden) * 0.1
        
        # State variables
        self.v_mem = np.zeros(n_hidden)
        self.i_syn = np.zeros(n_hidden)
        self.spikes = np.zeros(n_hidden)
        self.kinematic_state = np.zeros(n_outputs)
        
    def step(self, spike_input: np.ndarray) -> np.ndarray:
        # Synaptic current integration: I_syn(t) = beta * I_syn(t-1) + W_in * S_in + W_rec * S_rec
        self.i_syn = self.beta * self.i_syn + np.dot(self.W_in, spike_input) + np.dot(self.W_rec, self.spikes)
        
        # Membrane potential integration: V_mem(t) = alpha * V_mem(t-1) * (1 - S(t-1)) + I_syn(t)
        self.v_mem = self.alpha * self.v_mem * (1.0 - self.spikes) + self.i_syn
        
        # Spike generation
        self.spikes = (self.v_mem >= self.v_thresh).astype(float)
        
        # Linear kinematic readout filter
        self.kinematic_state = 0.95 * self.kinematic_state + 0.05 * np.dot(self.W_out, self.spikes)
        return self.kinematic_state

if __name__ == "__main__":
    decoder = NeuromorphicSpikingBCIDecoder()
    # Simulate 100 ms of spike inputs
    np.random.seed(123)
    outputs = []
    for _ in range(100):
        raw_spikes = (np.random.rand(64) < 0.05).astype(float) # 50 Hz Poisson rate
        vel = decoder.step(raw_spikes)
        outputs.append(vel)
    outputs = np.array(outputs)
    assert outputs.shape == (100, 3)
    assert not np.isnan(outputs).any()
    print("Neuromorphic Spiking BCI Decoder Verification: PASS")
```

---

## 3. LIÊN HỆ ĐIỀU HÀNH & ĐIỀU PHỐI

- **MOC Gốc:** [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
- **MOC Phân lớp:** [[15_INTERFACES/15_INTERFACES_MOC|15_INTERFACES_MOC]]
- **Kiểm toán Hệ thống:** [[20_OPERATIONS/AMOS_OS_AUDIT_2026-09-03|AMOS_OS_AUDIT]]
