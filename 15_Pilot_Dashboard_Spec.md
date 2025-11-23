---
version: 2.0.0
build: 2025-11-23T00:00:00
format: markdown
type: dual
name: Pilot Dashboard Specification
description: Specification for a reflexive, multi-layer municipal permitting dashboard under RGT v2.0 (Architecture v0.2)
architecture_version: RGT_System_Architecture_v0_2
role: dashboard
---

# Pilot Dashboard Specification (v2.0)

This specification defines the **metrics, visualizations, alerts, and reflexive diagnostics** required for the Municipal Permitting Pilot Dashboard under **Reflexive Governance Theory (RGT) v2.0**.

The dashboard provides:
- real-time visibility into system stability,
- early-warning drift detection,
- α/K envelope compliance,
- Safety Envelope monitoring,
- fairness & legitimacy tracking,
- symbolic field signals,
- metabolic load management,
- reversibility analysis,
- and Reflexive Data Loop (RDL) health indicators.

---

# 1. Dashboard Purpose

The dashboard is designed to:

### **1.1 Support reflexive governance**
Real-time monitoring of the system’s internal state across L0–L4.

### **1.2 Detect instability early**
Identify drift acceleration, envelope violations, or symbolic contradictions.

### **1.3 Guide decision posture**
Show when to operate in:
- **Presence Mode** (exploratory, reflective, uncertain contexts)  
- **Articulation Mode** (execution, clear conditions)

### **1.4 Protect legitimacy and fairness**
Track fairness foundations and legitimacy floor.

### **1.5 Prevent overload**
Monitor metabolic load and cadence integrity.

### **1.6 Ensure reversibility**
Classify decisions by reversibility class and highlight risks.

---

# 2. Core Dashboard Panels

The v2.0 dashboard includes seven major panels:

1. **Stability Panel (α/K Envelope)**
2. **Drift Panel (L1 Drift Indices)**
3. **Fairness & Legitimacy Panel**
4. **Symbolic Coherence Panel**
5. **Metabolic Load Panel**
6. **Reversibility & Risk Panel**
7. **Reflexive Data Loop (RDL) Health Panel**

Each panel includes:
- metrics (from Metrics Appendix v2.0),
- thresholds,
- early-warning alerts,
- recommended posture adjustments.

---

# 3. Stability Panel — α/K Envelope

Monitors real-time control posture.

| Metric | Definition | Target Range | Alert Threshold |
|--------|------------|--------------|------------------|
| α (Sensitivity) | Speed of recognition | 0.4–0.8 | <0.3 or >0.9 |
| K (Intensity) | Strength of corrective force | 0.4–0.8 | <0.3 or >0.9 |
| α/K Ratio | Ethical stability condition | 0.6–1.6 | Outside range |
| Envelope Compliance | % of decisions inside bounds | ≥95% | <90% |

### **Visualization**
- Donut chart: % envelope compliance  
- Line graph: α/K drift over time  
- Heat bar: sensitivity vs intensity load  

### **Recommended Actions**
- High K → reduce intensity (RDL-2)  
- Low α → increase sensitivity (RDL-3)  
- Envelope violation → immediate escalation  

---

# 4. Drift Panel — L1 Drift Indices

Tracks all five drift types:

| Drift Index | Definition | Target | Alert |
|-------------|------------|--------|--------|
| SDI | Structural Drift | <0.3 | >0.45 |
| NDI | Normative Drift | <0.3 | >0.45 |
| SyDI | Symbolic Drift | <0.3 | >0.45 |
| LDI | Legitimacy Drift | <0.3 | >0.45 |
| MDI | Metabolic Drift | <0.3 | >0.45 |

### **Drift Acceleration**
\[
D' < 0.1
\]

Dashboard displays:
- slopes,  
- recent spikes,  
- common correlates (missing data, fairness drops, symbolic contradictions).  

### **Visualization**
- Multi-line drift graph  
- Drift radar  
- Trend panel with color-coded warnings  

---

# 5. Fairness & Legitimacy Panel

Tracks compliance with the Fairness–Legitimacy theorem.

## **5.1 Fairness Index (Fₜ)**  
Goal: Fₜ ≥ 0.7  

## **5.2 Legitimacy Index (Lₜ)**  
Goal: Lₜ ≥ 0.75  

### **5.3 Participation Parity (pₜ)**
Measures equity in involvement and impact.

### **5.4 Fairness → Legitimacy Bound**
\[
\Delta L \ge \gamma_f \Delta F
\]

### Visualization
- Dual-axis fairness/legitimacy graph  
- Lower-bound indicator  
- Parity bar  

---

# 6. Symbolic Coherence Panel

Tracks meaning and narrative alignment.

| Metric | Definition | Target | Alert |
|--------|------------|--------|--------|
| SCI | Symbolic Coherence Index | ≥0.65 | <0.5 |
| Emotional Climate | Affective stability | Stable | Negative trend |
| Narrative Harmony | Alignment of communication | High | Contradictions detected |

### Visualization
- Coherence scorecard  
- Word cloud mismatch detector  
- Narrative timeline with drift flags  

---

# 7. Metabolic Load Panel

Tracks staff and system cadence health.

| Metric | Target | Alert |
|--------|--------|---------|
| MLI (Metabolic Load Index) | ≤0.7 | ≥0.85 |
| Compression Spike Count | ≤2/week | ≥3/week |
| Dilation Recovery Time | <36 hours | >48 hours |

Visualization:
- load trend line  
- cadence oscillation graph  
- compression/dilation tracker  

---

# 8. Reversibility & Risk Panel

Reversibility-class aware decision display.

### **Classes**
- **R0 — Reversible**  
- **R1 — Partially Reversible**  
- **R2 — Irreversible**  

Each decision gets a badge.

### **Rules**
- R1 → simulate via RDL-4  
- R2 → simulate + canary test via RDL-6  
- Irreversible at low coherence → blocked by Safety Envelope  

Visualization:
- decision list with reversibility class  
- risk heatmap  
- threshold alerts  
- envelope compliance indicator  

---

# 9. Reflexive Data Loop (RDL) Health Panel

Shows real-time loop stability.

| RDL | Status | Condition |
|------|--------|-----------|
| RDL-1 Drift Sentry | Contractive | Must be <1.0 gain |
| RDL-2 Gain Scheduling | Active | K reduces under uncertainty |
| RDL-3 Cadence Control | Active | α increases under ambiguity |
| RDL-4 Off-Policy Eval | Mandatory | All R1/R2 |
| RDL-5 Multi-Objective | Stable | Balanced tradeoffs |
| RDL-6 Canary Gate | Armed | High-risk only |
| RDL-7 Reversibility | Active | Full traceability |
| RDL-8 Metabolic Cadence | Stable | Load < threshold |

Visualization:
- Loop wheel diagram  
- Stability indicator (green/yellow/red)  
- Contractive gain readout  

---

# 10. Alerts System

Alerts activate under:

### **Envelope Violations**
- α/K outside range  
- ε-pressure ≥ 0.6  
- metabolic overload  

### **Drift Acceleration**
- D' ≥ 0.15  

### **Fairness/Legitimacy Collapse**
- Fₜ < 0.6  
- Lₜ < 0.7  

### **Symbolic Disruptions**
- SCI < 0.5  
- contradictory narrative events  

### **Reversibility Risks**
- Approving R2 without RDL-4  
- High-stakes decision under low coherence  

### **Mode Drift**
- Using Articulation Mode under high uncertainty  

---

# 11. Recommended Actions Panel

Based on conditions:
- shift to Presence Mode  
- reduce intensity (K↓)  
- increase sensitivity (α↑)  
- slow throughput  
- activate decompression cycles  
- run simulation (RDL-4)  
- run canary (RDL-6)  
- pause irreversible decisions  
- initiate symbolic field repair  

---

# 12. Audit & Logging Integration

The dashboard logs all:
- envelope violations,  
- drift spikes,  
- fairness/legitimacy dips,  
- reversibility-class actions,  
- metabolic overloads,  
- symbolic mismatches,  
- mode errors.  

Each log includes:
- timestamp,  
- decision node,  
- triggering indices,  
- RDL pathways,  
- operator mode,  
- recommended correction.

---

# 13. Summary

The Pilot Dashboard provides the **reflexive monitoring core** for RGT v2.0 in municipal permitting.

It ensures:
- stability,  
- fairness,  
- reversibility,  
- meaning coherence,  
- load balance,  
- ethical posture,  
- and reflexive learning.

A system that can **see itself clearly** can correct itself before destabilization.

