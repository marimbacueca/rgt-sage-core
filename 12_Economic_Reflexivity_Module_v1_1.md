# 12_Economic_Reflexivity_Module_v1_1.md

::: info
RGT Sage — Reflexive Mathematics Core **v1.0** (updated 2025-11-01)  
Synced with Annexes **E–M**, **§28 Reflexive Simulation Suite**, and **§51 Mathematical Calibration Report**.
:::


## Purpose
Model resource allocation and policy coupling as **Variational Inequalities (VI)** with reflexive ethics and stability constraints.

## Mathematical Core Links
- **VI Existence/Uniqueness** (Annex B): Stampacchia; strong monotonicity μ and Lipschitz L.
- **Reflexive Game Theory** (Annex K): finite-depth beliefs → infinite-depth limit; extragradient solver.
- **Stability** (Annex J): interconnections bounded via ρ(Γ)<1.
- **Ethics Gate** (Annex G): feasibility cone C(α) on EG_vec.

## Solver Recipe (Ops Default)
1. Choose depth d s.t. q^d ≤ ε (belief contraction).  
2. Run **projected extragradient** with stepsize τ < μ/L².  
3. Enforce Safe & cone gate each iteration; log (μ, L, τ, ε).

## Policy Parameters
- Default α=0.5 (HF dominance).  
- Initial η*= (1−a_max)/(2 L_K ‖C_P‖), ρ*=(a_max+1)/2 (Annex F).  
- Stability target: ρ(Γ)≤0.9; dwell-time T_d ≥ C/(1−ρ_*).

## Outputs
- Allocation vector x*, beliefs t*, invariant checks (ΔV_R≤0, H_R↑).