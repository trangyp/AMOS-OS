---
canon-group: reference
rscf-state: derived
tags: [audit, murk, arxiv, qfm]
---

# arXiv QFM MURK Cross-Check Audit

## RSCF Proof Capsule

```yaml
artifact_id: ARXIV-QFM-MURK-AUDIT
rscf-state: derived
canon-group: reference
claim_class: AMOS_MODEL
provenance: MURK-style logical consistency check over the arXiv corpus
claim: The corpus is structurally consistent with AMOS RSCF frontmatter and QFM domain tags.
evidence: every note was checked for frontmatter, arxiv_id, rscf-state, source, and duplicate IDs.
falsifiers: a note lacks frontmatter or canonical fields; duplicate arxiv_ids remain; a note is misclassified.
```

## Domain Counts

- total: 21774
- quantum: 1914
- fractal: 297
- math: 11013
- qfm_multi: 1158
- other: 9733

## Findings

### missing_frontmatter
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2003.02342v1_Infinite-order_perturbative_treatment_for_quantum_evolution_with_exchange.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.00027v4_The_distribution_of_violent_event_and_interevent_times_in_conflicts.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.00034v1_Time_Series_Feature_Redundancy_Paradox__An_Empirical_Study_Based_on_Mortgage_Def.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.00043v1_Recursive_introversion__iterative_extroversion_and_transitive_ambiversion.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.00052v1_Efficient_and_Scalable_Deep_Reinforcement_Learning_for_Mean_Field_Control_Games.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.00075v1_Community_detection_by_simulated_bifurcation.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.00083v1_AI_Agent_for_Education__von_Neumann_Multi-Agent_System_Framework.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.00086v1_A_Functional_Human_Liver_Tissue_Model__3D_Bioprinted_Co-culture_Discoids.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.00110v1_Modelling_and_Control_of_Spatial_Behaviours_in_Multi-Agent_Systems_with_Applicat.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.00129v1_A_Data-Centric_Approach_to_Detecting_and_Mitigating_Demographic_Bias_in_Pediatri.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.00160v1_Deterministic_Model_of_Incremental_Multi-Agent_Boltzmann_Q-Learning__Transient_C.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.00165v1_Dynamic_Graph_Communication_for_Decentralised_Multi-Agent_Reinforcement_Learning.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.00191v2_Equilibria_in_Network_Constrained_Markets_with_System_Operator.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.00218v1_How_Well_Did_U_S__Rail_and_Intermodal_Freight_Respond_to_the_COVID-19_Pandemic_v.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.00278v1_A_data-driven_biophysical_network_model_reproduces_C__elegans_premotor_neural_dy.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.00296v4_From_Pixels_to_Predicates__Learning_Symbolic_World_Models_via_Pretrained_Vision-.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.00312v1_M2I2__Learning_Efficient_Multi-Agent_Communication_via_Masked_State_Modeling_and.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.00328v1_VoxVietnam__a_Large-Scale_Multi-Genre_Dataset_for_Vietnamese_Speaker_Recognition.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.00382v3_Adventures_in_Demand_Analysis_Using_AI.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.00390v1_Impossibility_of_Self-Organized_Aggregation_without_Computation.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.00461v1_Efficient_support_ticket_resolution_using_Knowledge_Graphs.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.00480v1_Lyapunov-based_Resilient_Secondary_Synchronization_Strategy_of_AC_Microgrids_Und.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.00504v2_The_Algonauts_Project_2025_Challenge__How_the_Human_Brain_Makes_Sense_of_Multimo.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.00618v2_An_Evaluation_of_Borda_Count_Variations_Using_Ranked_Choice_Voting_Data.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.00647v1_Lightweight_G-YOLOv11__Advancing_Efficient_Fracture_Detection_in_Pediatric_Wrist.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.00681v1_Performance_Variance_of_Low_Noise_Resonant_Capacitance_Bridges_While_Replacing_t.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.00720v3_Overground_gait_transitions_are_not_sharp_but_involve_gradually_changing_walk-ru.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.00813v3_Hybrid_Opto-Electrical_Excitation_of_Spin-Transfer_Torque_Nano-Oscillators_for_A.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.00826v2_LLM-Powered_Multi-Agent_System_for_Automated_Crypto_Portfolio_Management.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.00863v2_Paternalism_and_Deliberation__An_Experiment_on_Making_Formal_Rules.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.00865v1_Negative_to_Positive_Co-learning_with_Aggressive_Modality_Dropout.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.00867v1_Interactionalism__Re-Designing_Higher_Learning_for_the_Large_Language_Agent_Era.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.00881v1_Agentic_Systems__A_Guide_to_Transforming_Industries_with_Vertical_AI_Agents.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.00906v2_Large_Language_Model_Based_Multi-Agent_System_Augmented_Complex_Event_Processing.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.01022v3_Efficient_Connectivity-Preserving_Instance_Segmentation_with_Supervoxel-Based_Lo.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.01043v1_Higher_serum_25_OH_D_concentration_is_associated_with_lower_risk_of_metabolic_sy.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.01084v3_Are_Politicians_Responsive_to_Mass_Shootings__Evidence_from_U_S__State_Legislatu.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.01136v2_Symmetries-enhanced_Multi-Agent_Reinforcement_Learning.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.01185v1_Measurable_Improvement_in_Multi-Qubit_Readout_Using_a_Kinetic_Inductance_Traveli.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.01205v1_Harnessing_Multi-Agent_LLMs_for_Complex_Engineering_Problem-Solving__A_Framework.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.01206v1_Sensitivity_of_Room_Impulse_Responses_in_Changing_Acoustic_Environment.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.01219v1_Model_of_an_Open__Decentralized_Computational_Network_with_Incentive-Based_Load_.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.01241v2_Position_building_in_competition_is_a_game_with_incomplete_information.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.01260v1_The_Learning_Crisis__Three_Years_After_COVID-19.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.01266v1_PIMAEX__Multi-Agent_Exploration_through_Peer_Incentivization.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.01278v1_Risk_forecasting_using_Long_Short-Term_Memory_Mixture_Density_Networks.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.01389v2_Optimal_Strategy_Revision_in_Population_Games__A_Mean_Field_Game_Theory_Perspect.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.01438v1_Toi_uu_hieu_suat_toc_do_dong_co_Servo_DC_su_dung_bo_dieu_khien_PID_ket_hop_mang_.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.01448v1_Agency-Driven_Labor_Theory__A_Framework_for_Understanding_Human_Work_in_the_AI_A.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2025/2025-01/2501.01454v3_A_Fourfold_Pathogen_Reference_Ontology_Suite.md
- ... and 12174 more

### missing_arxiv_id
- OK (none found)

### invalid_rscf_state
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.00909v1_Inner_privacy_of_conscious_experiences_and_quantum_information.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.01129v2_TCM-ICP__Transformation_Compatibility_Measure_for_Registering_Multiple_LIDAR_Sca.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.02367v1_Thaddäus_Derfflinger_s_sunspot_observations_during_1802-1824__A_primary_referenc.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.03143v1_The_hard_problem_and_the_measurement_problem__a_no-go_theorem_and_potential_cons.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.03200v1_Differential_comparison_of_identified-hadron___bf_p_t__spectra_from_high-energy_.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.03260v1_Supporting_supervised_learning_in_fungal_Biosynthetic_Gene_Cluster_discovery__ne.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.03857v1_Robust_Brain_Magnetic_Resonance_Image_Segmentation_for_Hydrocephalus_Patients__H.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.05621v2_OralCam__Enabling_Self-Examination_and_Awareness_of_Oral_Health_Using_a_Smartpho.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.05667v1_Hardware-Conscious_Stream_Processing__A_Survey.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.05687_Enhancing_lexical-based_approach_with_external_knowledge_for_Vietnamese_multiple.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.06845v1_A_comment_on_paper_of_Kim_et_al__on_mechanisms_of_hysteresis_in_human_brain_netw.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.08767v1_Interventions_for_Ranking_in_the_Presence_of_Implicit_Bias.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.09442v3_Consciousness_and_Automated_Reasoning.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.09485v2_Multimodal_Data_Fusion_based_on_the_Global_Workspace_Theory.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.10344v1_A_Novel_Approach_Towards_Identification_of_Alcohol_and_Drug_Induced_People.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.10386_Taking_Recoveries_to_Task__Recovery-Driven_Development_for_Recipe-based_Robot_Ta.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.10535v3_Bridging_the_Gap_Between_Consciousness_and_Matter__Recurrent_Out-of-Body_Project.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.11027v3_The_Tensor_Brain__Semantic_Decoding_for_Perception_and_Memory.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.11331v2_Possible_Superluminal_Propagation_inside_Conscious_Beings.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.11385_Theta_surfaces.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.11453_Parameter_Space_Factorization_for_Zero-Shot_Learning_across_Tasks_and_Languages.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.11718v1_Locally_Private_Distributed_Reinforcement_Learning.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.11825v4_Recursion__evolution_and_conscious_self.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.00047v1_Design_Principles_Developed_through_User-Centered_and_Socio-Technical_Methods_Im.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.00175_UIT-ViIC__A_Dataset_for_the_First_Evaluation_on_Vietnamese_Image_Captioning.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.00176v1_Unbiased_Scene_Graph_Generation_via_Rich_and_Fair_Semantic_Extraction.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.00509v2_A_Machine_Consciousness_architecture_based_on_Deep_Learning_and_Gaussian_Process.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.00759_Comparison_Between_Traditional_Machine_Learning_Models_And_Neural_Network_Models.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.00931v1_Stochastic_reaction_networks_in_dynamic_compartment_populations.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.02403v1_Manipulation__trapping__splitting_and_merging_of_water_and_aqueous_bio-droplets_.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.02425v2_A_mean_field_approach_to_model_levels_of_consciousness_from_EEG_recordings.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.02721_Assessing_biophysical_and_socio-economic_impacts_of_climate_change_on_avian_biod.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.03738v1_Human_Creativity_and_Consciousness__Unintended_Consequences_of_the_Brain_s_Extra.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.04082v1_El_experimento_de_Cavendish.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.04347v1_Science_through_Wikipedia__A_novel_representation_of_open_knowledge_through_co-c.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.04852v1_Service_Selection_using_Predictive_Models_and_Monte-Carlo_Tree_Search.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.04895v1_Unveiling_the_research_landscape_of_Sustainable_Development_Goals_and_their_incl.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.05652v1_Functionally_Effective_Conscious_AI_Without_Suffering.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.06191v2_Did_JHotDraw_Respect_the_Law_of_Good_Style___A_deep_dive_into_the_nature_of_fals.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.06313v2_Minimisers_of_a_fractional_seminorm_and_nonlocal_minimal_surfaces.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.06546_Neural_Machine_Translation_with_Joint_Representation.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.06959_Recent_CMS_and_CMS-TOTEM_results_on_diffraction_and_exclusive_production.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.07655v1_The_Mathematical_Structure_of_Integrated_Information_Theory.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.07716v2_Synaptic_clock_as_a_neural_substrate_of_consciousness.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.08082v1_Realtime_Index-Free_Single_Source_SimRank_Processing_on_Web-Scale_Graphs.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.08249v1_Workshop_Report__Detection_and_Classification_in_Marine_Bioacoustics_with_Deep_L.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.08373v1_A_search_for_the_lenses_in_the_Herschel_Bright_Sources__HerBS__Sample.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.08433v1_Modeling_microbial_cross-feeding_at_intermediate_scale_portrays_community_dynami.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.08469v1_Prediction_of_Individual_Propofol_Requirements_based_on_Preoperative_EEG_Signals.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.08575v1_Syndrome-aware_Herb_Recommendation_with_Multi-Graph_Convolution_Network.md
- ... and 16578 more

### missing_source
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.00909v1_Inner_privacy_of_conscious_experiences_and_quantum_information.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.01129v2_TCM-ICP__Transformation_Compatibility_Measure_for_Registering_Multiple_LIDAR_Sca.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.02367v1_Thaddäus_Derfflinger_s_sunspot_observations_during_1802-1824__A_primary_referenc.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.03143v1_The_hard_problem_and_the_measurement_problem__a_no-go_theorem_and_potential_cons.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.03200v1_Differential_comparison_of_identified-hadron___bf_p_t__spectra_from_high-energy_.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.03260v1_Supporting_supervised_learning_in_fungal_Biosynthetic_Gene_Cluster_discovery__ne.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.03857v1_Robust_Brain_Magnetic_Resonance_Image_Segmentation_for_Hydrocephalus_Patients__H.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.05621v2_OralCam__Enabling_Self-Examination_and_Awareness_of_Oral_Health_Using_a_Smartpho.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.05667v1_Hardware-Conscious_Stream_Processing__A_Survey.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.05687_Enhancing_lexical-based_approach_with_external_knowledge_for_Vietnamese_multiple.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.06845v1_A_comment_on_paper_of_Kim_et_al__on_mechanisms_of_hysteresis_in_human_brain_netw.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.08767v1_Interventions_for_Ranking_in_the_Presence_of_Implicit_Bias.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.09442v3_Consciousness_and_Automated_Reasoning.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.09485v2_Multimodal_Data_Fusion_based_on_the_Global_Workspace_Theory.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.10344v1_A_Novel_Approach_Towards_Identification_of_Alcohol_and_Drug_Induced_People.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.10386_Taking_Recoveries_to_Task__Recovery-Driven_Development_for_Recipe-based_Robot_Ta.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.10535v3_Bridging_the_Gap_Between_Consciousness_and_Matter__Recurrent_Out-of-Body_Project.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.11027v3_The_Tensor_Brain__Semantic_Decoding_for_Perception_and_Memory.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.11331v2_Possible_Superluminal_Propagation_inside_Conscious_Beings.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.11385_Theta_surfaces.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.11453_Parameter_Space_Factorization_for_Zero-Shot_Learning_across_Tasks_and_Languages.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.11718v1_Locally_Private_Distributed_Reinforcement_Learning.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2001.11825v4_Recursion__evolution_and_conscious_self.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.00047v1_Design_Principles_Developed_through_User-Centered_and_Socio-Technical_Methods_Im.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.00175_UIT-ViIC__A_Dataset_for_the_First_Evaluation_on_Vietnamese_Image_Captioning.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.00176v1_Unbiased_Scene_Graph_Generation_via_Rich_and_Fair_Semantic_Extraction.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.00509v2_A_Machine_Consciousness_architecture_based_on_Deep_Learning_and_Gaussian_Process.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.00759_Comparison_Between_Traditional_Machine_Learning_Models_And_Neural_Network_Models.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.00931v1_Stochastic_reaction_networks_in_dynamic_compartment_populations.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.02403v1_Manipulation__trapping__splitting_and_merging_of_water_and_aqueous_bio-droplets_.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.02425v2_A_mean_field_approach_to_model_levels_of_consciousness_from_EEG_recordings.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.02721_Assessing_biophysical_and_socio-economic_impacts_of_climate_change_on_avian_biod.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.03738v1_Human_Creativity_and_Consciousness__Unintended_Consequences_of_the_Brain_s_Extra.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.04082v1_El_experimento_de_Cavendish.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.04347v1_Science_through_Wikipedia__A_novel_representation_of_open_knowledge_through_co-c.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.04852v1_Service_Selection_using_Predictive_Models_and_Monte-Carlo_Tree_Search.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.04895v1_Unveiling_the_research_landscape_of_Sustainable_Development_Goals_and_their_incl.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.05652v1_Functionally_Effective_Conscious_AI_Without_Suffering.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.06191v2_Did_JHotDraw_Respect_the_Law_of_Good_Style___A_deep_dive_into_the_nature_of_fals.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.06313v2_Minimisers_of_a_fractional_seminorm_and_nonlocal_minimal_surfaces.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.06546_Neural_Machine_Translation_with_Joint_Representation.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.06959_Recent_CMS_and_CMS-TOTEM_results_on_diffraction_and_exclusive_production.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.07655v1_The_Mathematical_Structure_of_Integrated_Information_Theory.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.07716v2_Synaptic_clock_as_a_neural_substrate_of_consciousness.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.08082v1_Realtime_Index-Free_Single_Source_SimRank_Processing_on_Web-Scale_Graphs.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.08249v1_Workshop_Report__Detection_and_Classification_in_Marine_Bioacoustics_with_Deep_L.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.08373v1_A_search_for_the_lenses_in_the_Herschel_Bright_Sources__HerBS__Sample.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.08433v1_Modeling_microbial_cross-feeding_at_intermediate_scale_portrays_community_dynami.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.08469v1_Prediction_of_Individual_Propofol_Requirements_based_on_Preoperative_EEG_Signals.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2020/2002.08575v1_Syndrome-aware_Herb_Recommendation_with_Multi-Graph_Convolution_Network.md
- ... and 16578 more

### duplicates
- OK (none found)

### unclassified
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2007/0704_3643V1_SABBATH_DAY_HOME_AUTOMATION_IT_S_LIKE_MIXING_TECHNOLOGY_AND_RELIGION.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2007/0705_2972_SUMMARY_TALK_CHALLENGES_IN_PARTICLE_ASTROPHYSICS.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2007/0706_1996V1_PLANET_RB_A_PERSONAL_CONTRIBUTION_TO_A_PROTEOMIC_MAP_OF_HUMAN_RETINOBLASTOMA_PR.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2007/0706_4400V1_ALBERT_EINSTEIN_A_PIOUS_ATHEIST.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2007/0707_1075_CMB_FROM_THE_SOUTH_POLE_PAST_PRESENT_AND_FUTURE.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2007/0708_2061V1_SELECTIVE_VULNERABILITY_TO_KAINATE_INDUCED_OXIDATIVE_DAMAGE_IN_DIFFERENT_RAT_BRA.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2007/0709_0418V1_ROLE_OF_ELECTROSTATIC_INTERACTIONS_IN_THE_ASSEMBLY_OF_EMPTY_SPHERICAL_VIRAL_CAPS.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2008/0802_3664V1_GRAVITAS_PORTRAITS_OF_A_UNIVERSE_IN_MOTION.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2008/0803_3432_THE_THERMODYNAMIC_APPROACH_TO_MARKET.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2008/0803_4074V2_REFLECTIVE_VISUALIZATION_AND_VERBALIZATION_OF_UNCONSCIOUS_PREFERENCE.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2008/0804_0019V2_THE_STELLAR_HALO_OF_THE_GALAXY.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2008/0806_2286V1_EXTRATERRESTRIAL_NUCLEOBASES_IN_THE_MURCHISON_METEORITE.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2008/0806_4202V1_THE_COSMOLOGY_OF_THE_DIVINE_COMEDY.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2008/0807_1039V1_KEYNOTES_ON_MEMBRANE_PROTEOMICS.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2008/0807_1558V1_CYCLOOXYGENASE_INHIBITION_IN_ISCHEMIC_BRAIN_INJURY.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2008/0807_2731V1_RESOURCE_LETTER_BIO_MOLECULAR_NANO_MACHINES_WHERE_PHYSICS_CHEMISTRY_BIOLOGY.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2008/0808_0349_ULTRA_HIGH_ENERGY_COSMIC_RAYS_FROM_RADIO_GALAXIES_REVISITED.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2008/0808_1364_ON_BOUNDED_INTEGER_PROGRAMMING.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2008/0810_4358V1_STIRRING_ASTRONOMY_INTO_THEOLOGY_SIR_ISAAC_NEWTON_ON_THE_DATE_OF_THE_PASSION_OF.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2008/0810_4630V1_PERFORMANCE_OF_THE_TWO_AEROGEL_CHERENKOV_DETECTORS_OF_THE_JLAB_HALL_A_HADRON_SPECTROMETER.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2008/0812_2541V1_PARADOX_IN_PHYSICS_THE_CONSISTENCY_OF_INCONSISTENCY.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2008/0812_4378V1_THE_EQUATIONS_OF_MEDIEVAL_COSMOLOGY.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2009/0901_0168V3_CODING_FOR_TWO_USER_SISO_AND_MIMO_MULTIPLE_ACCESS_CHANNELS.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2009/0902_1426V1_OPTIMAL_DESIGNS_FOR_DOSE_FINDING_EXPERIMENTS_IN_TOXICITY_STUDIES.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2009/0904_0402V1_A_THERMODYNAMIC_BASIS_FOR_PREBIOTIC_AMINO_ACID_SYNTHESIS_AND_THE_NATURE_OF_THE_F.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2009/0904_3254V1_CHARACTERIZATION_OF_A_NAPHTHALENE_DIOXYGENASE_ENDOWED_WITH_AN_EXCEPTIONALLY_BROA.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2009/0905_1482V1_GLOBAL_HOT_GAS_IN_AND_AROUND_THE_GALAXY.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2009/0907_1727V1_MODELING_MOTILITY_OF_THE_KINESIN_DIMER_FROM_MOLECULAR_PROPERTIES_OF_INDIVIDUAL_M.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2009/0907_2192V1_PHYSICAL_FOUNDATIONS_OF_CONSCIOUSNESS_BRAIN_ORGANISATION_THE_ROLE_OF_SYNAPSES.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2009/0907_3355V1_A_NETWORK_BASED_APPROACH_FOR_SURVEILLANCE_OF_OCCUPATIONAL_HEALTH_EXPOSURES.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2009/0907_3410V1_OCCUPATIONAL_HEALTH_PROBLEM_NETWORK_THE_EXPOSOME.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2009/0908_0649V1_SSCMAP_AN_EXTENSIBLE_JAVA_APPLICATION_FOR_CONNECTING_SMALL_MOLECULE_DRUGS_USING.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2009/0909_1138V3_USER_EXPERIENCE_SOFTWARE_INTERFACES_AND_THE_UNCONSCIOUS.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2009/0910_5579V1_LIFE_THE_UNIVERSE_AND_ALMOST_EVERYTHING_SIGNS_OF_COSMIC_DESIGN.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2009/0911_0486_BUILDING_A_VIETNAMESE_LANGUAGE_QUERY_PROCESSING_FRAMEWORK_FOR_ELIBRARY_SEARCHING.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2009/0911_0652V1_BRAINSTORMING_THROUGH_THE_SEQUENCE_UNIVERSE_THEORIES_ON_THE_PROTEIN_PROBLEM.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2009/0912_1829_DOCUMENT_SEARCHING_SYSTEM_BASED_ON_NATURAL_LANGUAGE_QUERY_PROCESSING_FOR_VIETNAM.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2010/1001_3887V1_STARSHIPS_AND_SPINOZA.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2010/1004_1590V1_ELECTROSTATICS_IN_THE_STABILITY_AND_MISFOLDING_OF_THE_PRION_PROTEIN_SALT_BRIDGE.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2010/1006_5707_SMOOTH_STRUCTURES_ON_PSEUDOMANIFOLDS_WITH_ISOLATED_CONICAL_SINGULARITIES.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2010/1007_1270_HOW_TO_MAXIMIZE_USER_SATISFACTION_DEGREE_IN_MULTI_SERVICE_IP_NETWORKS.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2010/1008_2327V1_DENSITY_FUNCTIONAL_THEORY_FOR_STRONGLY_INTERACTING_ELECTRONS_PERSPECTIVES_FOR_P.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2010/1008_5161V3_ARTIFICIAL_BRAIN_BASED_ON_CREDIBLE_NEURAL_CIRCUITS_IN_A_HUMAN_BRAIN.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2010/1009_0077V1_NOT_ONLY_A_LACK_OF_RIGHT_DEFINITIONS_ARGUMENTS_FOR_A_SHIFT_IN_INFORMATION_PROCE.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2010/1010_1051V3_GALACTIC_CORONAE_IN_THE_INTRACLUSTER_ENVIRONMENT_SEMI_CONFINED_STELLAR_FEEDBACK.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2010/1010_3640V3_ON_THE_ITERATED_HAIRPIN_COMPLETION.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2010/1011_5240V1_A_COMPUTATIONAL_MODEL_OF_CELL_POLARIZATION_AND_MOTILITY_COUPLING_MECHANICS_AND_B.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2010/1011_5747V1_OPTIMAL_DESIGNS_FOR_DISCRIMINATING_BETWEEN_DOSE_RESPONSE_MODELS_IN_TOXICOLOGY_ST.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2010/1012_0749V1_THE_THICK_DISK_IN_THE_GALAXY_NGC_4244_FROM_S4G_IMAGING.md
- /Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/_arxiv_md/2010/1012_3148V1_TO_STUDY_THE_PHENOMENON_OF_THE_MORAVEC_S_PARADOX.md
- ... and 9683 more

## Post-Remediation MURK Verification

- frontmatter: 0
- invalid rscf-state: 0
- missing source: 0
- missing arxiv_id: 0
- duplicate arxiv_id: 0

## MURK Verdict

- **HARD contradictions:** none
- **CRITICAL issues:** none
- **Status:** corpus is structurally consistent after remediation.

---
**Related:** [[00-Home]] · [[ARXIV_QFM_MOC]] · [[ARXIV_QFM_CLAIMS]]
- [[00_ROOT_MOC]]
- [[11_KNOWLEDGE_MOC]] · [[AMOS_RSCF_NODES]]
