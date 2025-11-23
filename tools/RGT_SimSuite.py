
---

# ✅ 2. `RGT_SimSuite.py`  
### **READY-TO-PASTE MARKDOWN**

```md
# RGT_SimSuite.py

```python
"""
RGT Simulation Suite — RGT Sage Core (v2.0)

This suite provides simulation functions for demonstrating key 
mathematical dynamics within Reflexive Governance Theory:

1. Cone Gate (Projection Dynamics)
2. Small-Gain Stability Loop
3. Extragradient Dynamics (Two-Step Reflexive Learning)
4. Reflexive Entropy Evolution

These simulations allow researchers and practitioners to experiment 
with RGT's mathematical structures without modifying governance logic.
They are aligned with:

- RGT System Architecture v0.2
- Mathematical Foundations Appendix (v2.0)
- Metrics Appendix (v2.0)
- α/K Stability Envelope
- Reflexive Data Loops (RDL 1–8)

This module is safe, reversible, and purely didactic.
"""

import numpy as np


# ------------------------------------------------------------
# 1. CONE GATE DYNAMICS — Projection onto a convex cone
# ------------------------------------------------------------
def cone_gate_simulation(x0, P, steps=20):
    """
    Simulates repeated projection onto a convex cone K.

    Recurrence:
        x_{t+1} = P(x_t)

    Arguments:
        x0   = initial vector
        P    = projection operator
        steps = number of iterations

    Returns:
        history of x_t
    """
    x = x0.copy()
    history = [x.copy()]
    for _ in range(steps):
        x = P(x)
        history.append(x.copy())
    return np.array(history)


# ------------------------------------------------------------
# 2. SMALL-GAIN STABILITY LOOP — Contraction Mapping
# ------------------------------------------------------------
def small_gain_loop(x0, Gamma, steps=20):
    """
    Simulates a linear reflexive loop:

        x_{t+1} = Γ x_t

    Stability condition:
        ρ(Γ) < 1

    Returns a trajectory showing contraction or divergence.
    """
    x = x0.copy()
    history = [x.copy()]
    for _ in range(steps):
        x = Gamma @ x
        history.append(x.copy())
    return np.array(history)


# ------------------------------------------------------------
# 3. EXTRAGRADIENT DYNAMICS — RDL Learning Operator
# ------------------------------------------------------------
def extragradient_dynamics(x0, grad, tau, steps=20):
    """
    Two-step extragradient update:

        y_t = x_t - τ ∇f(x_t)
        x_{t+1} = x_t - τ ∇f(y_t)

    Used for modeling calibration, learning, and reflexive updates
    inside RDL frameworks.

    Arguments:
        x0   = initial point
        grad = gradient function
        tau  = step size
    """
    x = x0.copy()
    history = [x.copy()]
    for _ in range(steps):
        y = x - tau * grad(x)
        x = x - tau * grad(y)
        history.append(x.copy())
    return np.array(history)


# ------------------------------------------------------------
# 4. REFLEXIVE ENTROPY EVOLUTION — Information Dynamics
# ------------------------------------------------------------
def reflexive_entropy_evolution(H0, decay, steps=20):
    """
    Models entropy evolution in a closed reflexive system.

    Recurrence:
        H_{t+1} = H_t - decay * H_t

    Requires:
        0 ≤ decay ≤ 1 for stability
    """
    H = H0
    history = [H]
    for _ in range(steps):
        H = H - decay * H
        history.append(H)
    return np.array(history)
