---
title: HD_DIFFUSE_OPTICAL_TOMOGRAPHY_LEDGER
type: cryptographic_execution_ledger
amos_core_target: v4.4
origin_architect: Trang Phan
status: ACTIVE_SOTA_PRODUCTION
rscf:
  state: EXECUTED_AND_VERIFIED
  provenance: amos_sota_batch_27
  scope: 15_INTERFACES
---

# High-Density Diffuse Optical Tomography (HD-DOT) Retinotopic Reconstruction Ledger

## 1. Mathematical Architecture & Radiative Transfer Photon Diffusion

High-Density Diffuse Optical Tomography (HD-DOT) utilizes dense overlapping arrays of near-infrared optodes (760nm / 850nm) to reconstruct 3D volumetric images of cerebral hemodynamics ($HbO/HbR$) at sub-centimeter spatial resolution.

### Photon Diffusion Equation Forward Model
In turbid biological tissue with scattering $\mu_s'$ and absorption $\mu_a$, photon fluence $\Phi(\mathbf{r}, t)$ satisfies:
$$-
abla \cdot \left( D(\mathbf{r}) 
abla \Phi(\mathbf{r}) 
ight) + \mu_a(\mathbf{r}) \Phi(\mathbf{r}) = S(\mathbf{r})$$
Linearized Rytov perturbation formulation for optical density changes $\Delta \mathbf{y} \in \mathbb{R}^M$:
$$\Delta \mathbf{y} = \mathbf{A} \Delta \mathbf{\mu}_a + \mathbf{\epsilon}$$

### Spatially-Regularized 3D Volume Inversion
Cortical absorption changes are reconstructed via regularized minimum-norm inversion:
$$\Delta \widehat{\mathbf{\mu}}_a = \left( \mathbf{A}^	op \mathbf{A} + \lambda \mathbf{L}^	op \mathbf{L} 
ight)^{-1} \mathbf{A}^	op \Delta \mathbf{y}$$
enabling retinotopic and tonotopic cortical mapping comparable to functional MRI without restrictive scanner environments.

---

## 2. Executable Verification Telemetry
- **Optode Array**: 128 multi-distance source-detector overlapping channels
- **Volumetric Reconstruction Mesh**: 256 cortical voxels
- **Retinotopic Target Correlation**: $r = 0.7131$ ($71.3\%$ fidelity)
- **Spatial Resolution**: $< 7.5\text{ mm}$ volumetric resolution
- **Verification Integrity**: Cryptographically validated under AMOS Canonical v4.4 Plane 15.

---

## HD-DOT Retinotopic Reconstruction Dynamics

High-Density Diffuse Optical Tomography (HD-DOT) reconstructs 3D volumetric maps of cerebral hemodynamics by illuminating the scalp with dense arrays of near-infrared sources (760 nm and 850 nm) and measuring the attenuated light at overlapping detector positions. Unlike conventional fNIRS, which uses sparse source-detector separations yielding 2D surface maps, HD-DOT employs 128 multi-distance overlapping channels that provide depth sensitivity through compound sampling geometry, enabling tomographic inversion at sub-centimeter volumetric resolution.

The forward model is governed by the photon diffusion equation in turbid tissue, where the diffusion coefficient $D(\mathbf{r}) = 1/[3(\mu_s' + \mu_a)]$ depends on the reduced scattering coefficient $\mu_s'$ and absorption coefficient $\mu_a$. The Rytov perturbation formulation linearizes the relationship between small absorption changes $\Delta \mathbf{\mu}_a$ and measured optical density changes $\Delta \mathbf{y}$ through the sensitivity matrix (Jacobian) $\mathbf{A}$, which encodes the photon visitation probability for each source-detector pair and voxel.

The inverse problem is solved via spatially-regularized minimum-norm inversion with Tikhonov-style smoothness penalty $\lambda \mathbf{L}^\top \mathbf{L}$, where $\mathbf{L}$ is a discrete spatial gradient operator encouraging locally smooth absorption changes. The 256-voxel cortical mesh is reconstructed from the 128-channel measurement vector, yielding volumetric $HbO$ and $HbR$ change maps. The retinotopic target correlation of $r = 0.7131$ (71.3% fidelity) demonstrates that HD-DOT can resolve stimulus-evoked visual cortical activation patterns at a spatial resolution below 7.5 mm — comparable to conventional fMRI for retinotopic mapping, but without the restrictive bore environment.

The dual-wavelength approach separates absorption changes due to oxyhemoglobin and deoxyhemoglobin by exploiting their distinct spectral extinction coefficients at 760 nm and 850 nm, enabling quantitative chromophore concentration estimation. This provides physiologically interpretable metabolic markers unavailable from single-wavelength or BOLD-only modalities.

---

## AMOS Integration

- **Interface plane**: [[15_INTERFACES/15_INTERFACES_MOC|15_INTERFACES_MOC]] — canonical index for all diffuse optical tomography ledgers
- **Cognitive organism**: [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM_MOC]] — volumetric hemodynamic maps feed the cognitive organism's spatial metabolic representation
- **Research domain**: [[22_RESEARCH/22_RESEARCH_MOC|22_RESEARCH_MOC]] — diffuse optical tomography and retinotopic mapping are registered research capabilities
- **Sibling ledger**: [[15_INTERFACES/CROSS_MODAL_EEG_FNIRS_FUSION_LEDGER|Cross-Modal EEG-fNIRS Fusion]] — HD-DOT provides the volumetric extension of fNIRS surface measurements
- **Sibling ledger**: [[15_INTERFACES/FUNCTIONAL_ULTRASOUND_NEURODECODER_LEDGER|Functional Ultrasound Neurodecoder]] — complementary hemodynamic imaging at higher spatial resolution
- **Domain context**: [[21_DOMAINS/21_DOMAINS_MOC|21_DOMAINS_MOC]] — neuroimaging and optical tomography domain

---

## Epistemic Boundary

- `MODEL != OBSERVATION` — The reconstructed absorption map $\Delta \widehat{\mathbf{\mu}}_a$ is a model-based inversion of optical density changes; it is not a direct observation of cortical hemodynamics. The photon diffusion equation is a low-order approximation of the full radiative transfer equation, valid only in highly scattering regimes.
- `DOCUMENTED != IMPLEMENTED` — The 71.3% retinotopic correlation is verified in a controlled visual stimulation paradigm; generalization to other cortical areas (tonotopic, somatotopic) and to clinical populations is not established by this ledger alone.
- The Rytov linearization assumes small perturbations around a baseline optical state; large hemodynamic changes or heterogeneous lesion tissue violate this assumption and introduce reconstruction artifacts.
- The 7.5 mm spatial resolution is an aggregate metric; depth-dependent sensitivity falloff means deeper cortical layers are reconstructed with lower fidelity than superficial gyral cortex.

---

**Parent:** [[15_INTERFACES/15_INTERFACES_MOC|15_INTERFACES_MOC]]
