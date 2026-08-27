---
title: amos-security-safety-master-workflow
type: workflow
source: 08_WORKFLOWS
Type: Workflow
Skill: amos-security-safety-master
Agent: amos-security-safety-agent
Trigger: "AMOS Security & Safety — adversarial robustness, privacy, safety firewalls, immune systems, drift alignment. Use for security analysis, safety verification, or adversarial defense."
Version: 1.0.0
tags: [note, vault, canon/workflow]
rscf:
  state: AMOS_MODEL
  claim_class: EMPIRICAL
  provenance: AMOS_corpus
  scope: workflow_process
---


# Workflow: AMOS Security & Safety Master


## Preconditions

- The `amos-security-safety-master` skill exists and is loaded.
- The `amos-security-safety-agent` agent is available and has valid content_hash.
- The query falls within the skill's declared scope and domain.
- All required vault sources (if any) are accessible.
- Epistemic class labeling is enabled (SOURCE / DERIVED / AMOS_MODEL / EMPIRICAL).

## Steps

1. **Intake**: Identify the problem domain and confirm it matches the AMOS Security & Safety Master scope.
   - Classify the query against the domain's sub-capabilities
   - Route to the appropriate section of the parent skill
2. **Skill Invocation**: Load the `amos-security-safety-master` skill and its vault-sourced content.
   - Read the canonical vault source: `18_SECURITY/SECURITY_README.md`
   - Identify which sub-domain is most relevant
3. **Decomposition**: Break the problem into components using the domain's framework.
   - Apply MECE decomposition within the domain
   - Identify which sub-skills are relevant
4. **Application**: Apply the domain's equations, algorithms, or frameworks.
   - Use the appropriate knowledge family within the domain
   - Tag every equation with its epistemic status (SOURCE_CANON / AMOS_MODEL)
5. **Validation**: Check results against the domain's validation gates.
   - Law of Law: no unresolved contradictions
   - Rule of 2: binary contrast present
   - Rule of 4: complete decomposition
   - Epistemic class labels present
6. **Synthesis**: Combine component results into a MECE-compliant output.
   - Cross-reference with vault source for provenance
   - Declare any cross-domain bridges
7. **Output**: Present results with full provenance and epistemic labeling.
   - Include confidence ceiling
   - Record source path for every derived claim

## Validation Gates

- **G1 (Intake)**: Problem domain confirmed within AMOS Security & Safety Master scope.
- **G2 (Decomposition)**: Components are MECE and traceable to domain framework.
- **G3 (Application)**: Equations/algorithms carry correct epistemic status tags.
- **G4 (Validation)**: Results pass Law of Law, Rule of 2, Rule of 4 checks.
- **G5 (Output)**: Output format matches specification; provenance recorded; epistemic labels present.

## Failure Paths

- **Scope mismatch**: If problem is outside AMOS Security & Safety Master scope, route to matching domain master or escalate.
- **Validation failure**: Downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Missing dependency**: If a required cross-domain skill is unavailable, halt and report.
- **Epistemic overreach**: If a claim exceeds its evidence class, downgrade to UNVERIFIED.

## Dependencies

- `amos-security-safety-master` (primary skill)
- `amos-security-safety-agent.json` (primary agent)
- Vault source: `18_SECURITY/SECURITY_README.md`

## Provenance

- **Origin architect**: Trang Phan
- **Source**: AMOS skill corpus + Obsidian vault
- **Vault source**: `18_SECURITY/SECURITY_README.md`
- **Consolidation**: 2 sub-workflows merged into domain master
- **Merge date**: 2026-08-26
- **Epistemic class**: DERIVED (workflow generated from domain master skill)


## Validation

- **Consistency**: Results must not contain unresolved contradictions within the skill's scope (Law of Law).
- **Epistemic class**: All claims must be labeled SOURCE / DERIVED / AMOS_MODEL / EMPIRICAL — never claim beyond evidence.
- **Provenance**: Source path must be recorded for any derived claim.
- **Anti-overreach**: No claim beyond the skill's declared scope and epistemic class.
- **Bridge discipline**: Cross-domain bridges must be declared; symbolic equality ≠ empirical equality.
- **Equation firewall**: Any equation used must carry a status tag (ESTABLISHED_MATH / SOURCE_DERIVED / AMOS_MODEL / EMPIRICALLY_CALIBRATED / UNVERIFIED).
- **Failure mode**: If validation fails, downgrade confidence, flag the gap, and escalate — do not force-fit.

## Output

- Present results in the format specified by the skill (MURK format if applicable).
- Label all claims with epistemic class and confidence ceiling.
- Record provenance for every derived result.
- Flag any unresolved gaps as UNKNOWN/GAP — do not force-fit.
- Terminal state: VERIFIED (all gates passed) | CONDITIONAL (gates passed with caveats) | EXTERNAL_DEPENDENCY (blocked by missing input) | UNKNOWN/GAP (unable to resolve).

---
**MOC:** [[08_WORKFLOWS_MOC]]

## Orchestration Pattern

**Pattern**: Single-Agent with Validation Gates

This workflow follows a single-agent orchestration with explicit validation gates between steps:
1. **Intake** -> validation gate -> **Skill Invocation** -> validation gate -> **Application** -> validation gate -> **Output**
2. Each gate checks: epistemic labeling, provenance, scope compliance, confidence ceiling
3. On gate failure: route to error handling or escalate to parent workflow


## Evaluation Gates

### Gate 1: Intake Validation
- Query matches skill scope
- Required inputs present
- No scope violations detected

### Gate 2: Skill Load Validation
- Skill file exists and is valid
- Agent binding is valid
- Required vault sources accessible

### Gate 3: Output Validation
- Epistemic class labels present
- Provenance recorded for all derived claims
- Confidence ceiling not exceeded
- No unresolved CRITICAL_GAPs
- Scope compliance verified


## Error Handling

| Error Type | Detection | Recovery |
|---|---|---|
| Scope violation | Gate 1 check | Route to parent skill |
| Missing evidence | Gate 3 check | Flag as GAP, reduce confidence to 0.5 |
| Contradiction | Gate 3 check | Flag as CRITICAL_GAP, halt |
| Provenance loss | Gate 3 check | Mark as UNKNOWN, request human review |
| Timeout | Step budget exceeded | Return partial result with warnings |
| Drift | Confidence calibration check | Trigger drift alignment governor |


## Human-in-the-Loop

- **Default**: Automated execution without human intervention
- **Escalation triggers**:
  - CRITICAL_GAP detected
  - Confidence below 0.3
  - Scope violation requiring reclassification
  - Contradiction that cannot be auto-resolved
- **Review checkpoint**: After Gate 3, if any warnings are present


## Monitoring

- **Trace level**: Full (inputs, outputs, intermediate steps)
- **Metrics**: Step count, token usage, confidence, gap count, execution time
- **Alerts**: CRITICAL_GAP, confidence < 0.3, scope violation, timeout
- **Provenance**: Every output traces back to source evidence via provenance chain


## Composition

- **Skill**: `amos-security-safety-master`
- **Agent**: `amos-security-safety-agent`
- **Parent workflow**: Routes via `AMOS_HOME` or parent skill workflow
- **Chain depth**: Maximum 3 workflows in sequence without orchestrator approval
- **Parallel execution**: Supported when independent capabilities are invoked

