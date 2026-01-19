---
version: 2026.03.0
build: 2026-01-17T00:00:00-08:00
format: markdown
type: policy
name: RGT Sage — Security Policy
authority: canonical
scope: repository
rgt_core_version: RGT Core v2026.03
---

# Security Policy — RGT Sage

This document defines how **security, vulnerability handling, and incident response** are approached within the **RGT Sage** ecosystem.

Security in RGT Sage is treated as a **governance constraint**, not a purely technical concern.  
Failures of security are treated as **legitimacy, trust, and reversibility risks**, not just bugs.

---

## 1. Security Philosophy

RGT Sage security is governed by five principles:

1. **Containment before correction**  
2. **Reversibility before remediation**  
3. **Legitimacy before disclosure speed**  
4. **Human accountability before automation**  
5. **Transparency without harm amplification**

Security responses must **preserve trust and system integrity**, even under pressure.

---

## 2. Scope

This policy applies to:

- The **RGT Sage Agent** system prompts and behaviors
- All files within the RGT Sage repository
- Evaluation, enforcement, and integration artifacts
- Any deployed or experimental RGT Sage instances
- Documentation, manifests, and generated outputs

It does **not** govern external systems that merely reference RGT Sage.

---

## 3. What Counts as a Security Issue

A security issue includes (but is not limited to):

### 3.1 Technical Risks
- Unauthorized access paths
- Prompt injection or instruction override
- Leakage of private, sensitive, or restricted information
- Unintended persistence or memory
- Boundary bypass between advisory and authority roles

### 3.2 Governance & Ethical Risks
- Automation creep (AI acting with implied authority)
- Irreversibility exposure without safeguards
- Coercive framing or manipulation vectors
- Identity inference or profiling (EP violations)
- Metric gaming pathways (Goodhart capture)
- Hidden escalation or authority laundering

### 3.3 Interpretive & Symbolic Risks
- Misrepresentation of RGT as a decision engine
- Outputs framed as mandates or “final answers”
- Collapse of plural interpretations into a single “official” meaning
- Use of Sage outputs to justify harm or exclusion

These are treated as **security failures**, not “misuse.”

---

## 4. Reporting a Vulnerability

### 4.1 How to Report

If you discover a security issue:

- **Do not disclose it publicly**
- **Do not attempt to exploit it**
- **Do not escalate impact for demonstration**

Instead, report it via the repository’s designated security contact or issue channel marked **SECURITY**.

Include:
- a clear description of the issue,
- affected files or behaviors,
- conditions required to reproduce,
- potential impact (technical + governance),
- whether reversibility is compromised.

### 4.2 What *Not* to Include

Do **not** include:
- personal data,
- exploit code beyond minimal reproduction,
- speculative blame,
- assumptions of intent.

Security reporting is a **protective act**, not an accusation.

---

## 5. Response & Handling Process

All reported issues follow a **constraint-first response path**:

### Step 1 — Containment
- Freeze affected pathways
- Disable risky behaviors if necessary
- Prevent escalation or replication

### Step 2 — Classification
Each issue is classified across four axes:
- **Severity** (Low / Moderate / High / Critical)
- **Reversibility impact** (R0 / R1 / R2 exposure)
- **Legitimacy risk** (None / Local / Systemic)
- **Boundary breach** (Technical / Ethical / Human–AI)

### Step 3 — Analysis
- Root-cause analysis (technical + governance)
- Drift and cascade assessment
- Check for incentive or framing vulnerabilities

### Step 4 — Remediation
- Prefer reversible fixes
- Avoid silent behavior changes
- Update protocols or constraints if needed
- Add tests or enforcement traces where appropriate

### Step 5 — Disclosure
- Share findings proportionally
- Avoid harm amplification
- Document in the Patch Log if structural

---

## 6. Disclosure Policy

RGT Sage follows **responsible disclosure**.

- Critical vulnerabilities are disclosed **after containment**
- Ethical or governance vulnerabilities may require **contextual explanation**
- Not all issues require public disclosure if doing so increases harm

Transparency is balanced against **symbolic and legitimacy risk**.

---

## 7. Security vs. Safety vs. Ethics

In RGT Sage:

- **Security** = protection against boundary breach
- **Safety** = protection against harm under uncertainty
- **Ethics** = protection against extraction, coercion, or dehumanization

These domains overlap.  
A failure in one often propagates to the others.

---

## 8. Human–AI Boundary Enforcement

Security includes strict enforcement of:

- advisory-only posture,
- human override at all times,
- refusal under irreversibility pressure,
- no hidden authority escalation,
- no latent psychological inference.

Any erosion of this boundary is treated as **Critical**.

---

## 9. Non-Retaliation & Good-Faith Reporting

RGT Sage explicitly supports **good-faith security research**.

- No retaliation for responsible disclosure
- No punitive framing of reporters
- No attribution without consent

Security requires trust. Trust requires protection.

---

## 10. Ongoing Security Practices

The RGT Sage project maintains security through:

- periodic architecture reviews,
- adversarial prompt testing,
- drift and capture simulations,
- evaluation suites and enforcement traces,
- quarterly refresh cycles.

Security is treated as **continuous governance**, not a one-time fix.

---

## 11. Final Principle

> A secure system is not one that never fails —  
> it is one that can **notice failure early**,  
> **contain damage**,  
> and **correct itself without losing legitimacy**.

That principle governs all security decisions in RGT Sage.

---

**RGT Sage Security Policy**  
*Constraint-first.  
Legitimacy-aware.  
Human-accountable.*