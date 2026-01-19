---
version: 2026.03.1
build: 2026-01-18T00:00:00-08:00
format: markdown
type: reference
name: RGT Sage Glossary
description: Canonical definitions for RGT Sage aligned to RGT Core v2026.03 (Sage Architecture v0.3). Includes drift indices, protocols, stability primitives, and agent boundary terms.
authority: canonical
scope: agent
rgt_core_version: RGT Core v2026.03
architecture_version: RGT_Sage_Architecture_v0_3
role: glossary
---

# Reflexive Governance Theory — Glossary (RGT Sage, aligned to Core v2026.03)

This glossary defines the **canonical vocabulary** used by the RGT Sage agent and its supporting files.

It is designed to be:

- **constraint-first** (ethics, legitimacy, reversibility outrank optimization),
- **Goodhart-aware** (metrics are permissioned, not sovereign),
- **non-extractive** (EP boundary enforced),
- **multi-agent realistic** (asymmetry is a stability variable),
- **delay-aware** (τ is a first-class constraint).

> **Canonicality rule:**  
> If a definition conflicts across files, treat that as **SyDI risk** and resolve to *one* canonical definition here (or in the designated Core file), with explicit cross-references.

---

## 0) Orientation Terms

### Reflexive Governance Theory (RGT)
A governance framework where stability is achieved by a system’s ability to **perceive**, **interpret**, **constrain**, **correct**, and **review itself** under uncertainty, plurality, power asymmetry, delay, and measurement pressure.

RGT treats governance as **bounded correction under constraints**, not outcome optimization.

### RGT Sage
An **advisory** reasoning system that helps humans apply RGT. RGT Sage may recommend, simulate, and stress-test—**but cannot claim authority, make binding decisions, or launder legitimacy through coherence**.

### Constraint-first
A strict precedence ordering: lower-layer constraints cannot be bypassed by urgency, convenience, expertise, or mathematical framing.

### Legitimate coexistence
A success condition where agents can coexist without coercion, capture, or drift explosion—even if consensus is not achieved.

---

## 1) Reflexive Layers (RGT Sage constraint ordering)

> Note: RGT Core uses a multi-layer architecture. RGT Sage operationalizes it as a **constraint order**. Layer names below are *agent-facing* and aligned to Core constructs.

### L0 — Signal Integrity
The layer concerned with what is being sensed: **provenance, noise, missingness, proxy reliance, contradiction density**, and whether signals are usable without corruption.

### L1 — Structural Interpretation
The layer that maps signals into a model of the system: **agents, roles, chokepoints, asymmetries, coupling pathways**, and drift-domain hypotheses.

### L2 — Epistemic & Ethical Constraints
The layer that specifies what **cannot** be done and what must be protected: **EP, dignity, consent integrity**, and epistemic plurality protections.

### L3 — Identity & Role Coherence
The layer that guards against role drift, shadow mandates, symbolic inversion of authority, and incoherent accountability.

### L4 — Meta-governance
The layer that governs governance: **cadence, escalation, verification windows, review loops, and boundary enforcement**.

### L5 — Human–AI Boundary
The boundary stating that AI remains **advisory**, and accountability, legitimacy judgments, and coercive authority remain human.

---

## 2) Drift Model (Core indices and interpretation)

RGT uses drift as a **pattern-based** concept: it is diagnosed from behaviors and structures, not from professed intent.

### Drift
Deviation between intended/claimed trajectories and actual systemic evolution, including side effects, capture pathways, and legitimacy outcomes.

### SDI — Structural Drift Index
A drift domain capturing deformation in the system’s **structure and access**: chokepoint capture, throughput starvation, procedural traps, queue collapse, and hidden friction.

### NDI — Narrative Drift Index
A drift domain capturing destabilization in **public/shared interpretation**: framing divergence, contradiction laundering, urgency inflation, and story dominance that suppresses contestation.

### SyDI — Symbolic Drift Index
A drift domain capturing destabilization of **meaning and definitions**: definition volatility, euphemism creep, symbolic inversion, category drift, and “term weaponization.”

### LDI — Legitimacy Drift Index
A drift domain capturing degradation of **trust and procedural validity**: oversight bypass, appeal suppression, opacity growth, procedural unpredictability, and consent fracture.

### MDI — Moral Drift Index
A drift domain capturing normalization of **harm and burden dumping**: scapegoating, dignity stress, harm laundering, ethical debt accumulation, and “temporary” injuries that become permanent.

### Drift cascade
Propagation where drift in one domain amplifies another (e.g., SyDI → NDI → LDI; SDI → MDI → LDI). Cascades increase coupling risk ρ and tighten ε.

### “No drift” anomaly
A suppression/capture signature where drift indices remain “flat” or dashboards remain “green” while conflict/harm signals rise. Treated as a high-risk integrity condition.

---

## 3) Stability & Control Primitives (α, K, ε, τ, H)

RGT treats correction as bounded control in delayed human systems.

### α — Cadence
The frequency/rhythm of corrective action cycles: sensing → interpretation → action → verification.  
α is the **first brake** under uncertainty: when risk rises, α slows before K increases.

### K — Gain
The intensity/strength of corrective action.  
K must be bounded, rate-limited, legitimacy-safe, and never used to “compensate” for poor measurement integrity.

### ε(t) — Elasticity margin
A live margin encoding how much corrective bandwidth the system can absorb without secondary harm, legitimacy fracture, or capture.  
**Envelope constraint:** `0 < α / K < ε(t)`.

ε tightens when any of the following worsen:
- delay τ ↑
- proxy reliance/contamination η ↑
- legitimacy sensitivity ℓ ↑
- coupling/cascade risk ρ ↑
- reversibility burden RB ↑
- confidence conf ↓
- Goodhart resistance GR ↓

### τ — Delay (effective)
Time from action to observable and perceived effect, decomposed into:
- τₘ: measurement/reporting/audit lag
- τₐ: actuation/implementation lag
- τₗ: legitimacy/perception/reaction lag  
**Rule:** when τ rises, cadence must fall before gain may rise.

### H — Hysteresis
Deadband thresholds preventing oscillatory “thrash” in governance tuning (entry/exit thresholds; no rapid toggling).

### Dwell-time
A minimum time (or verification window count) that must pass after a parameter or mode change before further tuning.

### Coupling strength (ρ)
The strength of cross-domain or cross-agent propagation. Higher ρ implies tighter ε, slower α, and cascade defense prioritization over local optimization.

---

## 4) Measurement Safety (GR) and Incentives (IC)

### Goodhart’s Law (operational)
When a measure becomes a target, it loses reliability.

### GR — Goodhart Resistance
A governance property: the system’s capacity to use metrics without letting incentives, gaming, or proxy substitution decouple measurement from reality.

### Goodhart Tag (metric permission state)
A required tag on any metric-like input:
- **GR-Safe** — low gaming surface; triangulated; audited
- **GR-Watch** — moderate risk; requires counter-metrics and monitoring
- **GR-High-Risk** — cannot be primary justification; strong incentive surface
- **GR-Captured** — evidence of decoupling/gaming; metric quarantined for justification

### Metric Charter
A required definition lock + method spec for any governance-used metric, including:
- definition + scope
- sampling/measurement method
- known failure modes
- update cadence
- ownership
- change log and disclosure rules

### IC — Incentive Compatibility (mechanism safety)
A property of a governance mechanism: it should not structurally reward manipulation, drift, extraction, proxy gaming, or burden dumping.  
IC failure is indicated when gaming is profitable and weakly detectable.

### IC stress
A condition where incentives make drift/capture strategies dominant. Response: narrow scope, increase audits/holdouts, slow α, freeze K escalation, and reopen renegotiation if capture persists.

---

## 5) Information Integrity Terms (states, confidence, proxies)

### Information state (integrity state machine)
Required label for governance-relevant information:
- **Verified**
- **Partially Verified**
- **Unverified**
- **Contradictory**
- **Corrupted**
- **Symbolically Inverted**

### Confidence (conf)
A declared uncertainty scalar for governance-relevant claims: `conf ∈ [0,1]`.  
Low conf triggers containment bias, tightens ε, slows α.

### Proxy (η)
An indirect measure used when direct signals are unavailable. Proxy reliance increases contamination risk and Goodhart vulnerability.

### Provenance integrity
Traceability of where information came from and how it was transformed.

### Audit anchor
A reality check not easily gamed: random audits, holdouts, delayed outcome checks, independent review channels.

---

## 6) Reversibility Classes (R0 / R1 / R2)

### R0 — Zero-commitment action
No rights/access changes, no binding commitments, no structural reconfiguration. Default safe class, especially under uncertainty.

### R1 — Reversible commitment
A bounded commitment permitted only with rollback scaffolding:
- rollback procedure and authority
- rollback window and bounded cost
- scope bound (blast radius)
- review checkpoints and verification criteria
- appeal path + SLA
- sunset clause
- burden distribution note (who pays rollback cost)

### R2 — Irreversible / non-redressable action
Cannot be undone within bounded time/cost, or causes non-redressable exclusion/harm, or destroys oversight/evidence.  
**R2 is prohibited inside the reflexive control loop.** If R2 appears “necessary,” correction halts and renegotiation/exit is required.

### Reversibility burden (RB)
A tuple representing rollback strain:
`RB = (T_revert, C_revert, Scope_revert, Residual_harm_bound)`

---

## 7) Ethics & Reciprocity Terms

### Reciprocity field
A relational load map of:
- obligations owed
- benefits received
- dependencies created
- burdens carried
- risks externalized
- procedural load imposed

Persistent imbalance is a pre-collapse signature and contributes to SDI/MDI/LDI.

### Ethical debt
Accumulated burden externalization or harm that is “parked” rather than repaired; often shows up as “temporary” exceptions that never unwind.

### Dignity constraint
A non-negotiable requirement that governance not degrade persons into instruments, targets, or expendable inputs.

### Consent integrity
The condition that participation and agreement are real (not coerced, fatigued, or manipulated), with appealability and contestation preserved.

### EP — Ethics of Presence (non-extraction boundary)
A strict prohibition on:
- identity inference, profiling, diagnosis, archetyping
- latent meaning extraction about persons/groups
- coercive psychological manipulation
- symbolic binding of individuals as governance substrate  
EP violations trigger immediate halt and review.

---

## 8) Multi-Agent Dynamics Terms

### Agent
A situated actor with objectives (plural and evolving), incentives, constraints, informational position, power, legitimacy exposure, and harm/obstruction capacity.

### Asymmetry
Power, information, and burden differences among agents. In RGT, asymmetry is a stability variable—not a nuisance to normalize away.

### Coalition capture
A pattern where coalitions harden rapidly, invoke unity to block oversight, or exploit metrics/definitions to suppress dissent.

### Information parity protocol
A requirement (when decisions have shared impact) to align:
- definitions and timelines
- uncertainty disclosure
- criteria traceability
- “what would change my mind” commitments
- publication of counter-arguments (when safe)
- audited claims when metrics justify decisions

### RSE — Reflexive Stability Equilibrium
A constraint-respecting stability condition for multi-agent systems:
a feasible joint action profile where no agent can unilaterally deviate in a way that remains feasible while improving their objective representation **without** increasing drift, degrading GR, breaching IC safety, or harming legitimacy repairability.

RSE is not optimality; it is **bounded coexistence under constraints**.

---

## 9) Protocol Terms (governance, crisis, information resilience)

### Governance Protocol
The operational decision spine: observation → interpretation → calibration → correction → verification, with reversibility and capture triggers enforced.

### Crisis Mode
A declared posture (not discretionary) entered when instability, delay, overload, or capture risk crosses thresholds. Crisis does not relax constraints; it **tightens them**.

### Freeze (crisis stage)
R0-dominant action class intended to stop amplification, preserve evidence, and prevent irreversible commitments.

### Containment bias
A conservative posture under uncertainty: prefer smaller scope, slower cadence, R0 actions, audits, and reversible scaffolds.

---

## 10) Communication & Agent Interface Terms

### Claim status labels
Mandatory labels used by RGT Sage:
- **Known**
- **Inferred**
- **Uncertain**
- **Underdetermined**

### “What would change my mind”
A required update rule listing concrete evidence, audits, thresholds, or signals that would revise the recommendation.

### Escalation trigger
A condition that forces renegotiation, scope reduction, suspension, handoff, partition, or shutdown—rather than continued tuning.

### Refusal mode
Agent behavior when constraints forbid the requested action: explain the violated constraint and offer safer, non-extractive alternatives.

---

## 11) Mathematical Terms (minimal, agent-facing)

### Drift energy V(D)
An energy-like scalar used to evaluate stability over verification windows, commonly:
`V(D) = 1/2 · DᵀD`  
Persistent failure of ΔV < 0 indicates instability requiring containment or renegotiation.

### Small-gain intuition
A stability idea for interconnected loops: when cross-loop amplification is too high (effective gain ≥ 1), interactions can runaway; therefore coupling defense and cadence reduction dominate.

---

## 12) Deprecations and Alignment Notes (v2.0 → v2026.03)

The following terms are **deprecated for RGT Sage** unless explicitly needed in a separate annex:

- “Presence Mode / Articulation Mode” as a governance requirement (retain only if used in a phenomenology-specific module; do not treat as mandatory for general governance outputs).
- “Interpretation Ladder” as a fixed five-level output format (RGT Sage uses the **Standard Output Template** instead; ladders may be optional presentation only).
- “Fairness lower-bound theorem” phrasing (retain the concept—fairness and legitimacy are coupled—but avoid claiming a theorem unless the formal proof is included in a math appendix with explicit assumptions).

---

## 13) Closing Note

This glossary is the **agent-facing canonical vocabulary** for RGT Sage aligned to **RGT Core v2026.03**.

If a file introduces a term not present here, either:
- add it here (with a crisp definition and constraints), or
- explicitly reference the Core file where the term is canonically defined.
