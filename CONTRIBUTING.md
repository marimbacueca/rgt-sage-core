---
version: 2026.03.0
build: 2026-01-17T00:00:00-08:00
format: markdown
type: meta
name: RGT Sage — Contributing Guide
authority: canonical
scope: agent + human collaborators
rgt_core_version: RGT Core v2026.03
role: contribution-governance
---

# Contributing to RGT Sage

Thank you for contributing to **RGT Sage**, the advisory agent implementation of  
**Reflexive Governance Theory (RGT)**.

RGT Sage is not a conventional software project.
It is a **governance reasoning system** whose primary obligation is to preserve:

- legitimacy,
- reversibility,
- ethical boundaries,
- epistemic plurality,
- and human authority.

This guide defines **how contributions are proposed, evaluated, integrated, or rejected**.

---

# ========================================
# 1. Who This Guide Is For
# ========================================

This document applies to:

- maintainers of the RGT Sage agent,
- contributors proposing theory, protocol, or application changes,
- reviewers evaluating updates for alignment with RGT Core,
- humans collaborating with RGT Sage on extensions or pilots.

It does **not** apply to end-users seeking advice from the agent.

---

# ========================================
# 2. Contribution Philosophy
# ========================================

RGT Sage evolves through **deliberate, constraint-respecting refinement**, not rapid iteration.

Contributions must:

- reduce ambiguity without erasing plurality,
- strengthen constraints without increasing rigidity,
- improve clarity without centralizing authority,
- preserve reversibility,
- avoid optimization pressure.

**More structure is not always better.**
Unnecessary formalization is treated as a risk.

---

# ========================================
# 3. What Can Be Contributed
# ========================================

### Accepted Contribution Types

You may propose:

- theory refinements (kernels, definitions, failure modes),
- protocol clarifications or extensions,
- analytical methods or evaluation scaffolds,
- application patterns or integration templates,
- test suites, scorecards, or enforcement traces,
- documentation that improves interpretability or safety.

### Explicitly Out of Scope

The following are not accepted:

- policy prescriptions framed as universal solutions,
- irreversible governance recommendations,
- authority-granting logic for AI systems,
- behavioral manipulation techniques,
- profiling, archetyping, or identity inference methods,
- optimization frameworks that bypass legitimacy or ethics.

---

# ========================================
# 4. Contribution Requirements (Hard Gates)
# ========================================

Every contribution must satisfy **all** of the following.

## 4.1 Constraint Alignment

The proposal must explicitly state:

- which RGT Core files it depends on,
- which constraints it strengthens or clarifies,
- whether it introduces any new risks.

If a contribution weakens an existing constraint, it will be rejected.

---

## 4.2 Reversibility Declaration

Each contribution must include a reversibility classification:

- **R0** — documentation, clarification, analysis (default)
- **R1** — structural change with explicit rollback path
- **R2** — irreversible change (**not accepted**)

R2 proposals are rejected automatically.

---

## 4.3 Epistemic Status Disclosure

Contributors must label claims as:

- **Established** (convergent support),
- **Inferred** (model-dependent),
- **Exploratory** (hypothesis or scaffold),
- **Open** (unresolved / contested).

Undeclared certainty is treated as epistemic harm.

---

## 4.4 Goodhart & Incentive Check

If a contribution introduces metrics, indices, or scoring:

- a Goodhart tag must be proposed,
- a draft metric charter must be included,
- incentive and gaming risks must be discussed.

Metric-driven contributions without GR analysis will be rejected.

---

# ========================================
# 5. Contribution Structure
# ========================================

All contributions must include:

1. **Intent Summary**  
   What problem this addresses and why it matters.

2. **Scope & Boundaries**  
   What this does *not* attempt to solve.

3. **Constraint Impact**  
   Which RGT constraints are affected and how.

4. **Reversibility & Rollback**  
   Classification (R0/R1) and rollback path if applicable.

5. **Risks & Failure Modes**  
   Including misuse, misinterpretation, or capture risk.

6. **Cross-References**  
   Exact file paths and sections touched.

---

# ========================================
# 6. Review Process
# ========================================

All contributions undergo **constraint-first review**.

Reviewers evaluate:

- alignment with RGT Core,
- preservation of human authority,
- reversibility and containment,
- clarity without coercion,
- interaction with existing protocols.

A contribution may be:

- **Accepted**
- **Accepted with Revision**
- **Deferred** (needs more grounding)
- **Rejected** (with constraint-based explanation)

Rejection is not a judgment of quality.
It is a safeguard.

---

# ========================================
# 7. Style & Language Standards
# ========================================

Contributions must be:

- precise and non-theatrical,
- free of persuasive rhetoric,
- explicit about uncertainty,
- respectful of plural interpretations,
- written for auditability and longevity.

Avoid:

- urgency framing,
- moralizing language,
- claims of inevitability,
- “best practice” assertions without context.

---

# ========================================
# 8. Human–AI Boundary
# ========================================

Contributions must not:

- grant RGT Sage decision authority,
- reduce friction for automation of governance,
- obscure human accountability,
- present AI judgment as neutral or superior.

Any erosion of the human–AI boundary is grounds for rejection.

---

# ========================================
# 9. Documentation & Traceability
# ========================================

When updating or adding files:

- update the Crosslinks Index if roles change,
- avoid duplicating canonical definitions,
- reference the Glossary for terminology,
- add a short entry to the Patch Log.

Traceability is mandatory.

---

# ========================================
# 10. Conduct & Ethics
# ========================================

All contributors are bound by:

- the **RGT Sage Code of Conduct**,
- the **Ethics of Presence (EP)** constraints,
- non-extractive, dignity-preserving norms.

Contributions that violate EP or enable harm laundering
will be removed.

---

# ========================================
# 11. Disagreement & Forking
# ========================================

Disagreement is legitimate and expected.

If alignment cannot be reached:

- the contribution may remain deferred,
- or be documented as an open question,
- or be developed externally without being merged.

Forced convergence is prohibited.

---

# ========================================
# 12. Closing Note
# ========================================

Contributing to RGT Sage means contributing to a **governance ecology**, not a feature set.

If a proposal improves speed but weakens legitimacy, it should not be merged.
If it increases coherence but erases dissent, it should not be merged.
If it optimizes outcomes but bypasses ethics, it must not be merged.

RGT Sage evolves slowly on purpose.

That slowness is a form of care.
