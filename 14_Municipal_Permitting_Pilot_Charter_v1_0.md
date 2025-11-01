# 14_Municipal_Permitting_Pilot_Charter_v1_0.md

::: info
RGT Sage — Reflexive Mathematics Core **v1.0** (updated 2025-11-01)  
Synced with Annexes **E–M**, **§28 Reflexive Simulation Suite**, and **§51 Mathematical Calibration Report**.
:::


## Objective
Pilot a reflexive permitting workflow minimizing backlog while preserving fairness and stability.

## Success Criteria
- **Stability:** ρ(Γ)<1 across agency interconnections; ΔV_R≤0 per accepted decision.  
- **Ethics:** EG cone feasibility ≥ 95% of decisions; HF not sacrificed below α=0.5.  
- **Learning Arrow:** H_R non-decreasing.

## Protocol
1. Daily Γ estimation; auto-alarm at ρ(Γ)≥0.95.  
2. Rank window r* documented; only **SR^r** reflection allowed.  
3. Decision gate: Π_C(EG_vec), Safe check, then actuation.  
4. Dwell-time control: enforce T_d ≥ C/(1−ρ_*).

## Reporting
Weekly §28-style plots; quarterly calibration rollup (§51).