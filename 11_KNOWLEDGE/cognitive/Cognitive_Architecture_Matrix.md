---
AMOS_KNOWLEDGE_OBJECT:
  schema_family: RSCF
  schema_role: KNOWLEDGE_RSCF
  schema_version: "AMOS_CORE_v4.4-compatible-conceptual"
  object_status: ACTIVE_REFERENCE
  ingestion_state: NORMALIZED_FROM_PRIMARY_SOURCE
  mutation_policy: APPEND_OR_VERSION_NEVER_SILENT_OVERWRITE

  # ============================================================
  # 0. IDENTITY / ADDRESS
  # ============================================================

  identity:

    node_id:
      "RSCF.KNOWLEDGE.COSMOLOGY.CMB.SOUTH_POLE.OBSERVATIONAL_HISTORY.0707_1075"

    canonical_slug:
      "0707_1075_cmb_from_the_south_pole_past_present_and_future"

    canonical_title:
      "CMB from the South Pole: Past, Present, and Future"

    preferred_path:
      H: "11_KNOWLEDGE/cosmology"
      M: "cmb/observational_cosmology/south_pole"
      L: "arxiv/2007/0707_1075"

    legacy_path:
      "11_KNOWLEDGE/_arxiv_md/2007/0707_1075_CMB_FROM_THE_SOUTH_POLE_PAST_PRESENT_AND_FUTURE.md"

    parent_rscf:
      - "RSCF.KNOWLEDGE.PHYSICS"
      - "RSCF.KNOWLEDGE.COSMOLOGY"
      - "RSCF.KNOWLEDGE.COSMOLOGY.CMB"
      - "RSCF.KNOWLEDGE.COSMOLOGY.CMB.POLARIZATION"
      - "RSCF.KNOWLEDGE.COSMOLOGY.CMB.ANISOTROPY"
      - "RSCF.KNOWLEDGE.COSMOLOGY.INFLATION"
      - "RSCF.KNOWLEDGE.COSMOLOGY.DARK_ENERGY"
      - "RSCF.KNOWLEDGE.OBSERVATIONAL_ASTRONOMY.ANTARCTICA"

    node_type:
      KNOWLEDGE

    knowledge_type:
      - PRIMARY_SOURCE
      - CONFERENCE_REVIEW
      - HISTORICAL_FIELD_REVIEW
      - CMB
      - OBSERVATIONAL_COSMOLOGY
      - SOUTH_POLE
      - POLARIZATION
      - TEMPERATURE_ANISOTROPY
      - INSTRUMENTATION
      - INFLATION
      - DARK_ENERGY
      - SUNYAEV_ZELDOVICH
      - EXPERIMENT_LINEAGE

    source_epoch:
      arxiv_id: "0707.1075"
      arxiv_version: "v1"
      arxiv_date: "2007-07-09"

  # ============================================================
  # 1. EPISTEMIC CONTRACT
  # ============================================================

  epistemic_contract:

    site_characteristics:
      SOURCE_CLAIM

    historical_experiment_status:
      SOURCE_CLAIM

    experiment_performance_claims:
      SOURCE_CLAIM

    future_project_forecasts:
      SOURCE_CLAIM_HISTORICAL

    cosmological_interpretations:
      SOURCE_CLAIM

    AMOS_structural_synthesis:
      DERIVED

    contemporary_status:
      UNKNOWN_UNLESS_REVALIDATED

    conclusion_class:
      DERIVED

    source_boundary: >
      This node preserves Kovac and Barkats' 2007 review of South Pole CMB
      observing, including site characteristics, experimental history,
      instrumentation, scientific achievements, and planned experiments.
      Statements concerning "current", "future", experiment status,
      sensitivity targets, detector counts, source counts, best constraints,
      or scientific priorities are bound to the 2007 source epoch.

    hard_rules:

      - >
        Do not treat 2007 "future" plans as current project status.

      - >
        Do not reuse statements such as "first detection", "best current
        constraints", "deepest-yet", or "current frontier" without temporal
        qualification or modern revalidation.

      - >
        Preserve experimental provenance: DASI, ACBAR, BICEP, QUAD, SPT,
        Python, White Dish, and earlier South Pole efforts are distinct
        instruments and observational regimes.

      - >
        Do not infer inflationary gravitational waves from the existence
        or design of a B-mode experiment.

      - >
        Do not equate B-mode polarization generically with primordial
        gravitational waves; lensing B-modes and foregrounds are separate
        mechanisms.

      - >
        Do not infer dark-energy properties directly from SZ detections
        without the cluster-selection, mass-calibration, and cosmological-model
        assumptions required by the survey interpretation.

      - >
        Site superiority is frequency-, weather-, season-, and metric-dependent.
        The source emphasizes atmospheric stability and observing efficiency,
        not universal superiority over all other sites.

      - >
        Atmospheric opacity, stability, observing duty cycle, and sky access
        are distinct site variables.

      - >
        Historical achievement claims inherit the source's publication context
        and cited experimental literature.

    confidence_ceiling:

      source_historical_facts:
        SOURCE_BOUND

      site_measurements:
        SOURCE_BOUND

      source-era_cosmological_interpretation:
        SOURCE_BOUND

      future_predictions_from_2007:
        HISTORICAL_SOURCE_CLAIM

      current_2026_status:
        UNKNOWN_WITHOUT_REVALIDATION

  # ============================================================
  # 2. PROVENANCE
  # ============================================================

  provenance:

    source_id:
      "SRC.ARXIV.0707.1075v1"

    arxiv_id:
      "0707.1075"

    arxiv_version:
      "v1"

    arxiv_category:
      "astro-ph"

    title:
      "CMB from the South Pole: Past, Present, and Future"

    authors:
      - J_M_Kovac
      - D_Barkats

    affiliation:
      "California Institute of Technology"

    pages:
      8

    source_type:
      - CONFERENCE_REVIEW
      - EXPERIMENTAL_HISTORY
      - OBSERVATIONAL_COSMOLOGY_REVIEW

    source_domains:
      - CMB_temperature
      - CMB_polarization
      - South_Pole_site_testing
      - atmospheric_transmission
      - bolometers
      - interferometry
      - Inflation
      - SZ_clusters
      - dark_energy
      - gravitational_lensing

    raw_source_policy:
      DO_NOT_LOAD_UNLESS_REQUIRED

    raw_source_load_triggers:
      - exact_instrument_parameter
      - exact_temperature_anisotropy_value
      - exact_frequency_band
      - experiment_timeline
      - detector_count
      - exact_foreground_claim
      - historical_priority_claim
      - exact_sensitivity_target

  # ============================================================
  # 3. BOOTSTRAP CAPSULE
  # ============================================================

  bootstrap_capsule:

    class:
      DERIVED

    text: >
      Kovac and Barkats review roughly two decades of CMB observation from
      the South Pole, arguing that the site's high altitude, exceptionally
      low water vapor, atmospheric stability, six-month winter darkness,
      fixed-elevation sky tracks, and mature infrastructure made it unusually
      effective for long-duration millimeter-wave observations. The historical
      sequence progresses from early site-validation and temperature-anisotropy
      experiments through Python, Viper/ACBAR, DASI, and QUAD, culminating in
      2007-era programs aimed at two emerging frontiers: degree-scale CMB
      polarization for inflationary B-modes and arcminute-scale secondary
      anisotropies for structure growth, SZ clusters, gravitational lensing,
      dark energy, and neutrino constraints. The source is best represented
      as a coupled site -> instrument -> observable -> cosmological-inference
      lineage, with a strict temporal firewall around 2007 status claims.

    retrieval_keywords:
      - South Pole CMB
      - Kovac Barkats
      - BICEP
      - DASI
      - QUAD
      - ACBAR
      - SPT
      - Python telescope
      - CMB polarization
      - B modes
      - SZ clusters
      - atmospheric stability
      - Southern Hole
      - Inflation

  # ============================================================
  # 4. H / M / L FRACTAL ARCHITECTURE
  # ============================================================

  HML:

    H:

      id:
        "H.SOUTH_POLE_CMB_OBSERVATORY_ARCHITECTURE"

      governing_question: >
        How do the physical characteristics and infrastructure of the
        South Pole enable progressively more sensitive CMB measurements,
        and how do those measurements map onto cosmological questions?

      core_pattern:

        class:
          DERIVED

        expression: >
          SITE_PROPERTIES
          ->
          OBSERVING_STABILITY
          ->
          INSTRUMENT_DESIGN
          ->
          LONG_INTEGRATION
          ->
          CMB_OBSERVABLE
          ->
          COSMOLOGICAL_CONSTRAINT

    M:

      id:
        "M.SOUTH_POLE_CMB_SYSTEM"

      subsystems:

        M1_SITE:
          includes:
            - altitude
            - low_PWV
            - cold_temperature
            - atmospheric_stability
            - continuous_winter_darkness
            - constant_target_elevation

        M2_INFRASTRUCTURE:
          includes:
            - logistics
            - cryogen_support
            - electrical_power
            - observatory_space
            - satellite_data_transfer

        M3_EARLY_EXPERIMENTS:
          includes:
            - EMILIE
            - Bell_Princeton
            - Smoot_radiometers
            - UCSB_ACME
            - White_Dish

        M4_DARK_SECTOR_BUILDOUT:
          includes:
            - Python
            - Viper
            - ACBAR
            - DASI
            - QUAD

        M5_INFLATION_FRONTIER:
          includes:
            - BICEP
            - BICEP2
            - SPUD
            - degree_scale_B_modes

        M6_SMALL_SCALE_FRONTIER:
          includes:
            - SPT
            - SZ_cluster_surveys
            - lensing_B_modes
            - growth_of_structure

        M7_FOREGROUNDS:
          includes:
            - thermal_dust
            - synchrotron
            - Southern_Hole

        M8_COSMOLOGICAL_TARGETS:
          includes:
            - inflation
            - dark_energy
            - dark_matter
            - neutrinos
            - structure_growth

    L:

      id:
        "L.SOUTH_POLE_CMB_EXPERIMENT_PARAMETERS"

      dimensions:
        - frequency
        - angular_scale
        - detector_count
        - aperture
        - sensitivity
        - integration_time
        - field_area
        - atmospheric_opacity
        - atmospheric_fluctuation
        - observing_season

    HML_integrity_rule: >
      No cosmological conclusion may be detached from its instrument,
      angular scale, observing band, foreground regime, and source epoch.

  # ============================================================
  # 5. SITE CHARACTERISTICS
  # ============================================================

  site:

    location:
      Amundsen_Scott_South_Pole_Station

    physical_conditions:

      pressure_altitude:
        source_value:
          "3200 m"

      pressure:
        source_value:
          "681 mbar"

      precipitable_water_vapor:
        source_claim:
          "<0.5 mm over half of the time"

      average_annual_temperature:
        "-49 C"

      minimum_temperature:
        "-82 C"

    key_properties:
      - high
      - dry
      - cold
      - stable

    source_interpretation: >
      These conditions produce high millimeter/submillimeter transmission
      and unusually stable atmospheric emission.

    class:
      SOURCE_CLAIM

  # ============================================================
  # 6. ATMOSPHERIC STABILITY
  # ============================================================

  atmospheric_stability:

    mechanisms:
      - low_daily_thermal_variation
      - katabatic_wind_pattern

    source_metric:

      frequency:
        "150 GHz"

      comparison:
        "South Pole vs ALMA test site"

      source_claim:
        >
          Median wintertime fluctuations were reported as approximately
          30 times lower at the South Pole.

    class:
      SOURCE_CLAIM

    derived_significance: >
      Atmospheric stability can matter as much as raw transparency for
      ultra-sensitive differential CMB measurements.

  # ============================================================
  # 7. OBSERVING-GEOMETRY ADVANTAGE
  # ============================================================

  observing_geometry:

    winter_darkness:
      duration:
        approximately_6_months

      benefit:
        no_solar_contamination

    fixed_elevation_tracking:

      source_claim:
        >
          Target fields remain at the same elevation and do not set.

      benefit:
        - long_integration
        - stable_scan_geometry
        - reduced_field_availability_loss

    derived_pattern:

      expression: >
        POLAR_GEOMETRY
        ->
        CONTINUOUS_FIELD_VISIBILITY
        ->
        VERY_LONG_INTEGRATION

  # ============================================================
  # 8. INFRASTRUCTURE
  # ============================================================

  infrastructure:

    source_claim:
      >
        Fifty years of station operation had created mature support
        infrastructure by the source epoch.

    capabilities:
      - transportation
      - communications
      - construction_support
      - electrical_power
      - technical_support
      - laboratory_space
      - accommodations
      - cryogenic_support

    logistics:

      aircraft:
        LC_130_Hercules

      flight_window:
        "November to mid-February"

      approximate_flights_per_summer:
        300

      winter_inaccessibility:
        approximately_9_months

    operational_consequence:
      >
        Experiments require high reliability and strong annual planning.

    winter_over_model:

      team_size:
        "typically one or two"

      role:
        operate_experiment_during_winter

  # ============================================================
  # 9. SITE-TO-SCIENCE CAUSAL CHAIN
  # ============================================================

  site_science_chain:

    class:
      DERIVED

    expression: >
      LOW_PWV
      + ATMOSPHERIC_STABILITY
      + WINTER_DARKNESS
      + CONSTANT_ELEVATION
      + INFRASTRUCTURE
      ->
      HIGH_OBSERVING_EFFICIENCY
      ->
      DEEP_CMB_MAPS
      ->
      PRECISION_POWER_SPECTRA_AND_POLARIZATION

    causal_firewall: >
      This architecture explains observational capability; it does not
      by itself establish cosmological models inferred from the data.

  # ============================================================
  # 10. HISTORICAL PHASE I — HEROIC AGE
  # ============================================================

  heroic_age:

    epoch:
      "1984-1992"

    EMILIE:

      period:
        "1984-1985"

      aperture:
        "45 cm"

      wavelength:
        "~900 micrometers"

      science:
        galactic_center_dust_emission

      role:
        >
          Early logistical demonstration for submillimeter observing at Pole.

    Bell_Princeton:

      start:
        "1986-1987"

      aperture:
        "1.2 m"

      initial_frequency:
        "400 GHz"

      role:
        >
          First South Pole effort described by the source to measure
          CMB anisotropy.

      nickname:
        bicycle_wheel_experiment

      source_conclusion:
        >
          Confirmed quality of the observing site and paved the way
          for later CMB programs.

  # ============================================================
  # 11. EARLY RADIOMETER PROGRAMS
  # ============================================================

  Smoot_group:

    instrument:
      six_radiometers

    frequencies_GHz:
      - 0.6
      - 0.8
      - 2.5
      - 3.75
      - 7.5
      - 100

    campaigns:
      - "1989-1990"
      - "1991-1992"

    target:
      CMB_temperature_spectrum_distortion

    methods:
      - total_power
      - Dicke_switched_differential_radiometry

  # ============================================================
  # 12. UCSB / ACME
  # ============================================================

  UCSB_ACME:

    campaigns:
      - "1988-1989"
      - "1990-1991"
      - "1993-1994"

    final_configuration:

      bands:
        - Ka
        - Q

      telescope:
        "1 m off-axis Gregorian"

    reported_anisotropy:

      delta_T_rms:
        "41.2 +15.5/-6.7 microK"

      multipole_range:
        "36 < l < 106"

      frequency_range:
        "26-45 GHz"

      source_interpretation:
        >
          Spectrum consistent with thermal CMB anisotropy.

    class:
      SOURCE_CLAIM

  # ============================================================
  # 13. WHITE DISH
  # ============================================================

  White_Dish:

    aperture:
      "1.4 m"

    architecture:
      on_axis_telescope

    detector:
      single_mode_bolometer

    frequency:
      "90 GHz"

    cooling:
      ADR

    observation_periods:
      - "1991-1992"
      - "1992-1993"

    source_result:

      delta_T_rms_upper_limit:
        "<62 microK"

      multipole:
        "~800"

    historical_claim:
      >
        Source describes this as the tightest upper limit at
        sub-degree scales at that time.

  # ============================================================
  # 14. 1992 REGIME SHIFT
  # ============================================================

  regime_shift_1992:

    trigger:
      COBE_large_scale_CMB_anisotropy_detection

    organizational_change:
      CARA

    new_observing_zone:
      Dark_Sector

    derived_AMOS_interpretation:

      expression: >
        FIRST_ROBUST_COSMIC_ANISOTROPY
        ->
        FIELD_CONFIDENCE_INCREASE
        ->
        DEDICATED_INFRASTRUCTURE
        ->
        RAPID_INSTRUMENT_SCALING

  # ============================================================
  # 15. PYTHON
  # ============================================================

  Python:

    first_operation:
      1992

    aperture:
      "0.75 m"

    architecture:
      off_axis

    detector_array:
      "four 90 GHz bolometers"

    bolometer_temperature:
      "50 mK"

    achievements:

      early:
        >
          Degree-scale CMB anisotropy detection.

      repeatability:
        >
          Subsequent season reproduced the signal with multiple tests.

      winter_operation:
        >
          Became first CMB telescope described by source to operate
          through South Pole winter.

      final_maps:
        - "90 GHz"
        - "40 GHz"

    source_lessons:
      - environmental_enclosure_design
      - maintenance_access
      - cryogenic_facilities

    derived_role:
      >
        Python functioned as both science instrument and operational
        prototype for persistent winter CMB astronomy.

  # ============================================================
  # 16. VIPER
  # ============================================================

  Viper:

    commissioned:
      1998

    aperture:
      "2.1 m"

    architecture:
      off_axis_Gregorian

    optical_element:
      chopping_tertiary

    design_goal:
      - higher_throughput
      - higher_angular_resolution_than_Python

  # ============================================================
  # 17. ACBAR
  # ============================================================

  ACBAR:

    full_name:
      Arcminute_Cosmology_Bolometer_Array_Receiver

    telescope:
      Viper

    initial_operation:
      2001

    detector_count:
      16

    bolometer_temperature:
      "250 mK"

    original_frequency_pixels_GHz:
      - 150
      - 220
      - 280

    later_configuration:
      >
        Increasing fraction of focal plane devoted to 150 GHz,
        reaching all 16 pixels in final 2005 winter.

    scientific_output:

      - deep_high_resolution_temperature_maps
      - precise_small_scale_CMB_power_spectrum

    source_claim:
      >
        Combined with CBI and WMAP, ACBAR results provided very strong
        source-era cosmological parameter constraints from the CMB.

    freshness:
      HISTORICAL

  # ============================================================
  # 18. DASI
  # ============================================================

  DASI:

    full_name:
      Degree_Angular_Scale_Interferometer

    architecture:
      compact_interferometer

    frequency_range:
      "26-36 GHz"

    angular_range:
      "140 < l < 910"

    installation:
      1999

    temperature_observing:
      2000

    field_count:
      32

    achievements:

      acoustic_peaks:
        source_claim: >
          DASI independently confirmed harmonic acoustic peak structure
          and measured second and third peak amplitudes.

      polarization:
        upgrade:
          achromatic_polarizers

        observing_start:
          2001

        reported_detection:
          2002

        significance:
          "5 sigma"

        historical_claim:
          first_detection_of_CMB_polarization

    class:
      SOURCE_CLAIM

  # ============================================================
  # 19. QUAD
  # ============================================================

  QUAD:

    lineage:
      >
        DASI platform combined with QUEST 2.6 m Cassegrain telescope
        and bolometric polarization receiver.

    aperture:
      "2.6 m"

    detector_count:
      62

    detector_type:
      polarization_sensitive_bolometers

    frequencies_GHz:
      - 100
      - 150

    observing_status_2007:
      active

    target:

      polarization:
        E_mode

      multipole_range:
        "200 < l < 2000"

    source_claim:
      >
        Producing exceptionally deep E-mode polarization maps
        at medium-to-small angular scales.

    freshness:
      HISTORICAL_2007_STATUS

  # ============================================================
  # 20. SCIENTIFIC FRONTIER SHIFT
  # ============================================================

  frontier_2005_plus:

    priority_1:

      target:
        primordial_B_modes

      scale:
        degree_scale

      science:
        inflationary_gravity_waves

    priority_2:

      target:
        small_scale_CMB_anisotropy

      science:
        - SZ_clusters
        - gravitational_lensing
        - growth_of_structure
        - dark_energy
        - dark_matter
        - neutrinos

    source_basis:
      2005_Task_Force_on_CMB_Research

    class:
      SOURCE_CLAIM_HISTORICAL

  # ============================================================
  # 21. PRIMORDIAL B-MODE INFERENCE CHAIN
  # ============================================================

  primordial_B_mode_chain:

    target:
      inflationary_tensor_perturbations

    observable:
      degree_scale_CMB_B_mode_polarization

    experimental_requirement:
      - ultra_deep_integration
      - low_foreground_field
      - polarization_control
      - large_detector_count

    source_strategy:
      >
        Integrate deeply on approximately 2 percent of sky.

    inference_firewall: >
      A measured B-mode signal requires separation of primordial,
      lensing, foreground, and instrumental components before an
      inflationary tensor interpretation is licensed.

  # ============================================================
  # 22. SOUTHERN HOLE
  # ============================================================

  Southern_Hole:

    sky_area:
      approximately_800_deg2

    sky_fraction:
      "~2 percent"

    primary_advantage:
      low_thermal_dust_emission

    source_claim:
      >
        Thermal dust power may be roughly 100 times lower than in a
        typical high-galactic-latitude field.

    low_foreground_frequency:
      approximately_150_GHz

    visibility:

      South_Pole:
        continuous_high_elevation_view

      Atacama:
        approximately_6_hours_per_day

    class:
      SOURCE_CLAIM

  # ============================================================
  # 23. FOREGROUND MODEL
  # ============================================================

  foregrounds:

    high_frequency:
      dominant:
        thermal_dust

    low_frequency:
      dominant:
        synchrotron

    source_strategy:
      >
        Observe near an intermediate frequency and select an unusually
        clean field to minimize total polarized foreground contamination.

    derived_expression: >
      TOTAL_FOREGROUND(frequency, sky_position)
      =
      DUST
      +
      SYNCHROTRON
      +
      OTHER_COMPONENTS

    firewall: >
      A low-foreground model prediction is not equivalent to direct
      measurement of the actual polarized foreground.

  # ============================================================
  # 24. BICEP
  # ============================================================

  BICEP:

    science_goal:
      >
        Degree-scale B-mode polarization from inflationary
        gravitational waves.

    leaders:
      - A_Lange
      - J_Bock

    detector_count:
      98

    detector_type:
      polarization_sensitive_bolometers

    frequencies_GHz:
      - 100
      - 150

    aperture:
      "30 cm"

    optical_design:
      cryogenic_refractor

    design_priorities:
      - stability
      - high_optical_throughput
      - sidelobe_control
      - large_angular_scale_polarimetry

    first_winter:
      2006

    source_status:
      HISTORICAL_ACTIVE_EXPERIMENT

  # ============================================================
  # 25. BICEP2 / SPUD
  # ============================================================

  BICEP2_SPUD:

    source_status:
      PLANNED_IN_2007

    architecture:
      array_of_seven_monochromatic_telescopes

    first_receiver_target:
      2008

    first_receiver_detector_count:
      512

    detector_type:
      antenna_coupled_TES_bolometers

    frequency:
      "150 GHz"

    predicted_mapping_speed_gain:
      "9x"

    later_deployment_plan:
      >
        Six additional receivers planned for phased deployment
        beginning in 2009.

    epistemic_class:
      HISTORICAL_FORECAST

    firewall: >
      Planned deployment, sensitivity, and mapping speed are not
      equivalent to later achieved performance.

  # ============================================================
  # 26. SPT
  # ============================================================

  SPT:

    full_name:
      South_Pole_Telescope

    aperture:
      "10 m"

    mass:
      "244 metric tons"

    architecture:
      off_axis_Gregorian

    design_surface_accuracy:
      "20 micrometers"

    design_pointing:
      "1 arcsecond"

    first_light:
      "2007-02-16"

    initial_camera:

      detector_count:
        960

      detector_type:
        TES_bolometer_array

      frequencies_GHz:
        - 90
        - 150
        - 220

    initial_science_goal:

      survey:
        SZ_cluster_survey

      maximum_area:
        "up to 4000 deg2"

    cosmological_targets:
      - expansion_rate
      - growth_of_structure
      - dark_energy_equation_of_state

    future_source_plan:
      >
        Polarimeter for small-scale lensing-induced B-mode mapping.

    class:
      SOURCE_CLAIM_WITH_HISTORICAL_FORECASTS

  # ============================================================
  # 27. SZ CLUSTER INFERENCE
  # ============================================================

  SZ_cluster_cosmology:

    observable:
      SZ_cluster_number_counts

    physical_dependency:
      - growth_of_structure
      - cosmic_expansion

    cosmological_targets:
      - dark_energy
      - matter_distribution

    source_model: >
      Large SZ surveys can constrain dark-energy properties through
      cluster abundance evolution.

    inference_firewall:
      >
        Cluster counts require mass-observable calibration, selection
        modeling, and cosmological assumptions; number counts alone do
        not directly measure the dark-energy equation of state.

  # ============================================================
  # 28. LENSING B-MODE BRANCH
  # ============================================================

  lensing_B_modes:

    origin:
      gravitational_lensing_of_CMB_polarization

    angular_scale:
      small_scale

    source_goal:
      >
        Map high-redshift structure formation.

    distinction:

      primordial_B_mode:
        target:
          Inflation

      lensing_B_mode:
        target:
          matter_distribution_and_structure

    firewall: >
      Primordial and lensing B-modes must remain separate mechanism nodes.

  # ============================================================
  # 29. EXPERIMENTAL LINEAGE GRAPH
  # ============================================================

  experiment_lineage:

    ROOT:
      South_Pole_site_validation

    branch_1:
      sequence:
        - EMILIE
        - Bell_Princeton
        - Python
        - Viper
        - ACBAR
        - SPT

      dominant_axis:
        temperature_and_small_scale_resolution

    branch_2:
      sequence:
        - DASI
        - QUAD

      dominant_axis:
        polarization_and_acoustic_scale_measurement

    branch_3:
      sequence:
        - BICEP
        - BICEP2
        - SPUD

      dominant_axis:
        degree_scale_polarization_and_B_modes

    class:
      DERIVED

  # ============================================================
  # 30. TECHNOLOGY EVOLUTION GRAPH
  # ============================================================

  technology_evolution:

    class:
      DERIVED

    stages:

      T0:
        single_detector_radiometer_or_bolometer

      T1:
        small_bolometer_arrays

      T2:
        interferometric_arrays

      T3:
        polarization_sensitive_bolometers

      T4:
        TES_arrays

      T5:
        hundreds_to_thousands_of_detectors

    driving_relation: >
      DETECTOR_COUNT
      + INSTRUMENT_STABILITY
      + OBSERVING_TIME
      ->
      MAPPING_SPEED
      ->
      DEPTH_AND_AREA

    caveat: >
      Mapping speed is not controlled by detector count alone.

  # ============================================================
  # 31. SCIENCE SCALE MAP
  # ============================================================

  angular_scale_map:

    large_scale:

      approximate_scale:
        degree

      observables:
        - primordial_B_modes
        - large_scale_polarization

      experiments:
        - BICEP
        - BICEP2_SPUD

    intermediate_scale:

      multipole_range:
        hundreds_to_thousands

      observables:
        - acoustic_peaks
        - E_mode_polarization

      experiments:
        - DASI
        - QUAD

    small_scale:

      approximate_scale:
        arcminute

      observables:
        - damping_tail
        - SZ
        - lensing
        - secondary_anisotropies

      experiments:
        - ACBAR
        - SPT

  # ============================================================
  # 32. CMB OBSERVABLE GRAPH
  # ============================================================

  observable_graph:

    temperature_anisotropy:

      primary:
        acoustic_peaks

      secondary:
        - SZ
        - lensing_related_effects

    polarization:

      E_mode:
        scalar_perturbation_sensitive

      B_mode:

        primordial:
          inflationary_tensor_candidate

        lensing:
          structure_generated

    derived_AMOS_rule: >
      CMB temperature and polarization observables should be routed by
      angular scale and physical origin before cosmological interpretation.

  # ============================================================
  # 33. FIELD MILESTONE CAPSULES
  # ============================================================

  milestone_capsules:

    MC_DEGREE_ANISOTROPY:

      class:
        SOURCE_CLAIM

      source_summary: >
        South Pole experiments repeatedly detected degree-scale CMB
        temperature anisotropy.

      instruments:
        - UCSB_ACME
        - Python

    MC_ACOUSTIC_PEAKS:

      class:
        SOURCE_CLAIM

      source_summary: >
        DASI contributed to confirmation of harmonic acoustic peak structure.

    MC_FIRST_POLARIZATION:

      class:
        SOURCE_CLAIM

      source_summary: >
        DASI reported the first detection of CMB polarization in 2002.

    MC_SMALL_SCALE_SPECTRUM:

      class:
        SOURCE_CLAIM

      source_summary: >
        ACBAR produced very precise small-scale CMB temperature measurements.

    MC_NEXT_FRONTIERS:

      class:
        HISTORICAL_SOURCE_CLAIM

      source_summary: >
        B-mode inflation searches and small-scale structure/SZ observations
        were identified as major next frontiers.

  # ============================================================
  # 34. TEMPORAL REGIME FIREWALL
  # ============================================================

  temporal_regimes:

    R1984_1992:
      label:
        HEROIC_AGE

      focus:
        - site_validation
        - early_temperature_measurement

    R1992_2005:
      label:
        DARK_SECTOR_BUILDOUT

      focus:
        - degree_scale_anisotropy
        - acoustic_peaks
        - first_polarization
        - small_scale_temperature

    R2005_2007:
      label:
        NEW_FRONTIERS

      focus:
        - primordial_B_modes
        - SZ_cluster_cosmology
        - CMB_lensing

    R_POST_2007:
      label:
        OUTSIDE_SOURCE

      status:
        REVALIDATION_REQUIRED

  # ============================================================
  # 35. PROVENANCE TOPOLOGY
  # ============================================================

  evidence_topology:

    E0:

      type:
        PRIMARY_REVIEW

      id:
        "SRC.ARXIV.0707.1075v1"

    E1:

      type:
        SITE_MEASUREMENTS

      parent:
        E0

      includes:
        - atmospheric_opacity
        - PWV
        - atmospheric_fluctuations

    E2:

      type:
        EXPERIMENTAL_HISTORY

      parent:
        E0

      includes:
        - Python
        - ACBAR
        - DASI
        - QUAD
        - BICEP
        - SPT

    E3:

      type:
        UNDERLYING_PRIMARY_EXPERIMENTS_AS_CITED

      parent:
        E0

      independently_ingested:
        false

    E4:

      type:
        DERIVED_ARCHITECTURE

      parents:
        - E1
        - E2
        - E3

      supports:
        - site_instrument_science_chain
        - experiment_lineage
        - angular_scale_map

      independent:
        false

    anti_sybil_rule: >
      Many experiment results summarized in one review do not count as
      independent evidence until their primary papers are separately ingested.

  # ============================================================
  # 36. COMPETING / CONFOUNDING MECHANISMS
  # ============================================================

  competing_mechanisms:

    B_MODE:

      HYP_B1:
        mechanism:
          primordial_tensor_modes

      HYP_B2:
        mechanism:
          gravitational_lensing

      HYP_B3:
        mechanism:
          Galactic_dust

      HYP_B4:
        mechanism:
          synchrotron

      HYP_B5:
        mechanism:
          instrumental_systematics

      state:
        COMPETING_UNTIL_COMPONENT_SEPARATION

    SMALL_SCALE_TEMPERATURE:

      HYP_T1:
        mechanism:
          primary_CMB_damping_tail

      HYP_T2:
        mechanism:
          thermal_SZ

      HYP_T3:
        mechanism:
          kinetic_SZ

      HYP_T4:
        mechanism:
          foreground_sources

      HYP_T5:
        mechanism:
          lensing_secondary_effects

      state:
        MIXED_SIGNAL_REGIME

  # ============================================================
  # 37. CAUSAL FIREWALL
  # ============================================================

  causal_firewall:

    supported_physical_links:

      water_vapor:
        affects:
          millimeter_opacity_and_fluctuation

      atmospheric_stability:
        affects:
          observational_noise

      long_integration:
        affects:
          map_depth

      detector_count:
        affects:
          mapping_speed_under_other_conditions

      SZ_clusters:
        trace:
          structure_growth

      lensing:
        produces:
          CMB_B_modes

    not_established_directly:

      - detection_of_B_mode_implies_Inflation
      - SPT_cluster_count_alone_determines_dark_energy
      - low_dust_model_guarantees_no_foreground_bias
      - South_Pole_is_optimal_for_every_CMB_measurement
      - detector_count_alone_determines_sensitivity

  # ============================================================
  # 38. SENSITIVITY / LOAD-BEARING VARIABLES
  # ============================================================

  sensitivity:

    site_level:
      highest_leverage:
        - PWV
        - atmospheric_fluctuation
        - field_visibility

    inflation_B_mode:
      highest_leverage:
        - detector_noise
        - foreground_level
        - instrumental_polarization_systematics
        - sky_fraction
        - integration_time
        - lensing_B_mode

    SZ_cosmology:
      highest_leverage:
        - cluster_mass_calibration
        - selection_function
        - survey_area
        - cosmological_model

    fragile_claims:

      "low foreground means primordial B-mode detectable":
        CONDITIONAL

      "cluster counts constrain dark energy":
        CONDITIONAL

      "South Pole superior to Atacama":
        METRIC_AND_REGIME_DEPENDENT

  # ============================================================
  # 39. INVALIDATION CONDITIONS
  # ============================================================

  invalidation_conditions:

    site_claims:
      - newer_site_measurement_changes_comparison
      - frequency_or_weather_regime_changes

    historical_priority:
      - primary_literature_changes_priority_attribution

    B_mode_strategy:
      - foreground_assumptions_invalid
      - lensing_floor_dominates
      - instrument_systematics_exceed_model

    SPT_dark_energy:
      - mass_calibration_failure
      - cluster_selection_bias
      - cosmological_model_mismatch

    temporal_status:
      - any_post_2007_development

  # ============================================================
  # 40. FAILURE RECOVERY
  # ============================================================

  failure_recovery:

    if_site_superiority_claim_changes:

      invalidate:
        - comparative_site_ranking

      preserve:
        - South_Pole_site_measurements
        - historical_instrument_success

    if_B_mode_foreground_model_fails:

      invalidate:
        - expected_primordial_sensitivity

      preserve:
        - BICEP_instrument_design
        - observed_field_selection_strategy

    if_SPT_forecast_changes:

      invalidate:
        - 2007_future_performance_expectation

      preserve:
        - first_light
        - telescope_design
        - initial_science_goal

    rollback_policy:
      LOCAL_DEPENDENCY_INVALIDATION

  # ============================================================
  # 41. STRUCTURAL AMOS PATTERN
  # ============================================================

  structural_pattern:

    name:
      OBSERVATORY_CAPABILITY_TO_COSMOLOGICAL_INFERENCE

    class:
      DERIVED

    expression: >
      ENVIRONMENT
      ->
      OBSERVATORY
      ->
      INSTRUMENT
      ->
      MAP
      ->
      POWER_SPECTRUM_OR_CATALOG
      ->
      PHYSICAL_COMPONENT_SEPARATION
      ->
      COSMOLOGICAL_PARAMETER

    integrity_rule: >
      Do not skip intermediate measurement and modeling layers when
      converting site capability into cosmological claims.

  # ============================================================
  # 42. SECONDARY AMOS PATTERN — ITERATIVE OBSERVATORY EVOLUTION
  # ============================================================

  observatory_evolution_pattern:

    class:
      DERIVED

    expression: >
      PIONEER_EXPERIMENT
      ->
      SITE_VALIDATION
      ->
      OPERATIONAL_FAILURE_AND_LEARNING
      ->
      INFRASTRUCTURE_IMPROVEMENT
      ->
      DETECTOR_SCALING
      ->
      HIGHER_SENSITIVITY
      ->
      NEW_SCIENCE_REGIME

    source_examples:

      Python:
        contribution:
          winter_operation_lessons

      Viper_ACBAR:
        contribution:
          small_scale_precision

      DASI_QUAD:
        contribution:
          polarization_transition

      BICEP_SPUD:
        contribution:
          detector_scaling_for_B_modes

      SPT:
        contribution:
          large_aperture_secondary_CMB_surveys

  # ============================================================
  # 43. PROOF / CLAIM CAPSULES
  # ============================================================

  proof_capsules:

    PC_SITE_ADVANTAGE:

      claim:

        class:
          SOURCE_CLAIM

        text: >
          The South Pole combines low water vapor, cold temperatures,
          atmospheric stability, long winter darkness, and continuous
          field visibility, making it highly suitable for deep CMB observations.

      premises:
        - site_measurements
        - polar_geometry
        - infrastructure

      confidence_ceiling:
        SOURCE_BOUND

    PC_DASI_POLARIZATION:

      claim:

        class:
          SOURCE_CLAIM

        text: >
          DASI reported a 5-sigma detection of CMB polarization in 2002,
          described by the source as the first such detection.

      evidence:
        - cited_DASI_primary_result

      confidence_ceiling:
        SOURCE_BOUND

    PC_ACBAR_SMALL_SCALE:

      claim:

        class:
          SOURCE_CLAIM

        text: >
          ACBAR produced high-precision measurements of the small-scale
          CMB temperature power spectrum.

      confidence_ceiling:
        SOURCE_BOUND

    PC_BMODE_FRONTIER:

      claim:

        class:
          HISTORICAL_SOURCE_CLAIM

        text: >
          By the source epoch, the search for degree-scale primordial
          B-mode polarization was identified as a leading CMB research frontier.

      temporal_validity:
        2007

    PC_SPT_SZ:

      claim:

        class:
          MODEL_WITH_SOURCE_DESIGN

        text: >
          A large SZ cluster survey can constrain structure growth and
          dark-energy parameters under appropriate cosmological and
          cluster-calibration assumptions.

      confidence_ceiling:
        MODEL

  # ============================================================
  # 44. ATOMIC RSCF SUBNODES
  # ============================================================

  atomic_subnodes:

    - id: "RSCF.0707_1075.H.SOUTH_POLE_CMB"
      type: H_NODE

    - id: "RSCF.0707_1075.M.SITE"
      type: M_NODE

    - id: "RSCF.0707_1075.M.INFRASTRUCTURE"
      type: M_NODE

    - id: "RSCF.0707_1075.M.EARLY_CMB"
      type: M_NODE

    - id: "RSCF.0707_1075.M.PYTHON"
      type: M_NODE

    - id: "RSCF.0707_1075.M.ACBAR"
      type: M_NODE

    - id: "RSCF.0707_1075.M.DASI"
      type: M_NODE

    - id: "RSCF.0707_1075.M.QUAD"
      type: M_NODE

    - id: "RSCF.0707_1075.M.BICEP"
      type: M_NODE

    - id: "RSCF.0707_1075.M.SPT"
      type: M_NODE

    - id: "RSCF.0707_1075.M.FOREGROUNDS"
      type: M_NODE

    - id: "RSCF.0707_1075.M.PRIMORDIAL_B_MODES"
      type: MODEL_NODE

    - id: "RSCF.0707_1075.M.SZ_COSMOLOGY"
      type: MODEL_NODE

    - id: "RSCF.0707_1075.L.SOUTH_POLE_PWV"
      type: OBSERVATION_NODE

    - id: "RSCF.0707_1075.L.DASI_POLARIZATION"
      type: OBSERVATION_NODE

    - id: "RSCF.0707_1075.L.SPT_FIRST_LIGHT"
      type: EVENT_NODE

    - id: "RSCF.0707_1075.L.SOUTHERN_HOLE"
      type: SKY_FIELD_NODE

  # ============================================================
  # 45. QUERY ROUTING
  # ============================================================

  routing_index:

    aliases:
      - South Pole CMB
      - 0707.1075
      - Kovac Barkats
      - CMB South Pole history
      - BICEP history
      - DASI polarization
      - ACBAR
      - SPT first light
      - Southern Hole
      - South Pole atmospheric stability

    semantic_routes:

      "Why observe the CMB from the South Pole?":
        route:
          - site
          - atmospheric_stability
          - observing_geometry
          - infrastructure

      "What did DASI achieve?":
        route:
          - DASI

      "What did ACBAR measure?":
        route:
          - ACBAR

      "Why was BICEP designed?":
        route:
          - BICEP
          - primordial_B_mode_chain

      "What is the Southern Hole?":
        route:
          - Southern_Hole
          - foregrounds

      "What was SPT designed to do?":
        route:
          - SPT
          - SZ_cluster_cosmology

      "What were the main CMB frontiers in 2007?":
        route:
          - frontier_2005_plus

      "Does B-mode detection prove inflation?":
        route:
          - primordial_B_mode_chain
          - competing_mechanisms
          - causal_firewall
        expected_answer:
          NO

      "Are these experiment statuses current?":
        route:
          - temporal_regimes
        expected_answer:
          NO_REVALIDATION_REQUIRED

  # ============================================================
  # 46. GMEF BINDING
  # ============================================================

  GMEF_binding:

    status:
      PARTIAL_UNBOUND

    reason: >
      Exact canonical GMEF serialization is not available in the loaded
      canon layer. Preserve semantic topology without inventing missing
      canonical field names.

    candidate_entities:
      - CMB_photon
      - telescope
      - bolometer
      - atmosphere
      - dust
      - synchrotron
      - galaxy_cluster
      - gravitational_lens

    candidate_fields:
      - atmosphere
      - sky
      - detector_array
      - polarization_field
      - temperature_anisotropy_field

    candidate_interactions:
      - atmospheric_absorption
      - atmospheric_emission
      - Thomson_scattering
      - gravitational_lensing
      - Sunyaev_Zeldovich_scattering
      - dust_emission
      - synchrotron_emission

    candidate_observables:
      - C_l_TT
      - C_l_EE
      - C_l_BB
      - cluster_count
      - opacity
      - PWV
      - map_depth

    candidate_regimes:
      - degree_scale
      - arcminute_scale
      - large_scale_polarization
      - small_scale_temperature
      - foreground_limited
      - instrument_noise_limited

  # ============================================================
  # 47. KNOWLEDGE LIFECYCLE
  # ============================================================

  lifecycle:

    pipeline:
      - HISTORICAL_SOURCE
      - PERSISTENT_EVIDENCE
      - NORMALIZED_RSCF
      - PRIMARY_EXPERIMENT_INGESTION
      - TEMPORAL_REVALIDATION
      - MODERN_CMB_LINEAGE_INTEGRATION

    current_stage:
      NORMALIZED_RSCF

    retention_class:
      LONG_TERM_CMB_OBSERVATORY_HISTORY_REFERENCE

    revalidation_priority:

      CRITICAL:
        - BICEP2_SPUD_future_status
        - SPT_future_status
        - current_B_mode_constraints
        - current_dark_energy_constraints

      DECISION_RELEVANT:
        - current_site_comparisons
        - current_foreground_models
        - modern_detector_sensitivity

      EXPLANATORY:
        - instrument_history
        - South_Pole_infrastructure_lineage

  # ============================================================
  # 48. RELATIONS
  # ============================================================

  relations:

    INDEXED_BY:
      - AMOS_RSCF_NODES
      - 11_KNOWLEDGE_MOC

    BELONGS_TO:
      - COSMOLOGY
      - CMB
      - OBSERVATIONAL_ASTRONOMY
      - ANTARCTIC_ASTRONOMY

    ABOUT:
      - SOUTH_POLE
      - CMB_TEMPERATURE
      - CMB_POLARIZATION
      - B_MODES
      - INFLATION
      - SUNYAEV_ZELDOVICH
      - DARK_ENERGY
      - GRAVITATIONAL_LENSING

    SHOULD_LINK_TO:
      - COBE
      - WMAP
      - DASI
      - QUAD
      - ACBAR
      - BICEP
      - BICEP2
      - SOUTH_POLE_TELESCOPE
      - CMB_B_MODES
      - CMB_E_MODES
      - SZ_EFFECT
      - CMB_LENSING
      - GALACTIC_DUST
      - SYNCHROTRON_FOREGROUNDS

  # ============================================================
  # 49. FINAL KNOWLEDGE CAPSULE
  # ============================================================

  final_capsule:

    claim:

      class:
        DERIVED

      text: >
        Kovac and Barkats present the South Pole as a CMB observatory whose
        scientific productivity emerges from a coupling between environmental
        stability, polar observing geometry, mature station infrastructure,
        progressively more capable detector systems, and increasingly focused
        cosmological objectives. Early experiments established site viability
        and degree-scale temperature anisotropy; Python demonstrated long-term
        winter operation; Viper/ACBAR extended precision temperature
        measurements to small angular scales; DASI mapped acoustic structure
        and reported the first CMB polarization detection; QUAD pushed deeper
        E-mode observations; BICEP and its planned successors targeted
        degree-scale primordial B-modes; and SPT was designed for large
        arcminute-scale SZ and structure surveys. The deepest reusable
        architecture is therefore SITE -> INSTRUMENT -> OBSERVABLE ->
        COMPONENT SEPARATION -> COSMOLOGICAL INFERENCE. The source should
        remain temporally bounded to 2007 for experiment status, sensitivity
        forecasts, foreground expectations, and "current frontier" statements.

    strongest_source_support:
      - site
      - atmospheric_stability
      - Python
      - ACBAR
      - DASI
      - QUAD
      - BICEP
      - SPT
      - Southern_Hole

    weakest_load_bearing_premises:
      - 2007_foreground_models
      - future_detector_performance
      - cluster_mass_to_dark_energy_inference
      - primordial_B_mode_forecast

    unresolved_at_source_epoch:
      - primordial_gravitational_wave_B_modes
      - tensor_to_scalar_ratio_at_target_sensitivity
      - lensing_B_mode_precision
      - SZ_dark_energy_constraints
      - full_foreground_complexity
      - ultimate_detector_scaling

    confidence_ceiling:

      historical_experiment_summary:
        SOURCE_BOUND

      site_to_observing_capability:
        DERIVED_WITH_SOURCE_SUPPORT

      future_2007_predictions:
        HISTORICAL_SOURCE_CLAIM

      contemporary_cosmology:
        UNKNOWN_WITHOUT_REVALIDATION

    safe_reuse:
      - South_Pole_CMB_history
      - CMB_experiment_lineage
      - site_selection_reasoning
      - observational_cosmology_architecture
      - temperature_vs_polarization_scale_mapping
      - B_mode_component_separation_reasoning

    revalidation_required:
      - current_BICEP_status
      - current_SPT_status
      - current_tensor_constraints
      - current_CMB_foregrounds
      - current_SZ_cosmology
      - current_dark_energy_constraints
      - modern_site_comparison

---