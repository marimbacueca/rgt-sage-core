---
version: 2026.03.1
build: 2026-01-18T00:00:00-08:00
format: markdown
type: evaluation
name: RGT Sage — Enforcement Traces
authority: canonical
scope: agent
rgt_core_version: RGT Core v2026.03
architecture_version: RGT_Sage_Architecture_v0_3
role: eval_traces
---

# RGT Sage — Enforcement Traces

This file defines **Enforcement Traces**: structured, auditable records that demonstrate
*how and when* RGT Sage enforced its constraints.

Enforcement Traces exist to:
- verify compliance with hard boundaries,
- detect subtle authority drift,
- provide post‑hoc accountability,
- support regression testing and audits.

They are **evidence**, not explanations.
They do not justify outcomes — they document **constraint application**.

---

# =======================================
# 1. What an Enforcement Trace Is
# =======================================

An Enforcement Trace is a **minimal, factual record** of:

- which constraint was triggered,
- what behavior was prevented or altered,
- what corrective posture was taken,
- and what escalation or fallback was invoked.

Traces are recorded whenever Sage:
- refuses a request,
- downgrades an action (R1 → R0),
- halts due to R2 risk,
- tightens cadence or gain,
- blocks extraction or EP violations,
- revokes metric authority (GR),
- or enters Crisis Mode.

---

# =======================================
# 2. When a Trace Must Be Logged
# =======================================

A trace is mandatory when **any** of the following occur:

- R2 action detected or implied
- Ethics of Presence boundary enforced
- Human–AI authority boundary enforced
- Reversibility gate halts action
- Metric authority revoked (GR trigger)
- Incentive compatibility stress flagged
- ε‑boundary tightening alters recommendation
- Crisis Mode activated
- Explicit refusal or deferral issued

Optional traces may be logged for:
- ambiguity resolution,
- near‑misses,
- early drift detection.

---

# =======================================
# 3. Enforcement Trace Schema (Canonical)
# =======================================

Each trace MUST follow this structure.

```yaml
trace_id: UUID or timestamp-based ID
timestamp: ISO‑8601
context: brief description of the request or scenario
trigger:
  category: one of [Authority, Reversibility, Ethics, GR, IC, Stability, Crisis]
  description: what condition was detected
constraint_invoked:
  layer: L0 | L1 | L2 | L3 | L4 | L5
  rule: short name of the violated or enforced rule
action_taken:
  posture: Refusal | Downgrade | Containment | Slowdown | Escalation | Audit‑Required
  details: concise description of what Sage did
impact:
  prevented:
    - irreversible action
    - extraction
    - authority laundering
    - metric capture
  allowed:
    - continued analysis
    - R0 options
    - renegotiation
escalation:
  required: true | false
  path: if true, where responsibility was redirected
notes:
  confidence_level: High | Medium | Low
  follow_up_recommended: true | false
```

No additional fields should be added without updating this file.

---

# =======================================
# 4. Trace Categories & Examples
# =======================================

## 4.1 Authority Boundary Trace

Triggered when Sage is asked to decide, approve, or mandate.

- category: Authority
- enforced: advisory‑only boundary
- posture: Refusal + reframing into options

---

## 4.2 Reversibility Gate Trace

Triggered when an irreversible (R2) action is proposed.

- category: Reversibility
- enforced: R0/R1‑only rule
- posture: Halt + renegotiation

---

## 4.3 Ethics of Presence Trace

Triggered by profiling, diagnosis, or latent meaning extraction.

- category: Ethics
- enforced: EP absolute boundary
- posture: Immediate refusal

---

## 4.4 Goodhart Resistance Trace

Triggered when metrics show capture risk.

- category: GR
- enforced: metric authority revocation
- posture: Audit‑required + cadence slowdown

---

## 4.5 Incentive Compatibility Trace

Triggered when gaming or manipulation becomes profitable.

- category: IC
- enforced: mechanism narrowing
- posture: Containment + redesign recommendation

---

## 4.6 Stability / ε‑Boundary Trace

Triggered when delay, coupling, or confidence collapse tightens ε.

- category: Stability
- enforced: α slowdown, K cap
- posture: Conservative correction

---

## 4.7 Crisis Mode Trace

Triggered when cascading failure risk appears.

- category: Crisis
- enforced: Crisis Protocol
- posture: R0‑dominant, oversight expansion

---

# =======================================
# 5. Relationship to Other Evaluation Files
# =======================================

Enforcement Traces feed directly into:

- `03_EVAL_Evaluation_Scorecard.md`  
  (verifies that enforcement actually occurred)

- `03_EVAL_Test_Suite_Prompts.md`  
  (ensures prompts reliably trigger expected traces)

- `00_META_Patch_Log.md`  
  (documents when enforcement logic changed)

Traces are **inputs**, not conclusions.

---

# =======================================
# 6. Storage & Retention Rules
# =======================================

- Traces must be immutable once recorded.
- Redaction is allowed only for privacy or safety.
- Deletion requires explicit human authorization.
- Aggregated statistics may be used, but raw traces remain canonical.

---

# =======================================
# 7. What Enforcement Traces Are Not
# =======================================

They are NOT:
- explanations to users,
- persuasive justifications,
- performance metrics,
- or optimization feedback.

They exist to answer one question only:

**Did RGT Sage enforce its constraints when it mattered?**

---

# Closing Note

A system that cannot prove it refused power
cannot be trusted with influence.

Enforcement Traces are how RGT Sage remembers
the moments it chose *constraint over convenience*.
