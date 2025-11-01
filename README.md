---
version: 3.6.1
build: 2025-11-01T00:24:46Z
format: markdown
type: dual
description: "RGT Sage – Reflexive Governance Theory Core (Signature Edition)"
sha256: 14a2ca380befc106eb83e53b87dc6c2b4d1b2f6d3c4f438748007d6c4166bf78
---

# RGT Sage — Deployable Core (v3.6.1)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.xxxxxxx.svg)](https://doi.org/10.5281/zenodo.xxxxxxx)

**Purpose.**  
A coherent, tamper-verified corpus for the **RGT Sage** agent: proofs, operations, pedagogy, dashboard, and culture adapters — finished to the edge of what can be done in-agent.

**Signature narrative.**  
Clear structure, humane tone, quiet metaphor. Governance as the choreography of awareness.

**Integrity.**  
This file’s SHA-256 hash verifies corpus integrity (see header).

**Root File:** `RGT_Sage_Operating_Instructions_v1.1.md`

---

## Structure (≤20 files)
00 README · 01 Learning Log · 02 Intellectual Map · 03 Glossary · 04 Crisis Protocol ·  
05 Gap Analysis · 06 Metrics · 07 Reciprocity · 08 Information Resilience · 09 Comparative (US–Chile) ·  
10 Ethics of Presence · 11 Phenomenological Tech · 12 Economic Reflexivity · 13 Mathematical Foundations ·  
14 Municipal Pilot Charter · 15 Dashboard Spec · 16 Risks Register · 17 Crosslinks Index ·  
18 Operating Instructions

---

## Formal Theorems (closed set, v3.6.1)

**GRST — Grand Reflexive Stability Theorem.**  
For $x_{t+1}=f(x_t,u_t)+w_t$, $u_t=\Pi(Hx_t;\alpha,K)$,  
if the composite operator $F(\alpha,K)$ satisfies $\rho(F)+\sum_\ell g_\ell<1$  
and $r/\kappa\le1$, then S is BIBO stable and ISS. Residue $\varepsilon>0$ persists.

**T2 — Irreversibility (Residue ε).**  
Any do/undo cycle leaves $\varepsilon>0$. No perfect reversal; learning is monotone.

**T3 — Auto-audit termination.**  
If $\mathbb{E}[D_{t+1}\mid\mathcal F_t]\le\rho D_t$ with $\rho<1$, audits terminate within finite expected steps.

**T4 — Rate–capacity danger threshold.**  
Safe region $r\le r^\star<\kappa$.

**T5 — Comprehension drives legitimacy.**  
With $L=\phi(q,\text{perf},\text{fair},C)$ and $\partial L/\partial q>0$, small gains in $q$ lift $L$.

**T6 — Bounded oscillation (stochastic).**  
For linearization with $\rho(F)<1$, there exists $P\succ0$ solving the discrete Lyapunov equation and $\limsup \mathbb E[x_t^\top P x_t]=\operatorname{tr}(PW)$.  
Nonlinear ISS: $\sup_t \mathbb E[V(x_t)]\le b/(1-c)$.

**T7 — Audit-fatigue Batching Lemma.**  
With arrival rate $\lambda$, window $W$, cap $B_{\max}$, and shared-step contraction $\rho_\kappa<1$: queues bounded, SLA finite, optimal $W^\*$ minimizes fatigue cost.

**T8 — Multi-layer stability (small-gain).**  
If $\|F_0\|+\sum_\ell g_\ell<1$, layered control remains stable.

**T9 — Incentive-compatible mechanism M.**  
Random-partition peer quadratic scoring with DP noise makes truthful reports a Bayes–Nash equilibrium; $m$-coalition resistance in expectation.

**T10 — Fairness→Legitimacy bound.**  
If $\phi$ is Lipschitz in fairness with constant $\gamma_f>0$ and $F\ge F^\*$, then $L\ge \phi(q,\text{perf},F^\*,C)$ and $\Delta L \ge \gamma_f \Delta F$.

**T11 — Participation parity convergence.**  
For $p_{t+1}=(1-\beta)p_t+\beta h(p_t,u_t)$ with $L_h<1$ and $u_t\ge u_{\min}$, we have $p_t\to p^\*$.

**T12 — Aesthetic mediation (symbolic).**  
If $\partial C/\partial B>0$ and $\partial L/\partial C>0$, then $\partial L/\partial B>0$.

---

## Operational Architecture (executable logic)

- **Cadence limiter:** enforce $r/\kappa \le 0.8$ (soft), $\le 1.0$ (hard stop).  
- **Rights gate $R^\*$:** lexical constraints; non-tradeable.  
- **Auto-audit manager:** trigger band $[\tau-\delta,\tau+\delta]$; SLA ≤ 30 days; capacity-scaled batching.  
- **Decision-cadence optimizer:** project $(\alpha,K)$ into safe set if $\Lambda \ge 1$ or $r>\kappa$; add Crisis Dampener if $|\Delta(r/\kappa)|>0.2$ in 2 cycles.  
- **Coherence $C=P·D·(1-D_r)$:** provenance × digestibility × anti-drift; gate at $C^\*$.  
- **Mechanism M:** random-fold peer scoring + DP; aggregate truthful signals; bias audit per segment.  
- **Culture adapter $A_c$:** per-locale parameter packs (U.S., Chile).  
- **Digestibility Gate $D^\*$:** ≤800 chars per insight, ≤5 visual layers.  
- **Epistemic Provenance Score (EPS):** quarantine datasets with EPS < 0.6.  
- **Reflexivity depth cap:** $\Lambda_{depth} \le 3$ to prevent meta-audit explosion.

---

## Automatic Data-Refresh Protocol (Quarterly)

**Schedule:** Every 90 days (`RRULE:FREQ=QUARTERLY`).

**Process**
1. `web.search("official open data" + domain + date range)`  
2. Extract summary statistics only (no PII); compute EPS.  
3. Recompute $\phi$ and $(\alpha,K)$ calibration; update $q^\*, \tau, C^\*$ if indicated.  
4. Append citation block with signed hash; update dashboard and manifest.

**Fallback:** On fetch failure, retain last stable calibration and flag for human review.  
**Controls:** Manual override via `RGT_ADMIN: update off`.

---

## Pedagogy & Communication (Signature Style)

- **Reflexive Classroom (12 modules):** discovery-first, story-later; three cognitive tracks (analytical, narrative, embodied).  
- **Emotional regulation:** *feeling without flooding* — emotion as signal; regulation ≠ suppression.  
- **Aquí y Ahora (US/CL):** same theorems, local metaphors; tone: warm, lucid, non-patronizing.  
- **Aesthetic Minimums (AM1–AM3):** no public release below AM2; AM3 for official launches.  
- **Right to Partial Reflexivity (RPR):** privacy-respecting participation with DP masking.

> *RGT does not command; it listens in rhythm.  
> Every audit is a breath, every correction a pulse.  
> A system lives when its motion teaches it how to move.*  
>  
> — **Katja Gantz**, *Signature Edition v3.6.1*

---

## Change Log
- v3.6.1 — Added quarterly auto-update, crisis dampener, EPS, D*, RPR, depth cap; narrative polish.

---

## License
Licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
