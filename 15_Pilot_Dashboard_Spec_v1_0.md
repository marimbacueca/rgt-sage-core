# 15_Pilot_Dashboard_Spec_v1_0.md

::: info
RGT Sage — Reflexive Mathematics Core **v1.0** (updated 2025-11-01)  
Synced with Annexes **E–M**, **§28 Reflexive Simulation Suite**, and **§51 Mathematical Calibration Report**.
:::


## KPIs & Invariants
| KPI | Formula | Target |
|---|---|---|
| Stability Radius | ρ(Γ) | < 1 (warn ≥0.9) |
| Potential Descent | ΔV_R | ≤ 0 (violation=red) |
| Reflexive Entropy | H_R | Monotone ↑ |
| Cone Feasibility | HF − α‖others‖ | ≥ 0 (α=0.5) |
| Safe Coverage | accepted steps with Safe | 100% |
| Rank Window Use | max rank used / r* | ≤ 1 |
| Dwell Time | T_d observed | ≥ C/(1−ρ_*) |

## Views
- **Stability:** ρ(Γ) timeline with plateau annotations.  
- **Ethics:** cone scatter w/ projection overlay.  
- **Entropy:** H_info, V_R, H_R traces.  
- **Solver:** extragradient convergence plot (‖z_k−z*‖).