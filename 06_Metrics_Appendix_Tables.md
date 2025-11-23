---
version: 2.0.0
build: 2025-11-23T00:00:00
format: markdown
type: dual
name: Metrics Appendix (Tables)
description: Comprehensive metrics, indices, thresholds, and stability values for Reflexive Governance Theory v2.0 (Architecture v0.2)
architecture_version: RGT_System_Architecture_v0.2
role: reference
---

# Metrics Appendix (v2.0)

This Appendix provides the **complete metrics, indices, thresholds, and diagnostic tables** for evaluating the stability, integrity, fairness, legitimacy, symbolic coherence, metabolic load, and governance performance of any system operating under **Reflexive Governance Theory v2.0**.

All metrics here are used by:
- the **Audit & Logging System v2.0**,  
- **Reflexive Data Loops (RDLs)**,  
- **α/K Stability Envelope**,  
- **Crisis Protocol**,  
- **Pilot Dashboards**,  
- and the **RGT Sage Engine**.

---

# 1. L0 Metrics — Data, Provenance & Information Integrity

## **1.1 Signal Quality Index (SQI)**

| Component | Definition | Scale | Notes |
|----------|------------|--------|-------|
| Resolution | Granularity of observation | 0–1 | Higher = better |
| Noise | Random corruption of signal | 0–1 | Lower = better |
| Timeliness | Recency relative to decision cadence | 0–1 | Higher = better |
| Context Fit | Appropriateness to domain | 0–1 | Avoid context overlap |
| Missingness | Portion of missing data | 0–1 | Lower = better |

### **Composite SQI**
\[
SQI = w_r R + w_n(1-N) + w_t T + w_c C + w_m(1-M)
\]

Minimum threshold for governance use: **SQI ≥ 0.65**

---

## **1.2 Provenance Integrity Index (PII)**

| Element | Requirement | Score |
|---------|-------------|--------|
| Source Identity | Transparent & known | 0 / 1 |
| Uncertainty Bounds | Specified in L0 | 0 / 1 |
| Bias Class | Declared | 0 / 1 |
| Transformation Chain | Fully documented | 0 / 1 |
| Accessibility | Auditable | 0 / 1 |

\[
PII = \frac{\text{Sum}}{5}
\]

Minimum threshold: **PII ≥ 0.8**

---

## **1.3 Narrative / Symbolic Coherence Index (SCI)**

| Factor | Measurement |
|--------|-------------|
| Symbol alignment | Degree to which symbols/narratives reinforce institutional purpose |
| Emotional climate | Collective affective environment |
| Ritual continuity | Stability of shared practices |
| Interpretive alignment | Shared meaning across groups |

Scale: **0–1**, with **SCI ≥ 0.6** required for legitimacy stability.

---

# 2. L1 Metrics — Indices, Drift & System State

## **2.1 Fairness Index (Fₜ)**

| Submetric | Description |
|-----------|-------------|
| Distributional parity | Equity of outcomes |
| Access parity | Equity of opportunities |
| Participation parity | Equitable involvement |
| Absence of bias | Structural or procedural |

Scale: **0–1**

---

## **2.2 Legitimacy Index (Lₜ)**

| Component | Definition |
|----------|------------|
| Procedural clarity | Transparent processes |
| Interpretive coherence | Actions make sense to stakeholders |
| Symbolic validity | Symbols align with governance |
| Reversibility | Ability to undo harmful actions |
| Fairness foundation | Derived from Fₜ |

Scale: **0–1**

### **Fairness–Legitimacy Lower Bound**
\[
\Delta L \ge \gamma_f \Delta F
\]
where **γ₍f₎ ≈ 0.4–0.7**

---

## **2.3 Drift Indices**

### **Structural Drift Index (SDI)**
Mismatch between formal architecture and lived practice.

### **Normative Drift Index (NDI)**
Divergence of values, norms, and expectations.

### **Symbolic Drift Index (SyDI)**
Degradation of narrative/aesthetic meaning structures.

### **Legitimacy Drift Index (LDI)**
Decline in trust and perceived validity.

### **Metabolic Drift Index (MDI)**
Chronic overload or underactivation.

Each scaled **0–1**

### Drift Acceleration
\[
D' = \frac{d(\text{drift})}{dt}
\]

Crisis threshold: **D' ≥ 0.15**

---

# 3. L2 Metrics — Control, α/K Stability & RDL Performance

## **3.1 α/K Stability Envelope**

### **Sensitivity (α)**
0–1 (higher = faster recognition)

### **Intensity (K)**
0–1 (higher = stronger corrective force)

### **Envelope Safety Condition**
\[
0.6 \le \frac{\alpha}{K} \le 1.6
\]

Violations → activate Crisis Protocol.

---

## **3.2 Loop Gain (gₗ) for RDL Stability**

Total reflexive loop gain:
\[
G = \sum_{\ell=1}^8 g_\ell
\]

### **Small-Gain Condition**
\[
G < 1
\]

If violated:
- reduce K (via RDL-2),  
- increase α (via RDL-3),  
- decrease decision throughput.

---

## **3.3 Reflexive Data Loop Health Matrix**

| RDL | Loop Function | Stability Requirement |
|------|----------------|------------------------|
| RDL-1 | Drift Sentry | Contractive on all drift indices |
| RDL-2 | Gain Scheduling | K must reduce under uncertainty |
| RDL-3 | Cadence Control | α must rise with uncertainty |
| RDL-4 | Off-Policy Eval | All irreversible decisions tested |
| RDL-5 | Multi-Objective | Tradeoffs must be explicit |
| RDL-6 | Canary / Ethics Gate | High-risk tested on small sets |
| RDL-7 | Reversibility | Full provenance & undo analysis |
| RDL-8 | Metabolic Cadence | Decision load ≤ metabolic buffer |

---

# 4. L3 Metrics — Governance & Votation

## **4.1 Decision Throughput (Tₜ)**

\[
T_t = \frac{\text{Decisions}}{\text{Unit Time}}
\]

Healthy range depends on domain, but **compression spikes** signal overload.

---

## **4.2 Reversibility Compliance Index (RCI)**

| Class | Requirement |
|--------|-------------|
| Reversible | No special constraint |
| Partial | RDL-4 recommended |
| Irreversible | RDL-4 + RDL-6 mandatory, α↑, K↓ |

\[
RCI = 1 - \text{Rate of envelope violations}
\]

---

## **4.3 Consensus Field Coherence Index (CFCI)**

Measures structured alignment of:
- preferences,  
- disagreements,  
- coalitions,  
- competing narratives.

Scale: **0–1**.

---

# 5. L4 Metrics — Sage Interface & Human-AI Partnership

## **5.1 Mode Alignment Score (MAS)**

| Mode | Conditions |
|------|------------|
| Presence Mode | Exploration, uncertainty, drift detection |
| Articulation Mode | Execution, clarity, high-certainty operations |

MAS determines whether the agent/human interface matches the appropriate phase.

Sustained mismatches → **mode drift**.

---

## **5.2 Explanation Transparency Index (ETI)**

Measures:
- clarity,  
- structure,  
- rationale,  
- constraints,  
- alternative paths.

Scale: **0–1**.

Minimum acceptable: **ETI ≥ 0.75**

---

## **5.3 Consent Boundary Compliance (CBC)**

All uses of:
- personal heuristics,  
- sensitive info,  
- inference  
must pass the **Consent Threshold**.

Violation = CBC score drops.

---

# 6. Safety Envelope Metrics

## **6.1 Epsilon-Boundary Pressure (εₚ)**

\[
\varepsilon_p = f(\text{identity risk}, \text{coherence loss}, \text{irreversibility})
\]

Crisis threshold: **εₚ ≥ 0.6**

---

## **6.2 Context Overlap Score (COS)**

0 = isolated  
1 = fully overlapping (unsafe)

Threshold: **COS ≤ 0.3**

---

## **6.3 Ethical Uncertainty Index (EUI)**

High EUI → increase α, lower K.

Threshold: **EUI ≥ 0.5** triggers caution.

---

## **6.4 Metabolic Load Index (MLI)**

\[
MLI = \frac{\text{Cognitive Load}}{\text{Metabolic Capacity}}
\]

Stable range:
- **MLI ≤ 0.7**

Crisis threshold:
- **MLI ≥ 0.85**

---

# 7. Stability Criteria Summary

| Criterion | Formal Condition | Interpretation |
|-----------|------------------|----------------|
| GRST-v2.0 | \(F(\cdot)\) stays in Lyapunov region | Drift remains bounded |
| α/K Envelope | \(0.6 \le \alpha/K \le 1.6\) | Ethical control |
| Small-Gain | \(G < 1\) | Loop interaction stability |
| Fairness→Legitimacy | \(\Delta L \ge \gamma_f \Delta F\) | Fairness stabilizes legitimacy |
| Aesthetic Mediation | \(\partial L/\partial B > 0\) | Symbolic clarity improves legitimacy |
| Reversibility Corridor | No irreversible decisions at low coherence | Safety guarantee |

---

# 8. Summary

This Appendix establishes the **quantitative backbone** of RGT v2.0.

These metrics ensure:
- safe α/K control,  
- stable drift detection,  
- coherent narratives,  
- legitimate governance,  
- symbolic integrity,  
- manageable metabolic load,  
- ethical reversibility,  
- and contractive reflexive loops.

The combined system enables a governance model that **learns faster than it destabilizes** and restores stability through reflexivity rather than force.

