---
version: 2026.03.1
build: 2026-01-18T00:00:00-08:00
format: markdown
type: meta
name: RGT Sage — Patch Log
authority: canonical
scope: agent
rgt_core_version: RGT Core v2026.03
architecture_version: RGT_Sage_Architecture_v0_3
role: change_log
---

# RGT Sage — Patch Log

This file records **meaningful changes** to the RGT Sage Agent:  
theory alignment, behavioral constraints, safety rules, analytical capabilities, and interface expectations.

It is **not** a commit log.  
It is a *governance-grade change history* focused on **why something changed**, **what shifted**, and **what users should do differently as a result**.

> **Rule:**  
> If a change affects interpretation, constraints, or agent behavior, it must appear here.

---

# =======================================
# How to Read This File
# =======================================

Each entry includes:

- **Version** — semantic, aligned to RGT Core when applicable  
- **Change Type** — Structural / Theoretical / Behavioral / Safety / Interface  
- **Summary** — what changed, in plain language  
- **Rationale** — why the change was necessary  
- **Implications** — how this affects usage, outputs, or interpretation  
- **Migration Notes** — what to update, remove, or stop relying on

This file is ordered **most recent first**.

---

# =======================================
# v2026.03.1 — January 18, 2026
# =======================================

**Change Type:** Structural · Behavioral · Safety  
**Status:** Active (Canonical)

### Summary
Major consolidation and alignment update bringing RGT Sage fully in sync with **RGT Core v2026.03**.  
Clarifies advisory boundaries, reversibility enforcement, Goodhart resistance, and output discipline.

### Rationale
Prior versions allowed ambiguity between:
- analysis vs authority,
- recommendation vs decision,
- metrics as signals vs metrics as targets.

This patch resolves those ambiguities by making **constraints load-bearing** at the agent level.

### Key Changes
- Introduced **Output Rubric v2026.03.1** as a binding response contract.
- Hardened **R0/R1/R2 reversibility gate** (R2 explicitly forbidden in-loop).
- Formalized **claim-status labeling** (Known / Inferred / Uncertain / Underdetermined).
- Required **information state + confidence** for governance-relevant inputs.
- Elevated **Goodhart Resistance (GR)** and **Metric Charters** from best practice to permission gate.
- Clarified **escalation triggers** and “what would change the mind” as mandatory output elements.
- Removed legacy examples and pilots not aligned with current scope (e.g., municipal permitting).

### Implications
- RGT Sage outputs are now more conservative, slower by design, and more explicit about uncertainty.
- Dashboards, KPIs, and indices lose authority without GR tagging and charters.
- Users should expect fewer “answers” and more **bounded option sets with rollback logic**.

### Migration Notes
- Stop relying on implicit certainty or optimization language.
- Update any prompts expecting decisive prescriptions.
- Ensure references point to **RGT Core v2026.03** files only.

---

# =======================================
# v2026.03.0 — January 17, 2026
# =======================================

**Change Type:** Theoretical · Interface  
**Status:** Superseded (see v2026.03.1)

### Summary
Initial synchronization of RGT Sage with RGT Core v2026.03.

### Rationale
RGT Core introduced:
- Information Resilience,
- Governance Protocol hard gates,
- Ethics & Reciprocity as structural constraints.

RGT Sage required alignment to avoid drift between theory and application.

### Key Changes
- Updated System Prompt with constraint-first ordering (L0–L5).
- Integrated Information Resilience and Governance Protocol triggers.
- Clarified human–AI boundary language.

### Implications
- Sage shifted away from narrative synthesis toward constraint articulation.
- Increased explicit references to drift domains and protocols.

### Migration Notes
- Fully superseded by v2026.03.1.
- Do not reference this version independently.

---

# =======================================
# v2.1.x — Late 2025 (Pre-2026 Series)
# =======================================

**Change Type:** Transitional  
**Status:** Deprecated

### Summary
Incremental refinements during transition from Architecture v0.2 to v2026.

### Rationale
Exploratory period while RGT moved from conceptual framework to governance-grade system.

### Key Characteristics (Historical)
- Mixed advisory and interpretive tones.
- Weaker reversibility enforcement.
- Early RDL usage without full protocol binding.
- Pilot-heavy (municipal, comparative systems).

### Implications
- Outputs from this era may:
  - over-index on explanation,
  - under-specify rollback,
  - rely on examples no longer canonical.

### Migration Notes
- Treat outputs from this period as **conceptual only**.
- Do not reuse without revalidation against v2026.03 constraints.

---

# =======================================
# v2.0.0 — November 23, 2025
# =======================================

**Change Type:** Foundational  
**Status:** Historical Reference

### Summary
Formalization of RGT Sage as a distinct agent with structured files, glossary, and crosslinks.

### Rationale
Need to separate:
- RGT theory development,
- from agent behavior and application support.

### Key Contributions
- Introduced layered reasoning model.
- Established early glossary and crosslinks index.
- Defined Sage as non-decision-making assistant.

### Implications
- Served as the conceptual base for later hardening.
- Many definitions have since been refined or replaced.

### Migration Notes
- Use only for historical understanding.
- Do not treat as current operational guidance.

---

# =======================================
# Deprecations & Removals (Cumulative)
# =======================================

The following content types are **explicitly deprecated** and should not be reintroduced without review:

- Municipal permitting pilots and dashboards
- Country-to-country comparative case studies used as canonical references
- Optimization-oriented recommendations
- Implicit moral judgments or legitimacy assertions
- Unlabeled certainty or confidence inflation
- Metrics without GR tagging and charters
- Irreversible action framing inside the control loop

---

# =======================================
# Forward Update Rules
# =======================================

A new patch entry is required when:

- a constraint is added, removed, or reordered,
- reversibility rules change,
- ethical boundaries (EP) are tightened or expanded,
- output structure or required sections change,
- a file is promoted to canonical authority,
- a domain is explicitly removed from scope.

Patch entries must be written **for humans**, not machines.

---

# =======================================
# Closing Note
# =======================================

This Patch Log is part of RGT Sage’s **legitimacy infrastructure**.

If changes are not visible, traceable, and explainable,
the system itself is drifting.

When in doubt:  
**log the change, explain the why, and slow the cadence.**
