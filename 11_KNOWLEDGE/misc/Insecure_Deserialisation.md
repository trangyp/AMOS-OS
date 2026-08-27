---
tags: [misc]
---
# Insecure Deserialisation

## Overview
Insecure deserialisation occurs when an application deserialises untrusted data without proper validation, allowing attackers to manipulate serialized objects to inject malicious payloads, achieve remote code execution, or perform privilege escalation. Listed as #8 in the OWASP Top 10.

## How It Works
1. Application receives serialized object data (JSON, XML, binary formats like Java ObjectOutputStream, Python pickle, PHP serialize)
2. Deserialisation reconstructs the object graph, potentially invoking custom methods (readObject, __wakeup, __reduce__)
3. Attacker crafts a malicious serialized payload that triggers dangerous code paths during reconstruction

## Common Vulnerable Technologies
- **Java**: `ObjectInputStream.readObject()`, XML decoding, `Yaml.load()`
- **Python**: `pickle.loads()`, `yaml.load()`, `json.loads()` with custom decoders
- **PHP**: `unserialize()`, `__wakeup()`, `__destruct()` magic methods
- **.NET**: `BinaryFormatter.Deserialize()`, `JavaScriptSerializer`, `XmlSerializer`
- **Ruby**: `Marshal.load()`, `YAML.load()`

## Attack Vectors
- **Gadget chains**: Chain existing library methods (commons-collections, ROME, Groovy) to achieve RCE
- **Object injection**: Modify serialized data to inject unexpected object types
- **Privilege escalation**: Tamper with serialized role/permission fields
- **DoS**: Craft deeply nested or cyclic object graphs to exhaust resources

## Detection
- Static analysis for deserialisation sinks (readObject, pickle.loads, unserialize)
- Dynamic testing with crafted serialized payloads
- Review all endpoints that accept serialized data (cookies, API params, file uploads)
- Monitor for unexpected object types in deserialisation input

## Mitigation
- **Avoid deserialising untrusted data** — use JSON with strict schema validation instead
- **Implement integrity checks** (HMAC signatures on serialized data)
- **Use allow-lists** for permitted classes during deserialisation
- **Disable dangerous features** (e.g., `pickle` → `json`, `YAML.load` → `YAML.safe_load`)
- **Patch deserialisation libraries** (Apache Commons-Collections, Jackson, Fastjson)
- **Sandbox deserialisation** in low-privilege contexts

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
