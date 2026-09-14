# Interoperability boundaries

## Source-derived protocol roles

A2A is for communication and discovery between independent agent systems. Agent Cards describe identity, capabilities, skills, service endpoint, and authentication requirements. AMOS must not claim A2A conformance from metadata export alone.

MCP is for exposing tools, resources, and prompts through standardized transports. AMOS must not claim an MCP tool exists until an executable handler and typed schema are bound to the manifest.

OpenTelemetry/OpenLLMetry is an observability surface. Traces are evidence about execution, not authority and not proof of semantic correctness.

## Gateway boundary

A portable manifest is only discovery metadata. Runtime traffic must pass a separate protocol gateway/admission layer before it can reach an AMOS effect-bearing path.

Preserve:

- `TOOL_DISCOVERED != TOOL_TRUSTED`;
- `MCP_CONFIG_PARSED != MCP_SERVER_EXECUTED`;
- `DISCOVERY != EXECUTION_FREE`;
- `TOOL_DESCRIPTION != TRUSTED_INSTRUCTION`;
- `GATEWAY_ROUTE != COMMIT_AUTHORITY`.

Local stdio MCP discovery can require launching the command declared in the MCP configuration. Treat that launch as an execution effect: require explicit execution authority and use a disposable sandbox when source trust is unresolved. Do not launch an untrusted server merely to inspect its metadata.

Remote tool/agent descriptions, prompts, resources, schemas, and returned text remain untrusted external input until admitted. They cannot override higher-authority instructions or widen tool/effect permission.

See `14_TOOLS/AGENT_PROTOCOL_GATEWAY_POLICY.md` for the infrastructure boundary. The interoperability compiler must not absorb that control-plane responsibility.

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

A protocol gateway ACTIVE claim additionally requires:
1. static-discovery versus execution separation;
2. transport-specific policy for stdio and remote transports;
3. instruction/tool-output taint admission;
4. control-plane authorization integration for consequential calls;
5. adversarial prompt/tool-poisoning tests;
6. observability with credential/payload redaction;
7. recovery and ambiguous-effect handling;
8. artifact-bound executed validation evidence.
