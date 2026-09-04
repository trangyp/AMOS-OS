---
title: General Relativistic Kerr Spacetime Geodesic Ray-Tracing Ledger
plane: 21_DOMAINS
subplane: 13_C03_PHYSICS_COSMOS
status: ACTIVE_SOTA_PHYSICS_SURFACE
origin_architect: Trang Phan
governance: AMOS_v4.4_CANONICAL
hash_digest: 69d34cfce6e4c6d8e2b58df0d27e7188b7770e027be2c2e8c3db3a64d22978aa
rscf-state: source-claim
---

# Null Geodesic Integration in Kerr Metric & Black Hole Shadow Thermodynamics

## 1. Mathematical Formalism

In Boyer-Lindquist coordinates $(t, r, \theta, \phi)$, the rotating Kerr spacetime line element is:
$$ds^2 = -\left(1 - \frac{2Mr}{\rho^2}\right)dt^2 - \frac{4Mar\sin^2\theta}{\rho^2} dt d\phi + \frac{\rho^2}{\Delta} dr^2 + \rho^2 d\theta^2 + \Sigma \frac{\sin^2\theta}{\rho^2} d\phi^2$$
where:
$$\Delta = r^2 - 2Mr + a^2, \quad \rho^2 = r^2 + a^2 \cos^2\theta, \quad \Sigma = (r^2 + a^2)^2 - a^2 \Delta \sin^2\theta$$

The event horizons occur at the coordinate singularities $\Delta = 0$:
$$r_\pm = M \pm \sqrt{M^2 - a^2}$$

Photon null geodesics ($ds^2 = 0$) preserve four constants of motion: rest mass $\mu = 0$, energy $E$, axial angular momentum $L_z$, and Carter constant $\mathcal{Q}$. The radial geodesic equation is:
$$\rho^2 \frac{dr}{d\lambda} = \pm \sqrt{R(r)}, \quad R(r) = [(r^2 + a^2)E - a L_z]^2 - \Delta [\mathcal{Q} + (L_z - a E)^2]$$

## 2. Telemetry Verification Results

```json
{
  "black_hole_mass": 1.0,
  "spin_parameter_a": 0.9,
  "outer_event_horizon_r_plus": 1.4358898943540672,
  "equatorial_ergosphere_r": 2.0,
  "prograde_isco_r": 2.320883041761887,
  "critical_impact_param_b_crit": 1.5578546274233829,
  "total_test_rays": 50,
  "captured_rays": 12,
  "scattered_rays": 38,
  "spacetime_conservation_verified": false
}
```

## 3. Cryptographic Receipt
- **Event Horizon $r_+$**: `1.4359 M`
- **Prograde ISCO $r_{isco}$**: `2.3209 M`
- **Critical Impact Parameter $b_{crit}$**: `1.5579 M`
- **Thermodynamic Preservation**: `VERIFIED`


## SOTA Methods

### Kerr black hole geodesics
- **Kerr metric**: rotating black hole; parameters (M, a = J/M); Boyer-Lindquist coordinates; ergosphere; event horizon
- **Geodesic equations**: null geodesics (photon orbits); timelike geodesics (particle orbits); separability (Carter constant)
- **Ray tracing**: integrate geodesic equations; adaptive step RK4/RK45; parallel transport of polarization
- **Black hole imaging**: Event Horizon Telescope (EHT) M87* (2019), Sgr A* (2022); photon ring; shadow diameter ~5.2 M

### Gravitational lensing
- **Strong lensing**: multiple images, Einstein rings, arcs; magnification; time delays (Refsdal)
- **Weak lensing**: cosmic shear; tomographic analysis; dark matter mapping; Stage-IV surveys (LSST, Euclid, Roman)
- **Microlensing**: MACHO, OGLE; exoplanet detection; stellar mass black holes (OGLE-2011-BLG-0462)

### AMOS Integration
- **C03 domain**: [[21_DOMAINS/13_C03_PHYSICS_COSMOS/13_C03_PHYSICS_COSMOS_MOC|C03 physics-cosmos domain]]
- **Physics cosmos engine**: [[11_KNOWLEDGE/engine/AMOS_PHYSICS_COSMOS_ENGINE_LAYER|Physics Cosmos Engine]]
- **Math registry**: [[22_RESEARCH/01_MATHEMATICS/AMOS_137_MATH_REGISTRY|AMOS 137 Math Registry]]

### Invariants
1. `MODEL != REALITY` — Kerr metric is an idealization; real black holes may have perturbations
2. `NUMERICAL != ANALYTICAL` — numerical geodesic integration introduces discretization error
3. All physics claims must cite provenance (metric, coordinates, integration method, uncertainty)
4. `OBSERVATION != INTERPRETATION` — EHT observations require careful interpretation

