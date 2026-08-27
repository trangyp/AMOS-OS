---
title: NEO4J GRAPH MODEL 2026 08 12
tags: [models, model, specification]
type: data
source: 11_KNOWLEDGE/models
---





```json
{
  "version": "3.0.0",
  "visualisation": {
    "nodes": [
      {
        "id": "n:1",
        "position": {
          "x": -50.430684540171136,
          "y": -140.5663622633827
        }
      },
      {
        "id": "n:2",
        "position": {
          "x": 139.84909740172733,
          "y": -324.9910034996489
        }
      },
      {
        "id": "n:3",
        "position": {
          "x": 299.57193260317933,
          "y": -178.86139102233832
        }
      },
      {
        "id": "n:4",
        "position": {
          "x": 175.66856527150895,
          "y": -128.42148453840298
        }
      },
      {
        "id": "n:5",
        "position": {
          "x": 266.8995502437135,
          "y": 58.57861329985714
        }
      },
      {
        "id": "n:6",
        "position": {
          "x": 538.7427910340889,
          "y": 192.55420778133222
        }
      },
      {
        "id": "n:7",
        "position": {
          "x": 236.17443347156012,
          "y": -370.51019558587416
        }
      },
      {
        "id": "n:8",
        "position": {
          "x": -102.26263962385956,
          "y": 118.21409125179171
        }
      },
      {
        "id": "n:9",
        "position": {
          "x": -328.524468955335,
          "y": 102.82919274874229
        }
      },
      {
        "id": "n:10",
        "position": {
          "x": -274.8842576382935,
          "y": 276.6916743042396
        }
      },
      {
        "id": "n:11",
        "position": {
          "x": -296.1372285809013,
          "y": -54.812987773499685
        }
      },
      {
        "id": "n:12",
        "position": {
          "x": 8.893104300266298,
          "y": -543.5012817529663
        }
      },
      {
        "id": "n:13",
        "position": {
          "x": -56.92415562865028,
          "y": -305.06821672217734
        }
      },
      {
        "id": "n:14",
        "position": {
          "x": -688.0495596834519,
          "y": -286.19568040771213
        }
      },
      {
        "id": "n:15",
        "position": {
          "x": -597.9983672693381,
          "y": -545.074682083341
        }
      },
      {
        "id": "n:16",
        "position": {
          "x": -207.89146713573766,
          "y": -353.6839130453263
        }
      },
      {
        "id": "n:17",
        "position": {
          "x": 93.2536488795547,
          "y": -333.40811847787205
        }
      },
      {
        "id": "n:18",
        "position": {
          "x": -147.62643467424377,
          "y": -189.7038435086252
        }
      },
      {
        "id": "n:19",
        "position": {
          "x": 77.9999452006158,
          "y": 64.48487278201769
        }
      },
      {
        "id": "n:20",
        "position": {
          "x": 80.6180062910457,
          "y": 197.4388739134272
        }
      },
      {
        "id": "n:21",
        "position": {
          "x": 131.54150076139885,
          "y": -211.5795054942333
        }
      },
      {
        "id": "n:22",
        "position": {
          "x": -221.91494442490807,
          "y": -627.1156464575337
        }
      },
      {
        "id": "n:23",
        "position": {
          "x": -53.34805647704911,
          "y": 343.0731938073788
        }
      },
      {
        "id": "n:24",
        "position": {
          "x": 318.83082391007184,
          "y": -539.8590464171822
        }
      },
      {
        "id": "n:25",
        "position": {
          "x": -364.5829507422324,
          "y": -558.292046119525
        }
      },
      {
        "id": "n:26",
        "position": {
          "x": -371.6430697328434,
          "y": -208.98058117049658
        }
      },
      {
        "id": "n:27",
        "position": {
          "x": 204.7876055155246,
          "y": -452.07639786538095
        }
      },
      {
        "id": "n:28",
        "position": {
          "x": -510.69405272926593,
          "y": 1021.4735035038594
        }
      },
      {
        "id": "n:29",
        "position": {
          "x": -53.77642856881697,
          "y": -448.9327421806776
        }
      }
    ]
  },
  "dataModel": {
    "version": "3.0.0",
    "graphSchemaRepresentation": {
      "version": "1.0.0",
      "graphSchema": {
        "nodeLabels": [
          {
            "$id": "nl:1",
            "token": "User",
            "properties": [
              {
                "$id": "p:1",
                "token": "id",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:2",
                "token": "name",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:3",
                "token": "preferences",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:4",
                "token": "goals",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:5",
                "token": "context",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:6",
                "token": "identity",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:7",
                "token": "privacySettings",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:8",
                "token": "consentState",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:9",
                "token": "type",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:10",
                "token": "ipRights",
                "type": {
                  "type": "string"
                },
                "nullable": false
              }
            ]
          },
          {
            "$id": "nl:10",
            "token": "Marketplace",
            "properties": [
              {
                "$id": "p:60",
                "token": "id",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:61",
                "token": "name",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:62",
                "token": "description",
                "type": {
                  "type": "string"
                },
                "nullable": false
              }
            ]
          },
          {
            "$id": "nl:11",
            "token": "Product",
            "properties": [
              {
                "$id": "p:63",
                "token": "id",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:64",
                "token": "name",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:65",
                "token": "type",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:66",
                "token": "description",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:67",
                "token": "price",
                "type": {
                  "type": "float"
                },
                "nullable": false
              }
            ]
          },
          {
            "$id": "nl:12",
            "token": "Practice",
            "properties": [
              {
                "$id": "p:68",
                "token": "id",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:69",
                "token": "name",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:70",
                "token": "description",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:71",
                "token": "evidenceGrade",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:72",
                "token": "culturalContext",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:73",
                "token": "contraindications",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:74",
                "token": "defaultDuration",
                "type": {
                  "type": "duration"
                },
                "nullable": false
              },
              {
                "$id": "p:75",
                "token": "durationRange",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:76",
                "token": "defaultIntensity",
                "type": {
                  "type": "string"
                },
                "nullable": false
              }
            ]
          },
          {
            "$id": "nl:13",
            "token": "Event",
            "properties": [
              {
                "$id": "p:77",
                "token": "id",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:78",
                "token": "type",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:79",
                "token": "timestamp",
                "type": {
                  "type": "datetime"
                },
                "nullable": false
              },
              {
                "$id": "p:80",
                "token": "status",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:81",
                "token": "version",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:82",
                "token": "businessState",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:83",
                "token": "trace",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:84",
                "token": "correlation",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:85",
                "token": "outcome",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:86",
                "token": "response",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:87",
                "token": "severity",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:88",
                "token": "consequence",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:89",
                "token": "action",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:90",
                "token": "forecastCertainty",
                "type": {
                  "type": "float"
                },
                "nullable": false
              },
              {
                "$id": "p:91",
                "token": "recommendationChain",
                "type": {
                  "type": "string"
                },
                "nullable": false
              }
            ]
          },
          {
            "$id": "nl:14",
            "token": "Rule",
            "properties": [
              {
                "$id": "p:92",
                "token": "id",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:93",
                "token": "name",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:94",
                "token": "description",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:95",
                "token": "category",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:96",
                "token": "condition",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:97",
                "token": "problem",
                "type": {
                  "type": "string"
                },
                "nullable": false
              }
            ]
          },
          {
            "$id": "nl:15",
            "token": "Protocol",
            "properties": [
              {
                "$id": "p:98",
                "token": "id",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:99",
                "token": "name",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:100",
                "token": "description",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:101",
                "token": "version",
                "type": {
                  "type": "string"
                },
                "nullable": false
              }
            ]
          },
          {
            "$id": "nl:16",
            "token": "SystemComponent",
            "properties": [
              {
                "$id": "p:102",
                "token": "id",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:103",
                "token": "name",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:104",
                "token": "type",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:105",
                "token": "description",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:106",
                "token": "latency",
                "type": {
                  "type": "duration"
                },
                "nullable": false
              },
              {
                "$id": "p:107",
                "token": "authenticationScope",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:108",
                "token": "layer",
                "type": {
                  "type": "string"
                },
                "nullable": false
              }
            ]
          },
          {
            "$id": "nl:17",
            "token": "Constraint",
            "properties": [
              {
                "$id": "p:109",
                "token": "id",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:110",
                "token": "name",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:111",
                "token": "type",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:112",
                "token": "description",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:113",
                "token": "severity",
                "type": {
                  "type": "string"
                },
                "nullable": false
              }
            ]
          },
          {
            "$id": "nl:18",
            "token": "Governance",
            "properties": [
              {
                "$id": "p:114",
                "token": "id",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:115",
                "token": "name",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:116",
                "token": "type",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:117",
                "token": "description",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:118",
                "token": "policy",
                "type": {
                  "type": "string"
                },
                "nullable": false
              }
            ]
          },
          {
            "$id": "nl:19",
            "token": "Interpretation",
            "properties": [
              {
                "$id": "p:119",
                "token": "id",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:120",
                "token": "type",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:121",
                "token": "description",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:122",
                "token": "confidence",
                "type": {
                  "type": "float"
                },
                "nullable": false
              },
              {
                "$id": "p:123",
                "token": "mode",
                "type": {
                  "type": "string"
                },
                "nullable": false
              }
            ]
          },
          {
            "$id": "nl:2",
            "token": "Signal",
            "properties": [
              {
                "$id": "p:11",
                "token": "id",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:12",
                "token": "type",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:13",
                "token": "value",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:14",
                "token": "timestamp",
                "type": {
                  "type": "datetime"
                },
                "nullable": false
              },
              {
                "$id": "p:15",
                "token": "source",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:16",
                "token": "provenanceClass",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:17",
                "token": "scope",
                "type": {
                  "type": "string"
                },
                "nullable": false
              }
            ]
          },
          {
            "$id": "nl:20",
            "token": "Notification",
            "properties": [
              {
                "$id": "p:124",
                "token": "id",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:125",
                "token": "type",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:126",
                "token": "content",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:127",
                "token": "probability",
                "type": {
                  "type": "float"
                },
                "nullable": false
              }
            ]
          },
          {
            "$id": "nl:21",
            "token": "Permission",
            "properties": [
              {
                "$id": "p:128",
                "token": "id",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:129",
                "token": "type",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:130",
                "token": "scope",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:131",
                "token": "grantedAt",
                "type": {
                  "type": "datetime"
                },
                "nullable": false
              },
              {
                "$id": "p:132",
                "token": "expiresAt",
                "type": {
                  "type": "datetime"
                },
                "nullable": false
              }
            ]
          },
          {
            "$id": "nl:22",
            "token": "Context",
            "properties": [
              {
                "$id": "p:133",
                "token": "id",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:134",
                "token": "name",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:135",
                "token": "type",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:136",
                "token": "description",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:137",
                "token": "factors",
                "type": {
                  "type": "string"
                },
                "nullable": false
              }
            ]
          },
          {
            "$id": "nl:23",
            "token": "Transformation",
            "properties": [
              {
                "$id": "p:138",
                "token": "id",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:139",
                "token": "name",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:140",
                "token": "description",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:141",
                "token": "status",
                "type": {
                  "type": "string"
                },
                "nullable": false
              }
            ]
          },
          {
            "$id": "nl:24",
            "token": "Claim",
            "properties": [
              {
                "$id": "p:142",
                "token": "id",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:143",
                "token": "content",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:144",
                "token": "type",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:145",
                "token": "confidence",
                "type": {
                  "type": "float"
                },
                "nullable": false
              },
              {
                "$id": "p:146",
                "token": "source",
                "type": {
                  "type": "string"
                },
                "nullable": false
              }
            ]
          },
          {
            "$id": "nl:25",
            "token": "Model",
            "properties": [
              {
                "$id": "p:147",
                "token": "id",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:148",
                "token": "name",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:149",
                "token": "version",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:150",
                "token": "status",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:151",
                "token": "populationValidatedAcross",
                "type": {
                  "type": "string"
                },
                "nullable": false
              }
            ]
          },
          {
            "$id": "nl:26",
            "token": "Group",
            "properties": [
              {
                "$id": "p:152",
                "token": "id",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:153",
                "token": "name",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:154",
                "token": "type",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:155",
                "token": "description",
                "type": {
                  "type": "string"
                },
                "nullable": false
              }
            ]
          },
          {
            "$id": "nl:27",
            "token": "Metric",
            "properties": [
              {
                "$id": "p:156",
                "token": "id",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:157",
                "token": "name",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:158",
                "token": "type",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:159",
                "token": "value",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:160",
                "token": "unit",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:161",
                "token": "burden",
                "type": {
                  "type": "float"
                },
                "nullable": false
              }
            ]
          },
          {
            "$id": "nl:28",
            "token": "Experience",
            "properties": [
              {
                "$id": "p:162",
                "token": "id",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:163",
                "token": "name",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:164",
                "token": "type",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:165",
                "token": "priority",
                "type": {
                  "type": "string"
                },
                "nullable": false
              }
            ]
          },
          {
            "$id": "nl:29",
            "token": "Data",
            "properties": [
              {
                "$id": "p:166",
                "token": "id",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:167",
                "token": "name",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:168",
                "token": "type",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:169",
                "token": "content",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:170",
                "token": "provenanceClass",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:171",
                "token": "lineage",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:172",
                "token": "integrity",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:173",
                "token": "variable",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:174",
                "token": "representation",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:175",
                "token": "statement",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:176",
                "token": "hypothesis",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:177",
                "token": "requirement",
                "type": {
                  "type": "string"
                },
                "nullable": false
              }
            ]
          },
          {
            "$id": "nl:3",
            "token": "Memory",
            "properties": [
              {
                "$id": "p:18",
                "token": "id",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:19",
                "token": "type",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:20",
                "token": "content",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:21",
                "token": "timestamp",
                "type": {
                  "type": "datetime"
                },
                "nullable": false
              },
              {
                "$id": "p:22",
                "token": "epistemicClass",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:23",
                "token": "modelMetadata",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:24",
                "token": "uncertainty",
                "type": {
                  "type": "float"
                },
                "nullable": false
              },
              {
                "$id": "p:25",
                "token": "missingness",
                "type": {
                  "type": "boolean"
                },
                "nullable": false
              },
              {
                "$id": "p:26",
                "token": "consentState",
                "type": {
                  "type": "string"
                },
                "nullable": false
              }
            ]
          },
          {
            "$id": "nl:4",
            "token": "World",
            "properties": [
              {
                "$id": "p:27",
                "token": "id",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:28",
                "token": "name",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:29",
                "token": "type",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:30",
                "token": "description",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:31",
                "token": "state",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:32",
                "token": "accessPolicy",
                "type": {
                  "type": "string"
                },
                "nullable": false
              }
            ]
          },
          {
            "$id": "nl:5",
            "token": "Agent",
            "properties": [
              {
                "$id": "p:33",
                "token": "id",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:34",
                "token": "name",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:35",
                "token": "type",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:36",
                "token": "role",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:37",
                "token": "workflow",
                "type": {
                  "type": "string"
                },
                "nullable": false
              }
            ]
          },
          {
            "$id": "nl:6",
            "token": "Location",
            "properties": [
              {
                "$id": "p:38",
                "token": "id",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:39",
                "token": "name",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:40",
                "token": "coordinates",
                "type": {
                  "type": "point"
                },
                "nullable": false
              },
              {
                "$id": "p:41",
                "token": "type",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:42",
                "token": "description",
                "type": {
                  "type": "string"
                },
                "nullable": false
              }
            ]
          },
          {
            "$id": "nl:7",
            "token": "Knowledge",
            "properties": [
              {
                "$id": "p:43",
                "token": "id",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:44",
                "token": "name",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:45",
                "token": "type",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:46",
                "token": "content",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:47",
                "token": "provenance",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:48",
                "token": "epistemicClass",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:49",
                "token": "evidenceGrade",
                "type": {
                  "type": "string"
                },
                "nullable": false
              }
            ]
          },
          {
            "$id": "nl:8",
            "token": "Asset",
            "properties": [
              {
                "$id": "p:50",
                "token": "id",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:51",
                "token": "name",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:52",
                "token": "type",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:53",
                "token": "format",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:54",
                "token": "content",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:55",
                "token": "ipOwner",
                "type": {
                  "type": "string"
                },
                "nullable": false
              }
            ]
          },
          {
            "$id": "nl:9",
            "token": "Organization",
            "properties": [
              {
                "$id": "p:56",
                "token": "id",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:57",
                "token": "name",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:58",
                "token": "type",
                "type": {
                  "type": "string"
                },
                "nullable": false
              },
              {
                "$id": "p:59",
                "token": "industry",
                "type": {
                  "type": "string"
                },
                "nullable": false
              }
            ]
          }
        ],
        "relationshipTypes": [
          {
            "$id": "rt:1",
            "token": "HAS_PREFERENCE",
            "properties": []
          },
          {
            "$id": "rt:10",
            "token": "INFLUENCES",
            "properties": []
          },
          {
            "$id": "rt:100",
            "token": "IS_AUTHORIZED_BY",
            "properties": []
          },
          {
            "$id": "rt:101",
            "token": "HAS_CONTROL",
            "properties": []
          },
          {
            "$id": "rt:102",
            "token": "LEARNS_PATTERNS_ACROSS",
            "properties": []
          },
          {
            "$id": "rt:103",
            "token": "DECREASES_PROBABILITY",
            "properties": []
          },
          {
            "$id": "rt:104",
            "token": "REQUESTS",
            "properties": []
          },
          {
            "$id": "rt:105",
            "token": "REQUESTS",
            "properties": []
          },
          {
            "$id": "rt:106",
            "token": "ENCOURAGES",
            "properties": []
          },
          {
            "$id": "rt:107",
            "token": "REPORTS",
            "properties": []
          },
          {
            "$id": "rt:108",
            "token": "REJECTS",
            "properties": []
          },
          {
            "$id": "rt:109",
            "token": "TARGETS",
            "properties": []
          },
          {
            "$id": "rt:11",
            "token": "CAPTURES",
            "properties": []
          },
          {
            "$id": "rt:110",
            "token": "LABELS",
            "properties": []
          },
          {
            "$id": "rt:111",
            "token": "INFERS",
            "properties": []
          },
          {
            "$id": "rt:112",
            "token": "EXCLUDES",
            "properties": []
          },
          {
            "$id": "rt:113",
            "token": "FORCES",
            "properties": []
          },
          {
            "$id": "rt:114",
            "token": "HAS_CONSENT",
            "properties": []
          },
          {
            "$id": "rt:115",
            "token": "SUSPENDS",
            "properties": []
          },
          {
            "$id": "rt:116",
            "token": "SUSPENDS",
            "properties": []
          },
          {
            "$id": "rt:117",
            "token": "ADDS",
            "properties": []
          },
          {
            "$id": "rt:118",
            "token": "REMOVES_FROM",
            "properties": []
          },
          {
            "$id": "rt:119",
            "token": "ISSUES",
            "properties": []
          },
          {
            "$id": "rt:12",
            "token": "PROVIDES",
            "properties": []
          },
          {
            "$id": "rt:120",
            "token": "NOTIFIES",
            "properties": []
          },
          {
            "$id": "rt:121",
            "token": "DISTINGUISHES",
            "properties": []
          },
          {
            "$id": "rt:122",
            "token": "RETAINS",
            "properties": []
          },
          {
            "$id": "rt:123",
            "token": "USES",
            "properties": []
          },
          {
            "$id": "rt:124",
            "token": "RELEVANT_TO",
            "properties": []
          },
          {
            "$id": "rt:125",
            "token": "IS_REPRESENTATION_OF",
            "properties": []
          },
          {
            "$id": "rt:126",
            "token": "NOTIFIES_DOWNSTREAM",
            "properties": []
          },
          {
            "$id": "rt:127",
            "token": "INVALIDATES",
            "properties": []
          },
          {
            "$id": "rt:128",
            "token": "HAS_UNCERTAINTY",
            "properties": []
          },
          {
            "$id": "rt:129",
            "token": "HAS_MISSINGNESS",
            "properties": []
          },
          {
            "$id": "rt:13",
            "token": "PROVIDES",
            "properties": []
          },
          {
            "$id": "rt:130",
            "token": "MAPS_TO",
            "properties": []
          },
          {
            "$id": "rt:131",
            "token": "HAS_METRIC",
            "properties": []
          },
          {
            "$id": "rt:132",
            "token": "HAS_METRIC",
            "properties": []
          },
          {
            "$id": "rt:133",
            "token": "HAS_METRIC",
            "properties": []
          },
          {
            "$id": "rt:134",
            "token": "HAS_TRANSITION",
            "properties": []
          },
          {
            "$id": "rt:135",
            "token": "SEPARATES",
            "properties": []
          },
          {
            "$id": "rt:136",
            "token": "REDUCES",
            "properties": []
          },
          {
            "$id": "rt:137",
            "token": "CHECKS",
            "properties": []
          },
          {
            "$id": "rt:138",
            "token": "CONSIDERS",
            "properties": []
          },
          {
            "$id": "rt:139",
            "token": "AVOIDS",
            "properties": []
          },
          {
            "$id": "rt:14",
            "token": "PROVIDES",
            "properties": []
          },
          {
            "$id": "rt:140",
            "token": "DECAYS",
            "properties": []
          },
          {
            "$id": "rt:141",
            "token": "RECORDS_COMPLETION",
            "properties": []
          },
          {
            "$id": "rt:15",
            "token": "PROVIDES",
            "properties": []
          },
          {
            "$id": "rt:16",
            "token": "OWNS",
            "properties": []
          },
          {
            "$id": "rt:17",
            "token": "OWNS",
            "properties": []
          },
          {
            "$id": "rt:18",
            "token": "ACCESSES",
            "properties": []
          },
          {
            "$id": "rt:19",
            "token": "ACCESSES",
            "properties": []
          },
          {
            "$id": "rt:2",
            "token": "HAS_GOAL",
            "properties": []
          },
          {
            "$id": "rt:20",
            "token": "ACCESSES",
            "properties": []
          },
          {
            "$id": "rt:21",
            "token": "GRANTS",
            "properties": []
          },
          {
            "$id": "rt:22",
            "token": "GRANTS",
            "properties": []
          },
          {
            "$id": "rt:23",
            "token": "DEFINES",
            "properties": []
          },
          {
            "$id": "rt:24",
            "token": "DEFINES",
            "properties": []
          },
          {
            "$id": "rt:25",
            "token": "DEFINES",
            "properties": []
          },
          {
            "$id": "rt:26",
            "token": "CONTAINS",
            "properties": []
          },
          {
            "$id": "rt:27",
            "token": "CONTAINS",
            "properties": []
          },
          {
            "$id": "rt:28",
            "token": "CONTAINS",
            "properties": []
          },
          {
            "$id": "rt:29",
            "token": "CONTAINS",
            "properties": []
          },
          {
            "$id": "rt:3",
            "token": "GENERATES",
            "properties": []
          },
          {
            "$id": "rt:30",
            "token": "PARTICIPATES_IN",
            "properties": []
          },
          {
            "$id": "rt:31",
            "token": "PARTICIPATES_IN",
            "properties": []
          },
          {
            "$id": "rt:32",
            "token": "PARTICIPATES_IN",
            "properties": []
          },
          {
            "$id": "rt:33",
            "token": "INITIATES",
            "properties": []
          },
          {
            "$id": "rt:34",
            "token": "UPDATES",
            "properties": []
          },
          {
            "$id": "rt:35",
            "token": "UPDATES",
            "properties": []
          },
          {
            "$id": "rt:36",
            "token": "UPDATES",
            "properties": []
          },
          {
            "$id": "rt:37",
            "token": "UPDATES",
            "properties": []
          },
          {
            "$id": "rt:38",
            "token": "REQUIRES",
            "properties": []
          },
          {
            "$id": "rt:39",
            "token": "REQUIRES",
            "properties": []
          },
          {
            "$id": "rt:4",
            "token": "GENERATES",
            "properties": []
          },
          {
            "$id": "rt:40",
            "token": "REQUIRES",
            "properties": []
          },
          {
            "$id": "rt:41",
            "token": "REQUIRES",
            "properties": []
          },
          {
            "$id": "rt:42",
            "token": "REQUIRES",
            "properties": []
          },
          {
            "$id": "rt:43",
            "token": "MONITORS",
            "properties": []
          },
          {
            "$id": "rt:44",
            "token": "ESCALATES_TO",
            "properties": []
          },
          {
            "$id": "rt:45",
            "token": "ESCALATES_TO",
            "properties": []
          },
          {
            "$id": "rt:46",
            "token": "CONTRIBUTES_TO",
            "properties": []
          },
          {
            "$id": "rt:47",
            "token": "PURCHASES",
            "properties": []
          },
          {
            "$id": "rt:48",
            "token": "LICENSES",
            "properties": []
          },
          {
            "$id": "rt:49",
            "token": "LICENSES",
            "properties": []
          },
          {
            "$id": "rt:5",
            "token": "GENERATES",
            "properties": []
          },
          {
            "$id": "rt:50",
            "token": "HAS_STATE",
            "properties": []
          },
          {
            "$id": "rt:51",
            "token": "HAS_STATE",
            "properties": []
          },
          {
            "$id": "rt:52",
            "token": "IS_PART_OF",
            "properties": []
          },
          {
            "$id": "rt:53",
            "token": "IS_PART_OF",
            "properties": []
          },
          {
            "$id": "rt:54",
            "token": "REFERENCES",
            "properties": []
          },
          {
            "$id": "rt:55",
            "token": "REFERENCES",
            "properties": []
          },
          {
            "$id": "rt:56",
            "token": "REFERENCES",
            "properties": []
          },
          {
            "$id": "rt:57",
            "token": "REFERENCES",
            "properties": []
          },
          {
            "$id": "rt:58",
            "token": "APPLIES_TO",
            "properties": []
          },
          {
            "$id": "rt:59",
            "token": "APPLIES_TO",
            "properties": []
          },
          {
            "$id": "rt:6",
            "token": "GENERATES",
            "properties": []
          },
          {
            "$id": "rt:60",
            "token": "APPLIES_TO",
            "properties": []
          },
          {
            "$id": "rt:61",
            "token": "APPLIES_TO",
            "properties": []
          },
          {
            "$id": "rt:62",
            "token": "APPLIES_TO",
            "properties": []
          },
          {
            "$id": "rt:63",
            "token": "APPLIES_TO",
            "properties": []
          },
          {
            "$id": "rt:64",
            "token": "RECEIVES",
            "properties": []
          },
          {
            "$id": "rt:65",
            "token": "RECEIVES",
            "properties": []
          },
          {
            "$id": "rt:66",
            "token": "RECEIVES",
            "properties": []
          },
          {
            "$id": "rt:67",
            "token": "GENERATES",
            "properties": []
          },
          {
            "$id": "rt:68",
            "token": "GENERATES",
            "properties": []
          },
          {
            "$id": "rt:69",
            "token": "INTERPRETS",
            "properties": []
          },
          {
            "$id": "rt:7",
            "token": "INFLUENCES",
            "properties": []
          },
          {
            "$id": "rt:70",
            "token": "INTERPRETS",
            "properties": []
          },
          {
            "$id": "rt:71",
            "token": "HAS_PERMISSION",
            "properties": []
          },
          {
            "$id": "rt:72",
            "token": "HAS_PERMISSION",
            "properties": []
          },
          {
            "$id": "rt:73",
            "token": "HAS_PERMISSION",
            "properties": []
          },
          {
            "$id": "rt:74",
            "token": "HAS_DEPENDENCY",
            "properties": []
          },
          {
            "$id": "rt:75",
            "token": "BLOCKS",
            "properties": []
          },
          {
            "$id": "rt:76",
            "token": "OPTIMIZES",
            "properties": []
          },
          {
            "$id": "rt:77",
            "token": "OPTIMIZES",
            "properties": []
          },
          {
            "$id": "rt:78",
            "token": "COINCIDES_WITH",
            "properties": []
          },
          {
            "$id": "rt:79",
            "token": "PRESERVES",
            "properties": []
          },
          {
            "$id": "rt:8",
            "token": "INFLUENCES",
            "properties": []
          },
          {
            "$id": "rt:80",
            "token": "PRESERVES",
            "properties": []
          },
          {
            "$id": "rt:81",
            "token": "PRESERVES",
            "properties": []
          },
          {
            "$id": "rt:82",
            "token": "VALIDATED_ACROSS",
            "properties": []
          },
          {
            "$id": "rt:83",
            "token": "IMPLEMENTS",
            "properties": []
          },
          {
            "$id": "rt:84",
            "token": "IMPLEMENTS",
            "properties": []
          },
          {
            "$id": "rt:85",
            "token": "IMPLEMENTS",
            "properties": []
          },
          {
            "$id": "rt:86",
            "token": "HAS_CONTEXT",
            "properties": []
          },
          {
            "$id": "rt:87",
            "token": "HAS_CLAIM",
            "properties": []
          },
          {
            "$id": "rt:88",
            "token": "HAS_CONSTRAINT",
            "properties": []
          },
          {
            "$id": "rt:89",
            "token": "HAS_CULTURAL_CONTEXT",
            "properties": []
          },
          {
            "$id": "rt:9",
            "token": "INFLUENCES",
            "properties": []
          },
          {
            "$id": "rt:90",
            "token": "HAS_METRIC",
            "properties": []
          },
          {
            "$id": "rt:91",
            "token": "HAS_IMPACT",
            "properties": []
          },
          {
            "$id": "rt:92",
            "token": "CONTROLS",
            "properties": []
          },
          {
            "$id": "rt:93",
            "token": "EXPORTS",
            "properties": []
          },
          {
            "$id": "rt:94",
            "token": "DISPUTES",
            "properties": []
          },
          {
            "$id": "rt:95",
            "token": "RESETS",
            "properties": []
          },
          {
            "$id": "rt:96",
            "token": "DELETES",
            "properties": []
          },
          {
            "$id": "rt:97",
            "token": "DELETES",
            "properties": []
          },
          {
            "$id": "rt:98",
            "token": "REVOKES",
            "properties": []
          },
          {
            "$id": "rt:99",
            "token": "RELATES_TO",
            "properties": []
          }
        ],
        "nodeObjectTypes": [
          {
            "$id": "n:1",
            "labels": [
              {
                "$ref": "#nl:1"
              }
            ]
          },
          {
            "$id": "n:2",
            "labels": [
              {
                "$ref": "#nl:2"
              }
            ]
          },
          {
            "$id": "n:3",
            "labels": [
              {
                "$ref": "#nl:3"
              }
            ]
          },
          {
            "$id": "n:4",
            "labels": [
              {
                "$ref": "#nl:4"
              }
            ]
          },
          {
            "$id": "n:5",
            "labels": [
              {
                "$ref": "#nl:5"
              }
            ]
          },
          {
            "$id": "n:6",
            "labels": [
              {
                "$ref": "#nl:6"
              }
            ]
          },
          {
            "$id": "n:7",
            "labels": [
              {
                "$ref": "#nl:7"
              }
            ]
          },
          {
            "$id": "n:8",
            "labels": [
              {
                "$ref": "#nl:8"
              }
            ]
          },
          {
            "$id": "n:9",
            "labels": [
              {
                "$ref": "#nl:9"
              }
            ]
          },
          {
            "$id": "n:10",
            "labels": [
              {
                "$ref": "#nl:10"
              }
            ]
          },
          {
            "$id": "n:11",
            "labels": [
              {
                "$ref": "#nl:11"
              }
            ]
          },
          {
            "$id": "n:12",
            "labels": [
              {
                "$ref": "#nl:12"
              }
            ]
          },
          {
            "$id": "n:13",
            "labels": [
              {
                "$ref": "#nl:13"
              }
            ]
          },
          {
            "$id": "n:14",
            "labels": [
              {
                "$ref": "#nl:14"
              }
            ]
          },
          {
            "$id": "n:15",
            "labels": [
              {
                "$ref": "#nl:15"
              }
            ]
          },
          {
            "$id": "n:16",
            "labels": [
              {
                "$ref": "#nl:16"
              }
            ]
          },
          {
            "$id": "n:17",
            "labels": [
              {
                "$ref": "#nl:17"
              }
            ]
          },
          {
            "$id": "n:18",
            "labels": [
              {
                "$ref": "#nl:18"
              }
            ]
          },
          {
            "$id": "n:19",
            "labels": [
              {
                "$ref": "#nl:19"
              }
            ]
          },
          {
            "$id": "n:20",
            "labels": [
              {
                "$ref": "#nl:20"
              }
            ]
          },
          {
            "$id": "n:21",
            "labels": [
              {
                "$ref": "#nl:21"
              }
            ]
          },
          {
            "$id": "n:22",
            "labels": [
              {
                "$ref": "#nl:22"
              }
            ]
          },
          {
            "$id": "n:23",
            "labels": [
              {
                "$ref": "#nl:23"
              }
            ]
          },
          {
            "$id": "n:24",
            "labels": [
              {
                "$ref": "#nl:24"
              }
            ]
          },
          {
            "$id": "n:25",
            "labels": [
              {
                "$ref": "#nl:25"
              }
            ]
          },
          {
            "$id": "n:26",
            "labels": [
              {
                "$ref": "#nl:26"
              }
            ]
          },
          {
            "$id": "n:27",
            "labels": [
              {
                "$ref": "#nl:27"
              }
            ]
          },
          {
            "$id": "n:28",
            "labels": [
              {
                "$ref": "#nl:28"
              }
            ]
          },
          {
            "$id": "n:29",
            "labels": [
              {
                "$ref": "#nl:29"
              }
            ]
          }
        ],
        "relationshipObjectTypes": [
          {
            "$id": "r:1",
            "type": {
              "$ref": "#rt:1"
            },
            "from": {
              "$ref": "#n:1"
            },
            "to": {
              "$ref": "#n:3"
            }
          },
          {
            "$id": "r:2",
            "type": {
              "$ref": "#rt:2"
            },
            "from": {
              "$ref": "#n:1"
            },
            "to": {
              "$ref": "#n:23"
            }
          },
          {
            "$id": "r:3",
            "type": {
              "$ref": "#rt:3"
            },
            "from": {
              "$ref": "#n:5"
            },
            "to": {
              "$ref": "#n:19"
            }
          },
          {
            "$id": "r:4",
            "type": {
              "$ref": "#rt:4"
            },
            "from": {
              "$ref": "#n:5"
            },
            "to": {
              "$ref": "#n:20"
            }
          },
          {
            "$id": "r:5",
            "type": {
              "$ref": "#rt:5"
            },
            "from": {
              "$ref": "#n:16"
            },
            "to": {
              "$ref": "#n:29"
            }
          },
          {
            "$id": "r:6",
            "type": {
              "$ref": "#rt:6"
            },
            "from": {
              "$ref": "#n:2"
            },
            "to": {
              "$ref": "#n:3"
            }
          },
          {
            "$id": "r:7",
            "type": {
              "$ref": "#rt:7"
            },
            "from": {
              "$ref": "#n:2"
            },
            "to": {
              "$ref": "#n:5"
            }
          },
          {
            "$id": "r:8",
            "type": {
              "$ref": "#rt:8"
            },
            "from": {
              "$ref": "#n:2"
            },
            "to": {
              "$ref": "#n:3"
            }
          },
          {
            "$id": "r:9",
            "type": {
              "$ref": "#rt:9"
            },
            "from": {
              "$ref": "#n:29"
            },
            "to": {
              "$ref": "#n:13"
            }
          },
          {
            "$id": "r:10",
            "type": {
              "$ref": "#rt:10"
            },
            "from": {
              "$ref": "#n:22"
            },
            "to": {
              "$ref": "#n:13"
            }
          },
          {
            "$id": "r:11",
            "type": {
              "$ref": "#rt:11"
            },
            "from": {
              "$ref": "#n:16"
            },
            "to": {
              "$ref": "#n:2"
            }
          },
          {
            "$id": "r:12",
            "type": {
              "$ref": "#rt:12"
            },
            "from": {
              "$ref": "#n:1"
            },
            "to": {
              "$ref": "#n:8"
            }
          },
          {
            "$id": "r:13",
            "type": {
              "$ref": "#rt:13"
            },
            "from": {
              "$ref": "#n:9"
            },
            "to": {
              "$ref": "#n:11"
            }
          },
          {
            "$id": "r:14",
            "type": {
              "$ref": "#rt:14"
            },
            "from": {
              "$ref": "#n:16"
            },
            "to": {
              "$ref": "#n:29"
            }
          },
          {
            "$id": "r:15",
            "type": {
              "$ref": "#rt:15"
            },
            "from": {
              "$ref": "#n:1"
            },
            "to": {
              "$ref": "#n:7"
            }
          },
          {
            "$id": "r:16",
            "type": {
              "$ref": "#rt:16"
            },
            "from": {
              "$ref": "#n:1"
            },
            "to": {
              "$ref": "#n:4"
            }
          },
          {
            "$id": "r:17",
            "type": {
              "$ref": "#rt:17"
            },
            "from": {
              "$ref": "#n:1"
            },
            "to": {
              "$ref": "#n:8"
            }
          },
          {
            "$id": "r:18",
            "type": {
              "$ref": "#rt:18"
            },
            "from": {
              "$ref": "#n:1"
            },
            "to": {
              "$ref": "#n:4"
            }
          },
          {
            "$id": "r:19",
            "type": {
              "$ref": "#rt:19"
            },
            "from": {
              "$ref": "#n:5"
            },
            "to": {
              "$ref": "#n:3"
            }
          },
          {
            "$id": "r:20",
            "type": {
              "$ref": "#rt:20"
            },
            "from": {
              "$ref": "#n:16"
            },
            "to": {
              "$ref": "#n:29"
            }
          },
          {
            "$id": "r:21",
            "type": {
              "$ref": "#rt:21"
            },
            "from": {
              "$ref": "#n:18"
            },
            "to": {
              "$ref": "#n:21"
            }
          },
          {
            "$id": "r:22",
            "type": {
              "$ref": "#rt:22"
            },
            "from": {
              "$ref": "#n:1"
            },
            "to": {
              "$ref": "#n:21"
            }
          },
          {
            "$id": "r:23",
            "type": {
              "$ref": "#rt:23"
            },
            "from": {
              "$ref": "#n:18"
            },
            "to": {
              "$ref": "#n:14"
            }
          },
          {
            "$id": "r:24",
            "type": {
              "$ref": "#rt:24"
            },
            "from": {
              "$ref": "#n:15"
            },
            "to": {
              "$ref": "#n:14"
            }
          },
          {
            "$id": "r:25",
            "type": {
              "$ref": "#rt:25"
            },
            "from": {
              "$ref": "#n:14"
            },
            "to": {
              "$ref": "#n:22"
            }
          },
          {
            "$id": "r:26",
            "type": {
              "$ref": "#rt:26"
            },
            "from": {
              "$ref": "#n:4"
            },
            "to": {
              "$ref": "#n:6"
            }
          },
          {
            "$id": "r:27",
            "type": {
              "$ref": "#rt:27"
            },
            "from": {
              "$ref": "#n:4"
            },
            "to": {
              "$ref": "#n:5"
            }
          },
          {
            "$id": "r:28",
            "type": {
              "$ref": "#rt:28"
            },
            "from": {
              "$ref": "#n:4"
            },
            "to": {
              "$ref": "#n:8"
            }
          },
          {
            "$id": "r:29",
            "type": {
              "$ref": "#rt:29"
            },
            "from": {
              "$ref": "#n:26"
            },
            "to": {
              "$ref": "#n:1"
            }
          },
          {
            "$id": "r:30",
            "type": {
              "$ref": "#rt:30"
            },
            "from": {
              "$ref": "#n:1"
            },
            "to": {
              "$ref": "#n:4"
            }
          },
          {
            "$id": "r:31",
            "type": {
              "$ref": "#rt:31"
            },
            "from": {
              "$ref": "#n:1"
            },
            "to": {
              "$ref": "#n:12"
            }
          },
          {
            "$id": "r:32",
            "type": {
              "$ref": "#rt:32"
            },
            "from": {
              "$ref": "#n:1"
            },
            "to": {
              "$ref": "#n:26"
            }
          },
          {
            "$id": "r:33",
            "type": {
              "$ref": "#rt:33"
            },
            "from": {
              "$ref": "#n:1"
            },
            "to": {
              "$ref": "#n:13"
            }
          },
          {
            "$id": "r:34",
            "type": {
              "$ref": "#rt:34"
            },
            "from": {
              "$ref": "#n:5"
            },
            "to": {
              "$ref": "#n:3"
            }
          },
          {
            "$id": "r:35",
            "type": {
              "$ref": "#rt:35"
            },
            "from": {
              "$ref": "#n:13"
            },
            "to": {
              "$ref": "#n:4"
            }
          },
          {
            "$id": "r:36",
            "type": {
              "$ref": "#rt:36"
            },
            "from": {
              "$ref": "#n:16"
            },
            "to": {
              "$ref": "#n:25"
            }
          },
          {
            "$id": "r:37",
            "type": {
              "$ref": "#rt:37"
            },
            "from": {
              "$ref": "#n:18"
            },
            "to": {
              "$ref": "#n:29"
            }
          },
          {
            "$id": "r:38",
            "type": {
              "$ref": "#rt:38"
            },
            "from": {
              "$ref": "#n:12"
            },
            "to": {
              "$ref": "#n:22"
            }
          },
          {
            "$id": "r:39",
            "type": {
              "$ref": "#rt:39"
            },
            "from": {
              "$ref": "#n:5"
            },
            "to": {
              "$ref": "#n:21"
            }
          },
          {
            "$id": "r:40",
            "type": {
              "$ref": "#rt:40"
            },
            "from": {
              "$ref": "#n:13"
            },
            "to": {
              "$ref": "#n:1"
            }
          },
          {
            "$id": "r:41",
            "type": {
              "$ref": "#rt:41"
            },
            "from": {
              "$ref": "#n:13"
            },
            "to": {
              "$ref": "#n:7"
            }
          },
          {
            "$id": "r:42",
            "type": {
              "$ref": "#rt:42"
            },
            "from": {
              "$ref": "#n:14"
            },
            "to": {
              "$ref": "#n:16"
            }
          },
          {
            "$id": "r:43",
            "type": {
              "$ref": "#rt:43"
            },
            "from": {
              "$ref": "#n:16"
            },
            "to": {
              "$ref": "#n:12"
            }
          },
          {
            "$id": "r:44",
            "type": {
              "$ref": "#rt:44"
            },
            "from": {
              "$ref": "#n:5"
            },
            "to": {
              "$ref": "#n:18"
            }
          },
          {
            "$id": "r:45",
            "type": {
              "$ref": "#rt:45"
            },
            "from": {
              "$ref": "#n:16"
            },
            "to": {
              "$ref": "#n:18"
            }
          },
          {
            "$id": "r:46",
            "type": {
              "$ref": "#rt:46"
            },
            "from": {
              "$ref": "#n:1"
            },
            "to": {
              "$ref": "#n:10"
            }
          },
          {
            "$id": "r:47",
            "type": {
              "$ref": "#rt:47"
            },
            "from": {
              "$ref": "#n:1"
            },
            "to": {
              "$ref": "#n:11"
            }
          },
          {
            "$id": "r:48",
            "type": {
              "$ref": "#rt:48"
            },
            "from": {
              "$ref": "#n:1"
            },
            "to": {
              "$ref": "#n:8"
            }
          },
          {
            "$id": "r:49",
            "type": {
              "$ref": "#rt:49"
            },
            "from": {
              "$ref": "#n:9"
            },
            "to": {
              "$ref": "#n:8"
            }
          },
          {
            "$id": "r:50",
            "type": {
              "$ref": "#rt:50"
            },
            "from": {
              "$ref": "#n:4"
            },
            "to": {
              "$ref": "#n:29"
            }
          },
          {
            "$id": "r:51",
            "type": {
              "$ref": "#rt:51"
            },
            "from": {
              "$ref": "#n:13"
            },
            "to": {
              "$ref": "#n:29"
            }
          },
          {
            "$id": "r:52",
            "type": {
              "$ref": "#rt:52"
            },
            "from": {
              "$ref": "#n:16"
            },
            "to": {
              "$ref": "#n:16"
            }
          },
          {
            "$id": "r:53",
            "type": {
              "$ref": "#rt:53"
            },
            "from": {
              "$ref": "#n:8"
            },
            "to": {
              "$ref": "#n:11"
            }
          },
          {
            "$id": "r:54",
            "type": {
              "$ref": "#rt:54"
            },
            "from": {
              "$ref": "#n:12"
            },
            "to": {
              "$ref": "#n:7"
            }
          },
          {
            "$id": "r:55",
            "type": {
              "$ref": "#rt:55"
            },
            "from": {
              "$ref": "#n:3"
            },
            "to": {
              "$ref": "#n:7"
            }
          },
          {
            "$id": "r:56",
            "type": {
              "$ref": "#rt:56"
            },
            "from": {
              "$ref": "#n:13"
            },
            "to": {
              "$ref": "#n:29"
            }
          },
          {
            "$id": "r:57",
            "type": {
              "$ref": "#rt:57"
            },
            "from": {
              "$ref": "#n:24"
            },
            "to": {
              "$ref": "#n:29"
            }
          },
          {
            "$id": "r:58",
            "type": {
              "$ref": "#rt:58"
            },
            "from": {
              "$ref": "#n:14"
            },
            "to": {
              "$ref": "#n:16"
            }
          },
          {
            "$id": "r:59",
            "type": {
              "$ref": "#rt:59"
            },
            "from": {
              "$ref": "#n:17"
            },
            "to": {
              "$ref": "#n:29"
            }
          },
          {
            "$id": "r:60",
            "type": {
              "$ref": "#rt:60"
            },
            "from": {
              "$ref": "#n:17"
            },
            "to": {
              "$ref": "#n:1"
            }
          },
          {
            "$id": "r:61",
            "type": {
              "$ref": "#rt:61"
            },
            "from": {
              "$ref": "#n:18"
            },
            "to": {
              "$ref": "#n:29"
            }
          },
          {
            "$id": "r:62",
            "type": {
              "$ref": "#rt:62"
            },
            "from": {
              "$ref": "#n:18"
            },
            "to": {
              "$ref": "#n:13"
            }
          },
          {
            "$id": "r:63",
            "type": {
              "$ref": "#rt:63"
            },
            "from": {
              "$ref": "#n:18"
            },
            "to": {
              "$ref": "#n:16"
            }
          },
          {
            "$id": "r:64",
            "type": {
              "$ref": "#rt:64"
            },
            "from": {
              "$ref": "#n:5"
            },
            "to": {
              "$ref": "#n:2"
            }
          },
          {
            "$id": "r:65",
            "type": {
              "$ref": "#rt:65"
            },
            "from": {
              "$ref": "#n:1"
            },
            "to": {
              "$ref": "#n:20"
            }
          },
          {
            "$id": "r:66",
            "type": {
              "$ref": "#rt:66"
            },
            "from": {
              "$ref": "#n:16"
            },
            "to": {
              "$ref": "#n:29"
            }
          },
          {
            "$id": "r:67",
            "type": {
              "$ref": "#rt:67"
            },
            "from": {
              "$ref": "#n:5"
            },
            "to": {
              "$ref": "#n:2"
            }
          },
          {
            "$id": "r:68",
            "type": {
              "$ref": "#rt:68"
            },
            "from": {
              "$ref": "#n:16"
            },
            "to": {
              "$ref": "#n:2"
            }
          },
          {
            "$id": "r:69",
            "type": {
              "$ref": "#rt:69"
            },
            "from": {
              "$ref": "#n:5"
            },
            "to": {
              "$ref": "#n:2"
            }
          },
          {
            "$id": "r:70",
            "type": {
              "$ref": "#rt:70"
            },
            "from": {
              "$ref": "#n:5"
            },
            "to": {
              "$ref": "#n:3"
            }
          },
          {
            "$id": "r:71",
            "type": {
              "$ref": "#rt:71"
            },
            "from": {
              "$ref": "#n:1"
            },
            "to": {
              "$ref": "#n:21"
            }
          },
          {
            "$id": "r:72",
            "type": {
              "$ref": "#rt:72"
            },
            "from": {
              "$ref": "#n:5"
            },
            "to": {
              "$ref": "#n:21"
            }
          },
          {
            "$id": "r:73",
            "type": {
              "$ref": "#rt:73"
            },
            "from": {
              "$ref": "#n:3"
            },
            "to": {
              "$ref": "#n:21"
            }
          },
          {
            "$id": "r:74",
            "type": {
              "$ref": "#rt:74"
            },
            "from": {
              "$ref": "#n:16"
            },
            "to": {
              "$ref": "#n:16"
            }
          },
          {
            "$id": "r:75",
            "type": {
              "$ref": "#rt:75"
            },
            "from": {
              "$ref": "#n:16"
            },
            "to": {
              "$ref": "#n:16"
            }
          },
          {
            "$id": "r:76",
            "type": {
              "$ref": "#rt:76"
            },
            "from": {
              "$ref": "#n:11"
            },
            "to": {
              "$ref": "#n:13"
            }
          },
          {
            "$id": "r:77",
            "type": {
              "$ref": "#rt:77"
            },
            "from": {
              "$ref": "#n:11"
            },
            "to": {
              "$ref": "#n:1"
            }
          },
          {
            "$id": "r:78",
            "type": {
              "$ref": "#rt:78"
            },
            "from": {
              "$ref": "#n:13"
            },
            "to": {
              "$ref": "#n:13"
            }
          },
          {
            "$id": "r:79",
            "type": {
              "$ref": "#rt:79"
            },
            "from": {
              "$ref": "#n:3"
            },
            "to": {
              "$ref": "#n:7"
            }
          },
          {
            "$id": "r:80",
            "type": {
              "$ref": "#rt:80"
            },
            "from": {
              "$ref": "#n:16"
            },
            "to": {
              "$ref": "#n:1"
            }
          },
          {
            "$id": "r:81",
            "type": {
              "$ref": "#rt:81"
            },
            "from": {
              "$ref": "#n:16"
            },
            "to": {
              "$ref": "#n:29"
            }
          },
          {
            "$id": "r:82",
            "type": {
              "$ref": "#rt:82"
            },
            "from": {
              "$ref": "#n:25"
            },
            "to": {
              "$ref": "#n:26"
            }
          },
          {
            "$id": "r:83",
            "type": {
              "$ref": "#rt:83"
            },
            "from": {
              "$ref": "#n:16"
            },
            "to": {
              "$ref": "#n:15"
            }
          },
          {
            "$id": "r:84",
            "type": {
              "$ref": "#rt:84"
            },
            "from": {
              "$ref": "#n:16"
            },
            "to": {
              "$ref": "#n:25"
            }
          },
          {
            "$id": "r:85",
            "type": {
              "$ref": "#rt:85"
            },
            "from": {
              "$ref": "#n:16"
            },
            "to": {
              "$ref": "#n:1"
            }
          },
          {
            "$id": "r:86",
            "type": {
              "$ref": "#rt:86"
            },
            "from": {
              "$ref": "#n:12"
            },
            "to": {
              "$ref": "#n:22"
            }
          },
          {
            "$id": "r:87",
            "type": {
              "$ref": "#rt:87"
            },
            "from": {
              "$ref": "#n:12"
            },
            "to": {
              "$ref": "#n:24"
            }
          },
          {
            "$id": "r:88",
            "type": {
              "$ref": "#rt:88"
            },
            "from": {
              "$ref": "#n:12"
            },
            "to": {
              "$ref": "#n:17"
            }
          },
          {
            "$id": "r:89",
            "type": {
              "$ref": "#rt:89"
            },
            "from": {
              "$ref": "#n:12"
            },
            "to": {
              "$ref": "#n:7"
            }
          },
          {
            "$id": "r:90",
            "type": {
              "$ref": "#rt:90"
            },
            "from": {
              "$ref": "#n:12"
            },
            "to": {
              "$ref": "#n:27"
            }
          },
          {
            "$id": "r:91",
            "type": {
              "$ref": "#rt:91"
            },
            "from": {
              "$ref": "#n:13"
            },
            "to": {
              "$ref": "#n:13"
            }
          },
          {
            "$id": "r:92",
            "type": {
              "$ref": "#rt:92"
            },
            "from": {
              "$ref": "#n:1"
            },
            "to": {
              "$ref": "#n:21"
            }
          },
          {
            "$id": "r:93",
            "type": {
              "$ref": "#rt:93"
            },
            "from": {
              "$ref": "#n:1"
            },
            "to": {
              "$ref": "#n:29"
            }
          },
          {
            "$id": "r:94",
            "type": {
              "$ref": "#rt:94"
            },
            "from": {
              "$ref": "#n:1"
            },
            "to": {
              "$ref": "#n:19"
            }
          },
          {
            "$id": "r:95",
            "type": {
              "$ref": "#rt:95"
            },
            "from": {
              "$ref": "#n:1"
            },
            "to": {
              "$ref": "#n:3"
            }
          },
          {
            "$id": "r:96",
            "type": {
              "$ref": "#rt:96"
            },
            "from": {
              "$ref": "#n:1"
            },
            "to": {
              "$ref": "#n:13"
            }
          },
          {
            "$id": "r:97",
            "type": {
              "$ref": "#rt:97"
            },
            "from": {
              "$ref": "#n:18"
            },
            "to": {
              "$ref": "#n:29"
            }
          },
          {
            "$id": "r:98",
            "type": {
              "$ref": "#rt:98"
            },
            "from": {
              "$ref": "#n:1"
            },
            "to": {
              "$ref": "#n:21"
            }
          },
          {
            "$id": "r:99",
            "type": {
              "$ref": "#rt:99"
            },
            "from": {
              "$ref": "#n:1"
            },
            "to": {
              "$ref": "#n:1"
            }
          },
          {
            "$id": "r:100",
            "type": {
              "$ref": "#rt:100"
            },
            "from": {
              "$ref": "#n:8"
            },
            "to": {
              "$ref": "#n:1"
            }
          },
          {
            "$id": "r:101",
            "type": {
              "$ref": "#rt:101"
            },
            "from": {
              "$ref": "#n:18"
            },
            "to": {
              "$ref": "#n:16"
            }
          },
          {
            "$id": "r:102",
            "type": {
              "$ref": "#rt:102"
            },
            "from": {
              "$ref": "#n:16"
            },
            "to": {
              "$ref": "#n:22"
            }
          },
          {
            "$id": "r:103",
            "type": {
              "$ref": "#rt:103"
            },
            "from": {
              "$ref": "#n:20"
            },
            "to": {
              "$ref": "#n:20"
            }
          },
          {
            "$id": "r:104",
            "type": {
              "$ref": "#rt:104"
            },
            "from": {
              "$ref": "#n:1"
            },
            "to": {
              "$ref": "#n:20"
            }
          },
          {
            "$id": "r:105",
            "type": {
              "$ref": "#rt:105"
            },
            "from": {
              "$ref": "#n:1"
            },
            "to": {
              "$ref": "#n:19"
            }
          },
          {
            "$id": "r:106",
            "type": {
              "$ref": "#rt:106"
            },
            "from": {
              "$ref": "#n:19"
            },
            "to": {
              "$ref": "#n:13"
            }
          },
          {
            "$id": "r:107",
            "type": {
              "$ref": "#rt:107"
            },
            "from": {
              "$ref": "#n:1"
            },
            "to": {
              "$ref": "#n:13"
            }
          },
          {
            "$id": "r:108",
            "type": {
              "$ref": "#rt:108"
            },
            "from": {
              "$ref": "#n:1"
            },
            "to": {
              "$ref": "#n:19"
            }
          },
          {
            "$id": "r:109",
            "type": {
              "$ref": "#rt:109"
            },
            "from": {
              "$ref": "#n:17"
            },
            "to": {
              "$ref": "#n:1"
            }
          },
          {
            "$id": "r:110",
            "type": {
              "$ref": "#rt:110"
            },
            "from": {
              "$ref": "#n:17"
            },
            "to": {
              "$ref": "#n:1"
            }
          },
          {
            "$id": "r:111",
            "type": {
              "$ref": "#rt:111"
            },
            "from": {
              "$ref": "#n:17"
            },
            "to": {
              "$ref": "#n:29"
            }
          },
          {
            "$id": "r:112",
            "type": {
              "$ref": "#rt:112"
            },
            "from": {
              "$ref": "#n:17"
            },
            "to": {
              "$ref": "#n:1"
            }
          },
          {
            "$id": "r:113",
            "type": {
              "$ref": "#rt:113"
            },
            "from": {
              "$ref": "#n:17"
            },
            "to": {
              "$ref": "#n:16"
            }
          },
          {
            "$id": "r:114",
            "type": {
              "$ref": "#rt:114"
            },
            "from": {
              "$ref": "#n:16"
            },
            "to": {
              "$ref": "#n:21"
            }
          },
          {
            "$id": "r:115",
            "type": {
              "$ref": "#rt:115"
            },
            "from": {
              "$ref": "#n:1"
            },
            "to": {
              "$ref": "#n:16"
            }
          },
          {
            "$id": "r:116",
            "type": {
              "$ref": "#rt:116"
            },
            "from": {
              "$ref": "#n:1"
            },
            "to": {
              "$ref": "#n:9"
            }
          },
          {
            "$id": "r:117",
            "type": {
              "$ref": "#rt:117"
            },
            "from": {
              "$ref": "#n:18"
            },
            "to": {
              "$ref": "#n:17"
            }
          },
          {
            "$id": "r:118",
            "type": {
              "$ref": "#rt:118"
            },
            "from": {
              "$ref": "#n:18"
            },
            "to": {
              "$ref": "#n:11"
            }
          },
          {
            "$id": "r:119",
            "type": {
              "$ref": "#rt:119"
            },
            "from": {
              "$ref": "#n:18"
            },
            "to": {
              "$ref": "#n:13"
            }
          },
          {
            "$id": "r:120",
            "type": {
              "$ref": "#rt:120"
            },
            "from": {
              "$ref": "#n:18"
            },
            "to": {
              "$ref": "#n:9"
            }
          },
          {
            "$id": "r:121",
            "type": {
              "$ref": "#rt:121"
            },
            "from": {
              "$ref": "#n:1"
            },
            "to": {
              "$ref": "#n:29"
            }
          },
          {
            "$id": "r:122",
            "type": {
              "$ref": "#rt:122"
            },
            "from": {
              "$ref": "#n:18"
            },
            "to": {
              "$ref": "#n:29"
            }
          },
          {
            "$id": "r:123",
            "type": {
              "$ref": "#rt:123"
            },
            "from": {
              "$ref": "#n:16"
            },
            "to": {
              "$ref": "#n:29"
            }
          },
          {
            "$id": "r:124",
            "type": {
              "$ref": "#rt:124"
            },
            "from": {
              "$ref": "#n:29"
            },
            "to": {
              "$ref": "#n:7"
            }
          },
          {
            "$id": "r:125",
            "type": {
              "$ref": "#rt:125"
            },
            "from": {
              "$ref": "#n:25"
            },
            "to": {
              "$ref": "#n:29"
            }
          },
          {
            "$id": "r:126",
            "type": {
              "$ref": "#rt:126"
            },
            "from": {
              "$ref": "#n:16"
            },
            "to": {
              "$ref": "#n:16"
            }
          },
          {
            "$id": "r:127",
            "type": {
              "$ref": "#rt:127"
            },
            "from": {
              "$ref": "#n:24"
            },
            "to": {
              "$ref": "#n:3"
            }
          },
          {
            "$id": "r:128",
            "type": {
              "$ref": "#rt:128"
            },
            "from": {
              "$ref": "#n:3"
            },
            "to": {
              "$ref": "#n:27"
            }
          },
          {
            "$id": "r:129",
            "type": {
              "$ref": "#rt:129"
            },
            "from": {
              "$ref": "#n:3"
            },
            "to": {
              "$ref": "#n:27"
            }
          },
          {
            "$id": "r:130",
            "type": {
              "$ref": "#rt:130"
            },
            "from": {
              "$ref": "#n:16"
            },
            "to": {
              "$ref": "#n:14"
            }
          },
          {
            "$id": "r:131",
            "type": {
              "$ref": "#rt:131"
            },
            "from": {
              "$ref": "#n:4"
            },
            "to": {
              "$ref": "#n:27"
            }
          },
          {
            "$id": "r:132",
            "type": {
              "$ref": "#rt:132"
            },
            "from": {
              "$ref": "#n:16"
            },
            "to": {
              "$ref": "#n:27"
            }
          },
          {
            "$id": "r:133",
            "type": {
              "$ref": "#rt:133"
            },
            "from": {
              "$ref": "#n:13"
            },
            "to": {
              "$ref": "#n:27"
            }
          },
          {
            "$id": "r:134",
            "type": {
              "$ref": "#rt:134"
            },
            "from": {
              "$ref": "#n:13"
            },
            "to": {
              "$ref": "#n:13"
            }
          },
          {
            "$id": "r:135",
            "type": {
              "$ref": "#rt:135"
            },
            "from": {
              "$ref": "#n:19"
            },
            "to": {
              "$ref": "#n:19"
            }
          },
          {
            "$id": "r:136",
            "type": {
              "$ref": "#rt:136"
            },
            "from": {
              "$ref": "#n:12"
            },
            "to": {
              "$ref": "#n:27"
            }
          },
          {
            "$id": "r:137",
            "type": {
              "$ref": "#rt:137"
            },
            "from": {
              "$ref": "#n:16"
            },
            "to": {
              "$ref": "#n:14"
            }
          },
          {
            "$id": "r:138",
            "type": {
              "$ref": "#rt:138"
            },
            "from": {
              "$ref": "#n:16"
            },
            "to": {
              "$ref": "#n:13"
            }
          },
          {
            "$id": "r:139",
            "type": {
              "$ref": "#rt:139"
            },
            "from": {
              "$ref": "#n:16"
            },
            "to": {
              "$ref": "#n:13"
            }
          },
          {
            "$id": "r:140",
            "type": {
              "$ref": "#rt:140"
            },
            "from": {
              "$ref": "#n:3"
            },
            "to": {
              "$ref": "#n:13"
            }
          },
          {
            "$id": "r:141",
            "type": {
              "$ref": "#rt:141"
            },
            "from": {
              "$ref": "#n:16"
            },
            "to": {
              "$ref": "#n:12"
            }
          }
        ],
        "constraints": [
          {
            "$id": "c:1",
            "name": "id_User_key",
            "constraintType": "key",
            "entityType": "node",
            "nodeLabel": {
              "$ref": "#nl:1"
            },
            "properties": [
              {
                "$ref": "#p:1"
              }
            ]
          },
          {
            "$id": "c:2",
            "name": "id_Signal_key",
            "constraintType": "key",
            "entityType": "node",
            "nodeLabel": {
              "$ref": "#nl:2"
            },
            "properties": [
              {
                "$ref": "#p:11"
              }
            ]
          },
          {
            "$id": "c:3",
            "name": "id_Memory_key",
            "constraintType": "key",
            "entityType": "node",
            "nodeLabel": {
              "$ref": "#nl:3"
            },
            "properties": [
              {
                "$ref": "#p:18"
              }
            ]
          },
          {
            "$id": "c:4",
            "name": "id_World_key",
            "constraintType": "key",
            "entityType": "node",
            "nodeLabel": {
              "$ref": "#nl:4"
            },
            "properties": [
              {
                "$ref": "#p:27"
              }
            ]
          },
          {
            "$id": "c:5",
            "name": "id_Agent_key",
            "constraintType": "key",
            "entityType": "node",
            "nodeLabel": {
              "$ref": "#nl:5"
            },
            "properties": [
              {
                "$ref": "#p:33"
              }
            ]
          },
          {
            "$id": "c:6",
            "name": "id_Location_key",
            "constraintType": "key",
            "entityType": "node",
            "nodeLabel": {
              "$ref": "#nl:6"
            },
            "properties": [
              {
                "$ref": "#p:38"
              }
            ]
          },
          {
            "$id": "c:7",
            "name": "id_Knowledge_key",
            "constraintType": "key",
            "entityType": "node",
            "nodeLabel": {
              "$ref": "#nl:7"
            },
            "properties": [
              {
                "$ref": "#p:43"
              }
            ]
          },
          {
            "$id": "c:8",
            "name": "id_Asset_key",
            "constraintType": "key",
            "entityType": "node",
            "nodeLabel": {
              "$ref": "#nl:8"
            },
            "properties": [
              {
                "$ref": "#p:50"
              }
            ]
          },
          {
            "$id": "c:9",
            "name": "id_Organization_key",
            "constraintType": "key",
            "entityType": "node",
            "nodeLabel": {
              "$ref": "#nl:9"
            },
            "properties": [
              {
                "$ref": "#p:56"
              }
            ]
          },
          {
            "$id": "c:10",
            "name": "id_Marketplace_key",
            "constraintType": "key",
            "entityType": "node",
            "nodeLabel": {
              "$ref": "#nl:10"
            },
            "properties": [
              {
                "$ref": "#p:60"
              }
            ]
          },
          {
            "$id": "c:11",
            "name": "id_Product_key",
            "constraintType": "key",
            "entityType": "node",
            "nodeLabel": {
              "$ref": "#nl:11"
            },
            "properties": [
              {
                "$ref": "#p:63"
              }
            ]
          },
          {
            "$id": "c:12",
            "name": "id_Practice_key",
            "constraintType": "key",
            "entityType": "node",
            "nodeLabel": {
              "$ref": "#nl:12"
            },
            "properties": [
              {
                "$ref": "#p:68"
              }
            ]
          },
          {
            "$id": "c:13",
            "name": "id_Event_key",
            "constraintType": "key",
            "entityType": "node",
            "nodeLabel": {
              "$ref": "#nl:13"
            },
            "properties": [
              {
                "$ref": "#p:77"
              }
            ]
          },
          {
            "$id": "c:14",
            "name": "id_Rule_key",
            "constraintType": "key",
            "entityType": "node",
            "nodeLabel": {
              "$ref": "#nl:14"
            },
            "properties": [
              {
                "$ref": "#p:92"
              }
            ]
          },
          {
            "$id": "c:15",
            "name": "id_Protocol_key",
            "constraintType": "key",
            "entityType": "node",
            "nodeLabel": {
              "$ref": "#nl:15"
            },
            "properties": [
              {
                "$ref": "#p:98"
              }
            ]
          },
          {
            "$id": "c:16",
            "name": "id_SystemComponent_key",
            "constraintType": "key",
            "entityType": "node",
            "nodeLabel": {
              "$ref": "#nl:16"
            },
            "properties": [
              {
                "$ref": "#p:102"
              }
            ]
          },
          {
            "$id": "c:17",
            "name": "id_Constraint_key",
            "constraintType": "key",
            "entityType": "node",
            "nodeLabel": {
              "$ref": "#nl:17"
            },
            "properties": [
              {
                "$ref": "#p:109"
              }
            ]
          },
          {
            "$id": "c:18",
            "name": "id_Governance_key",
            "constraintType": "key",
            "entityType": "node",
            "nodeLabel": {
              "$ref": "#nl:18"
            },
            "properties": [
              {
                "$ref": "#p:114"
              }
            ]
          },
          {
            "$id": "c:19",
            "name": "id_Interpretation_key",
            "constraintType": "key",
            "entityType": "node",
            "nodeLabel": {
              "$ref": "#nl:19"
            },
            "properties": [
              {
                "$ref": "#p:119"
              }
            ]
          },
          {
            "$id": "c:20",
            "name": "id_Notification_key",
            "constraintType": "key",
            "entityType": "node",
            "nodeLabel": {
              "$ref": "#nl:20"
            },
            "properties": [
              {
                "$ref": "#p:124"
              }
            ]
          },
          {
            "$id": "c:21",
            "name": "id_Permission_key",
            "constraintType": "key",
            "entityType": "node",
            "nodeLabel": {
              "$ref": "#nl:21"
            },
            "properties": [
              {
                "$ref": "#p:128"
              }
            ]
          },
          {
            "$id": "c:22",
            "name": "id_Context_key",
            "constraintType": "key",
            "entityType": "node",
            "nodeLabel": {
              "$ref": "#nl:22"
            },
            "properties": [
              {
                "$ref": "#p:133"
              }
            ]
          },
          {
            "$id": "c:23",
            "name": "id_Transformation_key",
            "constraintType": "key",
            "entityType": "node",
            "nodeLabel": {
              "$ref": "#nl:23"
            },
            "properties": [
              {
                "$ref": "#p:138"
              }
            ]
          },
          {
            "$id": "c:24",
            "name": "id_Claim_key",
            "constraintType": "key",
            "entityType": "node",
            "nodeLabel": {
              "$ref": "#nl:24"
            },
            "properties": [
              {
                "$ref": "#p:142"
              }
            ]
          },
          {
            "$id": "c:25",
            "name": "id_Model_key",
            "constraintType": "key",
            "entityType": "node",
            "nodeLabel": {
              "$ref": "#nl:25"
            },
            "properties": [
              {
                "$ref": "#p:147"
              }
            ]
          },
          {
            "$id": "c:26",
            "name": "id_Group_key",
            "constraintType": "key",
            "entityType": "node",
            "nodeLabel": {
              "$ref": "#nl:26"
            },
            "properties": [
              {
                "$ref": "#p:152"
              }
            ]
          },
          {
            "$id": "c:27",
            "name": "id_Metric_key",
            "constraintType": "key",
            "entityType": "node",
            "nodeLabel": {
              "$ref": "#nl:27"
            },
            "properties": [
              {
                "$ref": "#p:156"
              }
            ]
          },
          {
            "$id": "c:28",
            "name": "id_Experience_key",
            "constraintType": "key",
            "entityType": "node",
            "nodeLabel": {
              "$ref": "#nl:28"
            },
            "properties": [
              {
                "$ref": "#p:162"
              }
            ]
          },
          {
            "$id": "c:29",
            "name": "id_Data_key",
            "constraintType": "key",
            "entityType": "node",
            "nodeLabel": {
              "$ref": "#nl:29"
            },
            "properties": [
              {
                "$ref": "#p:166"
              }
            ]
          }
        ],
        "indexes": []
      }
    },
    "graphSchemaExtensionsRepresentation": {
      "nodeKeyProperties": [
        {
          "node": {
            "$ref": "#n:1"
          },
          "keyProperties": [
            {
              "$ref": "#p:1"
            }
          ]
        },
        {
          "node": {
            "$ref": "#n:2"
          },
          "keyProperties": [
            {
              "$ref": "#p:11"
            }
          ]
        },
        {
          "node": {
            "$ref": "#n:3"
          },
          "keyProperties": [
            {
              "$ref": "#p:18"
            }
          ]
        },
        {
          "node": {
            "$ref": "#n:4"
          },
          "keyProperties": [
            {
              "$ref": "#p:27"
            }
          ]
        },
        {
          "node": {
            "$ref": "#n:5"
          },
          "keyProperties": [
            {
              "$ref": "#p:33"
            }
          ]
        },
        {
          "node": {
            "$ref": "#n:6"
          },
          "keyProperties": [
            {
              "$ref": "#p:38"
            }
          ]
        },
        {
          "node": {
            "$ref": "#n:7"
          },
          "keyProperties": [
            {
              "$ref": "#p:43"
            }
          ]
        },
        {
          "node": {
            "$ref": "#n:8"
          },
          "keyProperties": [
            {
              "$ref": "#p:50"
            }
          ]
        },
        {
          "node": {
            "$ref": "#n:9"
          },
          "keyProperties": [
            {
              "$ref": "#p:56"
            }
          ]
        },
        {
          "node": {
            "$ref": "#n:10"
          },
          "keyProperties": [
            {
              "$ref": "#p:60"
            }
          ]
        },
        {
          "node": {
            "$ref": "#n:11"
          },
          "keyProperties": [
            {
              "$ref": "#p:63"
            }
          ]
        },
        {
          "node": {
            "$ref": "#n:12"
          },
          "keyProperties": [
            {
              "$ref": "#p:68"
            }
          ]
        },
        {
          "node": {
            "$ref": "#n:13"
          },
          "keyProperties": [
            {
              "$ref": "#p:77"
            }
          ]
        },
        {
          "node": {
            "$ref": "#n:14"
          },
          "keyProperties": [
            {
              "$ref": "#p:92"
            }
          ]
        },
        {
          "node": {
            "$ref": "#n:15"
          },
          "keyProperties": [
            {
              "$ref": "#p:98"
            }
          ]
        },
        {
          "node": {
            "$ref": "#n:16"
          },
          "keyProperties": [
            {
              "$ref": "#p:102"
            }
          ]
        },
        {
          "node": {
            "$ref": "#n:17"
          },
          "keyProperties": [
            {
              "$ref": "#p:109"
            }
          ]
        },
        {
          "node": {
            "$ref": "#n:18"
          },
          "keyProperties": [
            {
              "$ref": "#p:114"
            }
          ]
        },
        {
          "node": {
            "$ref": "#n:19"
          },
          "keyProperties": [
            {
              "$ref": "#p:119"
            }
          ]
        },
        {
          "node": {
            "$ref": "#n:20"
          },
          "keyProperties": [
            {
              "$ref": "#p:124"
            }
          ]
        },
        {
          "node": {
            "$ref": "#n:21"
          },
          "keyProperties": [
            {
              "$ref": "#p:128"
            }
          ]
        },
        {
          "node": {
            "$ref": "#n:22"
          },
          "keyProperties": [
            {
              "$ref": "#p:133"
            }
          ]
        },
        {
          "node": {
            "$ref": "#n:23"
          },
          "keyProperties": [
            {
              "$ref": "#p:138"
            }
          ]
        },
        {
          "node": {
            "$ref": "#n:24"
          },
          "keyProperties": [
            {
              "$ref": "#p:142"
            }
          ]
        },
        {
          "node": {
            "$ref": "#n:25"
          },
          "keyProperties": [
            {
              "$ref": "#p:147"
            }
          ]
        },
        {
          "node": {
            "$ref": "#n:26"
          },
          "keyProperties": [
            {
              "$ref": "#p:152"
            }
          ]
        },
        {
          "node": {
            "$ref": "#n:27"
          },
          "keyProperties": [
            {
              "$ref": "#p:156"
            }
          ]
        },
        {
          "node": {
            "$ref": "#n:28"
          },
          "keyProperties": [
            {
              "$ref": "#p:162"
            }
          ]
        },
        {
          "node": {
            "$ref": "#n:29"
          },
          "keyProperties": [
            {
              "$ref": "#p:166"
            }
          ]
        }
      ],
      "relationshipKeyProperties": []
    },
    "graphMappingRepresentation": {
      "dataSourceSchema": {
        "type": "local-unstructured",
        "tableSchemas": [
          {
            "name": "COSMO Engineering Build Contract v1.0 — Missing Implementation Layer.docx",
            "expanded": false,
            "fields": []
          },
          {
            "name": "COSMO Founder Canon v1.0 + System Boundary Charter.docx",
            "expanded": false,
            "fields": []
          },
          {
            "name": "COSMO Phase 1 — Human Problem Architecture v1.0.docx",
            "expanded": false,
            "fields": []
          },
          {
            "name": "COSMO Phase 1 — Human Problem Architecture.docx",
            "expanded": false,
            "fields": []
          },
          {
            "name": "COSMO Phase 2 — Constitution v1.0.docx",
            "expanded": false,
            "fields": []
          },
          {
            "name": "COSMO Phase 3 — Evidence and Claims Governance System.docx",
            "expanded": false,
            "fields": []
          },
          {
            "name": "COSMO Phase 4 — Ontology v1.0.docx",
            "expanded": false,
            "fields": []
          },
          {
            "name": "COSMO Phase 5 — Personal State Model.docx",
            "expanded": false,
            "fields": []
          },
          {
            "name": "COSMO Phase 6 — Resonance Model v1.0.docx",
            "expanded": false,
            "fields": []
          },
          {
            "name": "COSMO Phase 7 — Unified Transformation Memory Architecture.docx",
            "expanded": false,
            "fields": []
          },
          {
            "name": "COSMO Phase 8 — Personal Digital Twin Specification.docx",
            "expanded": false,
            "fields": []
          },
          {
            "name": "COSMO Phase 9 — Practice and Intervention Library.docx",
            "expanded": false,
            "fields": []
          },
          {
            "name": "COSMO Phase 10 — Adaptive Personalization Protocol.docx",
            "expanded": false,
            "fields": []
          },
          {
            "name": "COSMO Phase 11 — Presence Architecture.docx",
            "expanded": false,
            "fields": []
          },
          {
            "name": "COSMO Phase 12 — Perspective and Meaning Intelligence Specification.docx",
            "expanded": false,
            "fields": []
          },
          {
            "name": "COSMO Phase 13 — Companion AI Constitution and Runtime.docx",
            "expanded": false,
            "fields": []
          },
          {
            "name": "COSMO Phase 14 — Avatar Evolution System.docx",
            "expanded": false,
            "fields": []
          },
          {
            "name": "COSMO Phase 15 — Transformation Quest Engine.docx",
            "expanded": false,
            "fields": []
          },
          {
            "name": "COSMO Phase 16 — Relationship Graph and Gifting Protocol.docx",
            "expanded": false,
            "fields": []
          },
          {
            "name": "COSMO PHASE 17 — Community Operating System v1.0.docx",
            "expanded": false,
            "fields": []
          }
        ]
      },
      "nodeMappings": [],
      "relationshipMappings": []
    },
    "configurations": {
      "idsToIgnore": [],
      "arrayDelimiter": "|",
      "vectorDelimiter": "|"
    }
  }
}

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]
```

---
**MOC:** [[MODELS_MOC]]
