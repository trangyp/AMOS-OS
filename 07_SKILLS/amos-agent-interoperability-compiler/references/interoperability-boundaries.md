# Interoperability boundaries

## Source-derived protocol roles

A2A is for communication and discovery between independent agent systems. Agent Cards describe identity, capabilities, skills, service endpoint, and authentication requirements. AMOS must not claim A2A conformance from metadata export alone.

MCP is for exposing tools, resources, and prompts through standardized transports. AMOS must not claim an MCP tool exists until an executable handler and typed schema are bound to the manifest.

OpenTelemetry/OpenLLMetry is an observability surface. Traces are evidence about execution, not authority and not proof of semantic correctness.

## Promotion gates

A2A ACTIVE requires:
1. candidate manifest validation;
2. protocol-schema validation against the target A2A release;
3. endpoint and transport implementation;
4. authentication/authorization policy;
5. negative and interoperability tests;
6. executed receipt.

MCP ACTIVE requires:
1. candidate manifest validation;
2. typed input/output schema;
3. executable tool/resource/prompt handler;
4. authority and side-effect policy;
5. transport tests;
6. executed receipt.
