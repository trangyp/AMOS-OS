---
title: uni market engine
type: reference
tags: [reference, amos-c07-econ-finance-master]
---

# AMOS Uni Market Engine

> Source: `_00_Cosmo brain/engine/A/AMOS_Uni_Market_Engine_v0_Unipower4.md`
> Epistemic class: SOURCE_DERIVED

---
canon-group: human-system
canon-type: framework
rscf-state: source-claim
topic: amos-uni-market-engine-v0
tags: [canon-group/tech-ai, canon/framework, rscf/claim, rscf/provenance, rscf/state/observation, topic/amos-uni-market-engine-v0, engine]
created: 2026-08-22
---

[
  {
    "meta": {
      "name": "VN_Driver_Charging_Logistics_SUPER_Engine_vInfinity_clean",
      "version": "vInfinity_clean_2.0.0",
      "created_at_utc": "2025-11-27T09:22:50.183031Z",
      "description": "Refactored, size-optimised version of VN_Driver_Charging_Logistics_SUPER_Engine_x100k. Removes explicit x100k layers and keeps a canonical virtual expansion model plus all axes for drivers, logistics, charging, roles, scenarios, and Vietnam geography.",
      "country": "Vietnam",
      "density_profile": "x100k_virtual_kernel_only",
      "primitive_count": 19,
      "domain_count": 9,
      "province_count": 63,
      "source_engine": "VN_Driver_Charging_Logistics_SUPER_Engine_x100k"
    },
    "engine": {
      "primitives": [
        "driver",
        "vehicle",
        "charging_point",
        "battery_asset",
        "route",
        "trip",
        "session",
        "tariff",
        "payment_flow",
        "energy_flow",
        "grid_node",
        "policy_rule",
        "contract",
        "service_plan",
        "maintenance_event",
        "downtime_event",
        "safety_event",
        "data_stream",
        "control_signal"
      ],
      "vn_domains": [
        "driver_behaviour_and_experience",
        "vehicle_and_fleet_management",
        "charging_infrastructure_network",
        "energy_grid_and_load_interaction",
        "pricing_payments_and_finance",
        "digital_os_and_data_integration",
        "regulation_policy_and_compliance",
        "city_ecosystem_and_urban_planning",
        "logistics_and_last_mile_networks"
      ],
      "vn_geography": {
        "provinces_63": [
          "Ha Noi",
          "Ho Chi Minh",
          "Hai Phong",
          "Da Nang",
          "Can Tho",
          "An Giang",
          "Ba Ria \u2013 Vung Tau",
          "Bac Giang",
          "Bac Kan",
          "Bac Lieu",
          "Bac Ninh",
          "Ben Tre",
          "Binh Dinh",
          "Binh Duong",
          "Binh Phuoc",
          "Binh Thuan",
          "Ca Mau",
          "Cao Bang",
          "Dak Lak",
          "Dak Nong",
          "Dien Bien",
          "Dong Nai",
          "Dong Thap",
          "Gia Lai",
          "Ha Giang",
          "Ha Nam",
          "Ha Tinh",
          "Hai Duong",
          "Hau Giang",
          "Hoa Binh",
          "Hung Yen",
          "Khanh Hoa",
          "Kien Giang",
          "Kon Tum",
          "Lai Chau",
          "Lam Dong",
          "Lang Son",
          "Lao Cai",
          "Long An",
          "Nam Dinh",
          "Nghe An",
          "Ninh Binh",
          "Ninh Thuan",
          "Phu Tho",
          "Phu Yen",
          "Quang Binh",
          "Quang Nam",
          "Quang Ngai",
          "Quang Ninh",
          "Quang Tri",
          "Soc Trang",
          "Son La",
          "Tay Ninh",
          "Thai Binh",
          "Thai Nguyen",
          "Thanh Hoa",
          "Thua Thien Hue",
          "Tien Giang",
          "Tra Vinh",
          "Tuyen Quang",
          "Vinh Long",
          "Vinh Phuc",
          "Yen Bai"
        ],
        "urban_archetypes": [
          "mega_city_core",
          "tier1_urban",
          "tier2_city",
          "industrial_cluster",
          "tourism_cluster",
          "rural_town",
          "remote_area"
        ]
      },
      "vehicle_and_ownership": {
        "vehicle_segments": [
          "ev_2w_motorbike",
          "ev_3w_taxi",
          "ev_4w_passenger_car",
          "ev_4w_taxi_ridehail",
          "ev_minibus_shuttle",
          "ev_bus_city",
          "ev_truck_light",
          "ev_truck_heavy"
        ],
        "ownership_models": [
          "private_individual",
          "small_fleet_owner",
          "

---
**MOC:** [[references_MOC]]
