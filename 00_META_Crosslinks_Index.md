---
version: 2.1.0
build: 2026-01-18T00:00:00-08:00
format: markdown
type: dual
name: Crosslinks Index
description: RGT Sage Core — cross-file index for Reflexive Governance Theory (Sage) v2.x, mapping logical slots to conceptual roles. Designed to survive renames, prefix refactors, and module removals.
architecture_version: RGT_Sage_Architecture_v0_3
role: index
---

# Crosslinks Index (v2.1)

This index is the **canonical map** of the RGT Sage Core corpus.

Each number represents a **logical slot** in the architecture, **independent of filename suffixes** (e.g., `_v1_0`, `_v2_0`).  
The *source of truth* for a file’s state is:

1) its YAML frontmatter (`version`, `role`, etc.), and  
2) its conceptual slot in this index.

> **Naming convention (recommended):**  
> Use prefixes by layer/function for clarity and sorting:  
> `00_META_*`, `01_THEORY_*`, `02_ARCH_*`, `03_PROTOCOLS_*`, `04_APP_*`, `05_TOOLS_*`, `06_LOGS_*`  
> Slot numbers below remain stable even if prefixes change.

---

## Root

- **Root → `RGT_Sage_Operating_Instructions.md`**  
  Core usage and navigation for the agent, including:
  - how to interpret “slots” and file roles,
  - how to route questions (theory vs protocol vs application),
  - safety boundaries and refusal logic,
  - how to cite and how to label uncertainty.

---

## 00–02 — META & SYSTEM HISTORY

- **00 → system prompt / operating constraints**  
  **Recommended filename:** `00_META_System_Prompt.md`  
  Role:
  - agent identity + boundaries,
  - “math is instrumental, not sovereign,”
  - human authority and escalation rules,
  - how to handle uncertainty, drift, and coercion risk.

- **01 → learning log / change ledger**  
  **Recommended filename:** `00_META_Learning_Log.md` (or `06_LOGS_Learning_Log.md`)  
  Role:
  - major corrections, conceptual upgrades, and “why we changed it,”
  - notable failure modes and mitigations,
  - deprecations and module removals.

- **02 → chronology / evolution map**  
  **Recommended filename:** `00_META_Chronology_Map.md`  
  Role:
  - development sequence (major forks, merges, releases),
  - key architectural transitions (e.g., Architecture v0.2 → v0.3).

---

## 03–08 — CORE THEORY & FOUNDATIONS

- **03 → glossary (canonical term authority)**  
  **Recommended filename:** `01_THEORY_Glossary.md`  
  Role:
  - definitions for all key terms and indices:
    - drift indices (SDI/NDI/SyDI/LDI/MDI),
    - α/K/ε/τ/H primitives,
    - reversibility classes (R0–R2),
    - GR (Goodhart Resistance), IC stress,
    - RDLs and layer model (L0–L5, if used in Sage).

- **04 → crisis protocol**  
  **Recommended filename:** `03_PROTOCOLS_Crisis_Protocol.md`  
  Role:
  - crisis declaration, freeze/snapshot/clarify/stabilize/exit stages,
  - non-bypass invariants (EP/dignity, reversibility, oversight, GR quarantine),
  - hysteresis + dwell-time requirements.

- **05 → subsystem gap analysis**  
  **Recommended filename:** `00_META_Subsystem_Gap_Analysis.md`  
  Role:
  - what is complete vs stubbed,
  - what needs proofs vs needs pilots vs needs UI/tooling,
  - priority backlog for the Sage agent’s evolution.

- **06 → metrics & gates appendix (tables)**  
  **Recommended filename:** `05_TOOLS_Metrics_and_Gates_Tables.md`  
  Role:
  - “reference tables” for:
    - drift thresholds and confidence bands,
    - α/K envelope regimes,
    - GR tags and reinstatement rules,
    - IC stress triggers,
    - legitimacy and reciprocity indicators,
    - RDL health indicators.

- **07 → reciprocity & resource flows**  
  **Recommended filename:** `03_PROTOCOLS_Ethics_and_Reciprocity.md` (or `01_THEORY_Reciprocity_Addendum.md`)  
  Role:
  - reciprocity fields (burden/benefit/obligation asymmetry),
  - fairness logic under power asymmetry,
  - non-extractive constraints and repair pathways.

- **08 → information resilience framework**  
  **Recommended filename:** `03_PROTOCOLS_Information_Resilience.md`  
  Role:
  - information states + confidence declaration,
  - GR tags, metric charters, audits/holdouts/counter-metrics,
  - capture triggers (GR collapse, “no drift” anomaly, symbolic inversion),
  - anti-coercion handling of disagreement.

---

## 09–13 — ETHICAL & MATHEMATICAL MODULES

### 09 — Comparative Systems (DEPRECATED / REMOVED)
- **09 → comparative systems module (Chile/USA)**  
  **Status:** **Removed** from the active Sage core (outdated + not agent-essential).  
  If retained for archival, move to an archive folder and mark as:
  - `role: archive`
  - `status: deprecated`
  - and explicitly date-stamp its empirical assumptions.

> **Replacement approach (recommended):**  
> If comparative analysis is needed later, generate *on-demand* case studies under `04_APP_*` with explicit:
> scope, date range, and evidence provenance — instead of keeping a fixed comparative file in core.

---

- **10 → ethics of presence (EP) / non-extraction boundary**  
  **Recommended filename:** `03_PROTOCOLS_Ethics_of_Presence_EP.md`  
  Role:
  - non-extractive interpretation limits,
  - presence vs articulation boundaries (if used),
  - hard-stop triggers for identity inference / profiling / diagnosis,
  - “do not launder power through interpretation.”

- **11 → phenomenological / qualitative signals protocol**  
  **Recommended filename:** `01_THEORY_Phenomenological_Tech_Protocol.md` (or `03_PROTOCOLS_Phenomenological_Tech_Protocol.md`)  
  Role:
  - how qualitative and experiential signals enter safely,
  - how they map to layers/indices without coercion,
  - reversibility-first handling of sensitive interpretive material.

- **12 → economic reflexivity module**  
  **Recommended filename:** `01_THEORY_Economic_Reflexivity_Module.md`  
  Role:
  - value-flow topology (material/informational/symbolic/relational/metabolic),
  - economic drift + reciprocity coupling,
  - anti-extraction constraints in institutional economics.

- **13 → mathematical foundations appendix**  
  **Recommended filename:** `01_THEORY_Mathematical_Foundations.md`  
  Role:
  - stability theorems and envelope conditions (α/K/ε under delay/coupling),
  - GR and capture formalization,
  - minimal multi-agent equilibrium notion (RSE),
  - “ethics over math” boundary stated formally.

---

## 14–16 — PILOT MODULES (REMOVED FROM CORE)

### 14–16 — Municipal Permitting Pilot (DEPRECATED / REMOVED)
- **14 → pilot charter**  
- **15 → pilot dashboard spec**  
- **16 → pilot risks register**  

**Status:** **Removed** from the active Sage core (pilot-specific + outdated).  
If needed later, reintroduce as **optional pilots** under `04_APP_*` with clear version/date and local assumptions.

> **Replacement approach (recommended):**  
> Keep pilots as *separate bundles*:
> - `04_APP_PILOT_<Domain>_Charter.md`  
> - `04_APP_PILOT_<Domain>_Dashboard_Spec.md`  
> - `04_APP_PILOT_<Domain>_Risks_Register.md`  
> so Sage core remains domain-agnostic.

---

## 17 — THIS FILE

- **17 → crosslinks index**  
  **Recommended filename:** `00_META_Crosslinks_Index.md`  
  Role:
  - canonical architecture map,
  - governs stable slot meanings across renames,
  - declares module lifecycle (active / optional / deprecated / archived).

---

# Recommended “Best Setup” After Updates (Minimal + Durable Core)

If you want the leanest, most future-proof Sage core that still feels “complete,” keep:

**00_META**
- System Prompt
- Crosslinks Index (this file)
- Learning Log
- Gap Analysis
- Chronology (optional but useful)

**01_THEORY**
- Glossary
- Mathematical Foundations (with “instrumental math” boundary)
- Economic Reflexivity (optional; keep if you actually use it)

**03_PROTOCOLS**
- Crisis Protocol
- Governance Protocol (if you have one in Sage)
- Information Resilience
- Ethics & Reciprocity
- Ethics of Presence (EP)

Everything else becomes:
- `04_APP_*` for case studies / pilots (on-demand, date-scoped),
- `05_TOOLS_*` for tables, validators, templates,
- `06_LOGS_*` for audits and evolution records.

This keeps the agent **domain-agnostic**, current, and harder to “rot.”

---

# Maintenance Notes

## Versioning
- Filenames may retain legacy suffixes, but **canonical version lives in YAML** inside each file.
- When a file changes role (e.g., core → pilot → archive), update both:
  - YAML (`role`, `status` if present), and
  - this index.

## Deprecation Rules
- If a module is removed from core:
  1) mark it deprecated in its YAML,
  2) move it to an `ARCHIVE/` or `PILOTS/` grouping,
  3) note the removal in the Learning Log (Slot + reason + date).

## Renaming / Prefix Refactor
- You may rename files to the prefix taxonomy (`00_META`, `01_THEORY`, etc.) without breaking the architecture,
  as long as the slot meaning (00–17) stays consistent.

## Tooling Expectations
- Sage should rely on **this index + YAML frontmatter + Glossary + Metrics Tables** as the structural spine.
- Any “system validation suite” should confirm:
  - required core files exist,
  - deprecated modules are not referenced as authoritative,
  - cross-file references resolve cleanly (no dead links).

---
