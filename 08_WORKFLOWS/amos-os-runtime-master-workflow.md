---
title: amos-os-runtime-master-workflow
Type: Workflow
Skill: amos-os-runtime-master
Agent: amos-os-runtime-agent
Trigger: "AMOS OS & Runtime — OS Kernel v4.4, runtime pipeline (Perceive→Route→Admit→Plan→Schedule→Execute→Observe→Repair→Audit→Finalize), infrastructure control plane, deployment. Use for runtime reasoning,"
Version: 1.0.0
tags: [note, vault]
---


# Workflow: AMOS OS & Runtime Master

## Preconditions

- The `amos-os-runtime-master` skill exists and is loaded.
- The `amos-os-runtime-agent` agent is available and has valid content_hash `19b38fc3f8172fd2`.
- The query falls within the skill's declared scope and domain.
- All required vault sources (if any) are accessible.
- Epistemic class labeling is enabled (SOURCE / DERIVED / AMOS_MODEL / EMPIRICAL).

## Steps

1. **Intake**: Identify the problem domain and confirm it matches the AMOS OS & Runtime Master scope.
   - Classify the query against the domain's sub-capabilities
   - Route to the appropriate section of the parent skill
2. **Skill Invocation**: Load the `amos-os-runtime-master` skill and its vault-sourced content.
   - Read the canonical vault source: `11_KNOWLEDGE/AMOS_Full_Brain_OS_Architecture.md`
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

- **G1 (Intake)**: Problem domain confirmed within AMOS OS & Runtime Master scope.
- **G2 (Decomposition)**: Components are MECE and traceable to domain framework.
- **G3 (Application)**: Equations/algorithms carry correct epistemic status tags.
- **G4 (Validation)**: Results pass Law of Law, Rule of 2, Rule of 4 checks.
- **G5 (Output)**: Output format matches specification; provenance recorded; epistemic labels present.

## Failure Paths

- **Scope mismatch**: If problem is outside AMOS OS & Runtime Master scope, route to matching domain master or escalate.
- **Validation failure**: Downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Missing dependency**: If a required cross-domain skill is unavailable, halt and report.
- **Epistemic overreach**: If a claim exceeds its evidence class, downgrade to UNVERIFIED.

## Dependencies

- `amos-os-runtime-master` (primary skill)
- `amos-os-runtime-agent.json` (primary agent, content_hash: `19b38fc3f8172fd2`)
- Vault source: `11_KNOWLEDGE/AMOS_Full_Brain_OS_Architecture.md` (content_hash: `33b191af65b363b7`)

## Authority

- **Bound skill**: `amos-os-runtime-master`
- **Bound agent**: `amos-os-runtime-agent`
- **Skill path**: `.devin/skills/amos-os-runtime-master/SKILL.md`
- **Agent path**: `.devin/agents/amos-os-runtime-agent.json`
- **Agent content_hash**: `19b38fc3f8172fd2`

## Provenance

- **Origin architect**: Trang Phan
- **Source**: AMOS skill corpus + Obsidian vault
- **Vault source**: `11_KNOWLEDGE/AMOS_Full_Brain_OS_Architecture.md` (content_hash: `33b191af65b363b7`)
- **Consolidation**: 176 sub-workflows merged into domain master
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
- Terminal state: VERIFIED (all gates passed) | CONDITIONAL (gates pas

---
**MOC:** [[08_WORKFLOWS_MOC]]
