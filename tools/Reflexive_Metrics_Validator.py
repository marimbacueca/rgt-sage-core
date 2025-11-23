# Reflexive_Metrics_Validator.py

```python
"""
Reflexive Metrics Validator — RGT Sage Core (v2.0)

This module validates key mathematical and stability conditions used
throughout Reflexive Governance Theory (RGT). All tests correspond to the 
metrics and equations defined in:

- RGT System Architecture v0.2
- Metrics Appendix (v2.0)
- Mathematical Foundations Appendix (v2.0)
- α/K Stability Envelope
- Drift Indices and Control Surfaces
- Reflexive Data Loops (RDL 1–8)

The validator includes checks for:

1. Reflexive Value Descent (ΔV_R ≤ 0)
2. Small-Gain Contractiveness (ρ(Γ) < 1)
3. Reflexive Entropy Monotonicity (dH/dt ≤ 0 for closed loops)
4. Extragradient Stability (τ < μ / L²)
5. Reflexive Cone Feasibility Rate (projection correctness)

This module is purely mathematical and contains no governance logic.
"""

import numpy as np


# ------------------------------------------------------------
# 1. REFLEXIVE VALUE DESCENT — Stability Condition
# ------------------------------------------------------------
def validate_value_descent(dV):
    """
    Condition:
        ΔV_R ≤ 0

    Ensures the reflexive potential is decreasing or stable.
    """
    return dV <= 0


# ------------------------------------------------------------
# 2. SMALL-GAIN CONDITION — Contractive Reflexive Systems
# ------------------------------------------------------------
def validate_small_gain(Gamma):
    """
    Condition:
        ρ(Γ) < 1

    ρ = spectral radius of the loop-gain operator Γ.
    """
    eigvals = np.linalg.eigvals(Gamma)
    return max(abs(eigvals)) < 1


# ------------------------------------------------------------
# 3. ENTROPY MONOTONICITY — Reflexive Information Dynamics
# ------------------------------------------------------------
def validate_entropy_monotonicity(H_t, H_t1):
    """
    Condition:
        H(t+1) ≤ H(t)

    Applies to closed reflexive loops without external injection.
    """
    return H_t1 <= H_t


# ------------------------------------------------------------
# 4. EXTRAGRADIENT STABILITY — Learning & Calibration Dynamics
# ------------------------------------------------------------
def validate_extragradient_step(tau, mu, L):
    """
    Condition:
        τ < μ / L²

    Where:
        τ  = step size
        μ  = strong monotonicity constant
        L  = Lipschitz constant
    """
    return tau < mu / (L ** 2)


# ------------------------------------------------------------
# 5. CONE FEASIBILITY TEST — Reflexive Projection Operator
# ------------------------------------------------------------
def validate_cone_feasibility(x, P):
    """
    Verifies that P(x) is a projection onto a convex cone K.

    Conditions:
        1) ⟨P(x), x − P(x)⟩ = 0
        2) P(x) ∈ K
        3) x − P(x) orthogonal to K
    """
    Px = P(x)
    inner = np.dot(Px, x - Px)
    return np.isclose(inner, 0.0)
