# 04_CrisisProtocol_v1.md

::: info
RGT Sage — Reflexive Mathematics Core **v1.0** (updated 2025-11-01)
This file was patched to align with Annexes **E–M**, the **§28 Reflexive Simulation Suite**, and the **§51 Mathematical Calibration Report**.
:::


## Reflexive Crisis Protocol — v1.0 Enhancements
1. **Stability Check:** compute ρ(Γ) with latest coupling estimates; if ≥1, trigger *Stabilize* routine (reduce cross-gain, increase dwell time).
2. **Safe Gate Enforcement:** require SR^r for any auto-escalation logic; block unguarded reflection.
3. **Entropy Monitor:** ensure H_R non-decreasing; if ΔH_R<0, roll back last step and quarantine schedule K(t).
4. **Ethics Gate:** project EG_vec onto cone C(α) before any high-impact actuation.

## Runbook (Fast Path)
- **Detect:** breach in MSI band or H_R invariant.
- **Diagnose:** inspect Γ, DR trends, η, ρ.
- **Act:** apply *Gain Dampening* (η←η/2), *Cross-Coupling Cut* (lower γ_ij), re-evaluate ρ(Γ).
