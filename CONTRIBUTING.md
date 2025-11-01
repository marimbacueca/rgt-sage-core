# CONTRIBUTING.md

::: info
RGT Sage — Reflexive Mathematics Core **v1.0** (updated 2025-11-01)  
Synced with Annexes **E–M**, **§28 Reflexive Simulation Suite**, and **§51 Mathematical Calibration Report**.
:::


## How to Contribute
- Keep proofs in Annexes; link code to §28.
- Respect **SR^r** (Safe-Reflection) and rank windows.
- Validate invariants (ΔV_R≤0, ρ(Γ)<1, H_R↑) in PR checks.

## Pull Request Checklist
- [ ] Proof sketch or reference to Annex theorem
- [ ] Simulation snippet (seeded) showing invariants
- [ ] Ethics gate call (Π_C) where applicable
- [ ] Stability note (ρ(Γ) estimate + dwell-time)

## Code Style
- Matplotlib only for charts; no seaborn; one chart per figure; no forced colors.
- Provide parameter tables (μ, L, τ, α, η*, ρ*).
