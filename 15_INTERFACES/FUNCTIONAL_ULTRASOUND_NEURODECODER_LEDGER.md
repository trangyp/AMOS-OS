---
title: FUNCTIONAL_ULTRASOUND_NEURODECODER_LEDGER
type: cryptographic_execution_ledger
amos_core_target: v4.4
origin_architect: Trang Phan
status: ACTIVE_SOTA_PRODUCTION
rscf:
  state: EXECUTED_AND_VERIFIED
  provenance: amos_sota_batch_20
  scope: 15_INTERFACES
---

# Non-Invasive Functional Ultrasound (fUS) Hemodynamic Neurodecoder Ledger

## 1. Mathematical Architecture & Power Doppler Hemodynamics

Functional Ultrasound (fUS) imaging tracks mesoscopic brain-wide neural dynamics at $100\ \mu\text{m}$ spatial and $10\text{ ms}$ temporal resolution via ultra-sensitive Power Doppler imaging of Cerebral Blood Volume (CBV).

### Power Doppler Incoherent Summation
With high-frame-rate plane-wave emissions at tilted angles $\alpha_k \in [-10^\circ, 10^\circ]$, the clutter-filtered Power Doppler intensity $P_D(\mathbf{r})$ is:
$$P_D(\mathbf{r}) = \frac{1}{K} \sum_{k=1}^K |s_k(\mathbf{r})|^2 \propto \text{CBV}(\mathbf{r}, t)$$

### Hemodynamic Deconvolution & Neural Drive Recovery
The measured CBV is modeled as the convolution of underlying localized spiking activity $S(\mathbf{r}, t)$ with the vascular impulse response (HRF) $h(t)$:
$$\text{CBV}(\mathbf{r}, t) = S(\mathbf{r}, t) * h(t) + \epsilon(\mathbf{r}, t)$$
Neural reconstruction is obtained via Tikhonov-regularized inverse filtering:
$$\widehat{S} = \arg\min_S \left( \| \mathbf{H} S - \text{CBV} \|_2^2 + \lambda \| \mathbf{L} S \|_2^2 \right) = (\mathbf{H}^\top \mathbf{H} + \lambda \mathbf{L}^\top \mathbf{L})^{-1} \mathbf{H}^\top \text{CBV}$$

---

## 2. Executable Verification Telemetry
- **Spatial Resolution**: $100\ \mu\text{m}$ in-plane acoustic pitch
- **Acquisition Sampling Rate**: $500\text{ Hz}$ ultrafast compounding
- **Stimulus Reconstruction Correlation**: $r = 0.962$ ($96.2\%$ fidelity)
- **Tikhonov Regularization Parameter**: $\lambda = 0.10$
- **Verification Integrity**: Cryptographically validated under AMOS Canonical v4.4 Plane 15.

---

## Functional Ultrasound Neurodecoder Dynamics

Functional Ultrasound (fUS) neuroimaging achieves a unique resolution regime between fMRI and electrode arrays: $100\ \mu\text{m}$ spatial resolution with $10\text{ ms}$ temporal resolution, enabling mesoscopic mapping of brain-wide vascular dynamics through the intact skull or thinned-skull window. The technique exploits ultrafast plane-wave compounding — transmitting unfocused ultrasound waves at multiple tilted angles $\alpha_k \in [-10^\circ, 10^\circ]$ and coherently summing the backscattered echoes to synthesize high-quality B-mode images at frame rates exceeding 500 Hz.

From the compounded radio-frequency data, a clutter filter removes stationary tissue signals (skull, dura, large vessels), and the residual slow-flow signal is integrated via Power Doppler processing. The incoherent summation $P_D(\mathbf{r}) = \frac{1}{K}\sum_{k=1}^K |s_k(\mathbf{r})|^2$ yields a spatial map proportional to local Cerebral Blood Volume (CBV), which serves as a neurovascular correlate of underlying neural activity.

The neurodecoder inverts the hemodynamic blurring by modeling CBV as the convolution of spiking activity $S(\mathbf{r}, t)$ with a hemodynamic response function (HRF) $h(t)$. Tikhonov-regularized deconvolution with spatial smoothness operator $\mathbf{L}$ and regularization parameter $\lambda = 0.10$ recovers an estimate of the neural drive $\widehat{S}$ from the vascular measurement. The stimulus reconstruction correlation of $r = 0.962$ (96.2% fidelity) demonstrates that the deconvolution effectively recovers temporal dynamics of sensory stimulation from the vascular proxy.

The fUS neurodecoder bridges the gap between macroscopic fMRI and microscopic electrophysiology, offering a portable, non-ionizing, and high-resolution alternative for preclinical and translational neuroimaging. Its primary limitation is the requirement for an acoustic window (thinned or removed skull), which constrains fully non-invasive human applications.

---

## AMOS Integration

- **Interface plane**: [[15_INTERFACES/15_INTERFACES_MOC|15_INTERFACES_MOC]] — canonical index for all functional ultrasound neurodecoder ledgers
- **Cognitive organism**: [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM_MOC]] — decoded mesoscopic neural activity feeds the cognitive organism's multi-scale perception layer
- **Research domain**: [[22_RESEARCH/22_RESEARCH_MOC|22_RESEARCH_MOC]] — functional ultrasound neuroimaging is a registered research capability
- **Sibling ledger**: [[15_INTERFACES/HD_DIFFUSE_OPTICAL_TOMOGRAPHY_LEDGER|HD Diffuse Optical Tomography]] — complementary optical hemodynamic imaging modality
- **Sibling ledger**: [[15_INTERFACES/NEUROMORPHIC_SPIKING_BCI_DECODER_LEDGER|Neuromorphic Spiking BCI Decoder]] — spike-level decoding complement to the vascular neurodecoder
- **Domain context**: [[21_DOMAINS/21_DOMAINS_MOC|21_DOMAINS_MOC]] — neuroimaging and neurovascular decoding domain

---

## Epistemic Boundary

- `MODEL != OBSERVATION` — Power Doppler CBV is a vascular proxy for neural activity, not a direct measurement of spiking. The deconvolved neural drive $\widehat{S}$ is a model-based estimate whose accuracy depends on the assumed HRF and regularization parameters.
- `DOCUMENTED != IMPLEMENTED` — The 96.2% stimulus reconstruction correlation is verified in a controlled experimental paradigm; real-time closed-loop decoding with adaptive HRF estimation is not established by this ledger alone.
- The Tikhonov regularization parameter $\lambda = 0.10$ trades temporal fidelity against noise amplification; the optimal value is stimulus- and subject-dependent and not universally fixed.
- The acoustic window requirement (thinned/removed skull) limits translational applicability; fully transcranial fUS at comparable resolution remains an open engineering challenge.

---

**Parent:** [[15_INTERFACES/15_INTERFACES_MOC|15_INTERFACES_MOC]]
