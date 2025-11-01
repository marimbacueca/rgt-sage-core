#!/usr/bin/env python3
"""
RGT_SimSuite.py — Reflexive Simulation Suite (v1.0)
Implements the 4 mini-sims aligned to Annexes G, J, K, and M.

Usage:
  python RGT_SimSuite.py --demo cone      # Annex G
  python RGT_SimSuite.py --demo stability # Annex J
  python RGT_SimSuite.py --demo game      # Annex K
  python RGT_SimSuite.py --demo entropy   # Annex M
  python RGT_SimSuite.py --all            # run all sims

Outputs:
  - PNG figures per sim in ./out/
  - JSON summary in ./out/sim_summary.json
"""

import os
import json
import argparse
from math import sqrt
import numpy as np

try:
    import matplotlib.pyplot as plt
    HAVE_PLOT = True
except Exception:
    HAVE_PLOT = False

OUTDIR = "out"

def ensure_outdir():
    os.makedirs(OUTDIR, exist_ok=True)

# ---------- Helper: projection onto scaled second-order cone ----------
# Cone C(alpha): {(h,u) | h >= alpha*||u||, h >= 0}. Map to standard SOC.
def proj_cone_scaled(h, u, alpha=0.5):
    u = np.asarray(u, dtype=float)
    y0 = h / alpha
    y1 = u
    normy1 = np.linalg.norm(y1)
    if normy1 <= y0 and y0 >= 0:
        py0, py1 = y0, y1
    elif normy1 <= -y0:
        py0, py1 = 0.0, np.zeros_like(y1)
    else:
        s = 0.5 * (normy1 + y0)
        if normy1 == 0:
            py0, py1 = s, np.zeros_like(y1)
        else:
            py0, py1 = s, s * (y1 / normy1)
    ph = alpha * py0
    pu = py1
    return ph, pu

def demo_cone(alpha=0.5, N=300, seed=7):
    np.random.seed(seed)
    m = 5  # EG_vec = (HF, OA, CP, RV, CL)
    EGs = np.random.rand(N, m)
    EGs[:,0] *= 0.4  # reduce HF to force projections
    grads = -np.abs(np.random.randn(N, m))  # descent directions (negative components)
    accepted = []
    projected = []
    for i in range(N):
        h = EGs[i,0]; u = EGs[i,1:]
        ph, pu = proj_cone_scaled(h, u, alpha=alpha)
        vproj = np.concatenate([[ph], pu])
        dv = float(np.dot(grads[i], vproj))
        acc = dv <= 0
        accepted.append(bool(acc))
        projected.append(vproj.tolist())
    accept_rate = float(np.mean(accepted))
    # Plot
    if HAVE_PLOT:
        import matplotlib.pyplot as plt
        ensure_outdir()
        r_before = np.linalg.norm(EGs[:,1:], axis=1)
        r_after  = np.linalg.norm(np.array(projected)[:,1:], axis=1)
        plt.figure()
        plt.scatter(r_before, EGs[:,0], s=12, alpha=0.6, label="before")
        plt.scatter(r_after,  np.array(projected)[:,0], s=12, alpha=0.6, label="after")
        xb = np.linspace(0, r_before.max()*1.05, 100)
        plt.plot(xb, alpha*xb)
        plt.xlabel("||others||"); plt.ylabel("HF")
        plt.title("Annex G — Vector EG Cone Gate")
        plt.legend(loc="best")
        plt.savefig(os.path.join(OUTDIR, "annexG_cone.png"), dpi=160, bbox_inches="tight")
        plt.close()
    return {"demo":"cone","alpha":alpha,"N":N,"accept_rate":accept_rate}

def demo_stability(T=40, e0=(1.0,0.6)):
    e0 = np.array(e0, dtype=float)
    M_stable = np.array([[0.82, 0.12],[0.10, 0.80]])
    M_unstab = np.array([[0.90, 0.35],[0.35, 0.90]])
    def run(M):
        e = np.zeros((T+1, 2)); e[0]=e0
        for t in range(T): e[t+1] = M @ e[t]
        V = (e**2) @ np.array([1.0,1.0])
        return V
    V_st = run(M_stable); V_un = run(M_unstab)
    if HAVE_PLOT:
        import matplotlib.pyplot as plt
        ensure_outdir()
        plt.figure()
        plt.plot(V_st, label="stable V_tot")
        plt.plot(V_un, label="unstable V_tot")
        plt.xlabel("t"); plt.ylabel("V_tot")
        plt.title("Annex J — Small-Gain Stability (2-loop)")
        plt.legend(loc="best")
        plt.savefig(os.path.join(OUTDIR, "annexJ_stability.png"), dpi=160, bbox_inches="tight")
        plt.close()
    return {"demo":"stability","T":T,"V_st_end":float(V_st[-1]),"V_un_end":float(V_un[-1])}

def demo_game(K=120):
    A = np.array([[2.0, 0.6],[0.6, 1.6]])
    eig = np.linalg.eigvals(0.5*(A + A.T)).real
    mu = float(np.min(eig)); L = float(np.linalg.norm(A,2))
    tau = 0.5*mu/(L**2)
    b  = np.array([-1.0, 0.5])
    z  = np.array([2.0, -2.0])
    hist = [float(np.linalg.norm(z))]
    for k in range(K):
        y = z - tau*(A@z + b)
        z = z - tau*(A@y + b)
        hist.append(float(np.linalg.norm(z)))
    if HAVE_PLOT:
        import matplotlib.pyplot as plt
        ensure_outdir()
        plt.figure()
        plt.plot(hist)
        plt.xlabel("iteration"); plt.ylabel("||z||")
        plt.title("Annex K — Extragradient Convergence")
        plt.savefig(os.path.join(OUTDIR, "annexK_game.png"), dpi=160, bbox_inches="tight")
        plt.close()
    return {"demo":"game","mu":mu,"L":L,"tau":float(tau),"norm0":hist[0],"norm_end":hist[-1]}

def softmax(s, tau=1.0):
    s = np.array(s, dtype=float)
    s = s - s.max()
    e = np.exp(s/tau)
    return e/np.sum(e)

def demo_entropy(T=50, tau_s=1.0, lam=2.0):
    q_star = np.array([0.5,0.5]); s = np.array([0.8,0.2])
    H_info_list=[]; V_R_list=[]; H_R_list=[]
    for t in range(T):
        q = softmax(s, tau=tau_s)
        V_R = 0.5*np.sum((q - q_star)**2)
        H_info = float(-(q*np.log(q+1e-12)).sum())
        H_R = float(H_info + lam*(1.0 - V_R))
        H_info_list.append(H_info); V_R_list.append(float(V_R)); H_R_list.append(H_R)
        grad = q - q_star
        s = s - 0.4*grad
    if HAVE_PLOT:
        import matplotlib.pyplot as plt
        ensure_outdir()
        plt.figure()
        plt.plot(H_info_list, label="H_info")
        plt.plot(V_R_list, label="V_R")
        plt.plot(H_R_list, label="H_R")
        plt.xlabel("t"); plt.ylabel("value")
        plt.title("Annex M — Reflexive Entropy & Time Arrow")
        plt.legend(loc="best")
        plt.savefig(os.path.join(OUTDIR, "annexM_entropy.png"), dpi=160, bbox_inches="tight")
        plt.close()
    mono = all(H_R_list[i+1] >= H_R_list[i]-1e-12 for i in range(len(H_R_list)-1))
    return {"demo":"entropy","T":T,"lambda":lam,"HR_monotone":bool(mono),"HR_end":H_R_list[-1]}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--demo", choices=["cone","stability","game","entropy"], help="run a single demo")
    ap.add_argument("--all", action="store_true", help="run all demos")
    args = ap.parse_args()

    ensure_outdir()
    results = {}
    if args.all or args.demo is None:
        results["cone"] = demo_cone()
        results["stability"] = demo_stability()
        results["game"] = demo_game()
        results["entropy"] = demo_entropy()
    else:
        if args.demo=="cone": results["cone"]=demo_cone()
        if args.demo=="stability": results["stability"]=demo_stability()
        if args.demo=="game": results["game"]=demo_game()
        if args.demo=="entropy": results["entropy"]=demo_entropy()

    with open(os.path.join(OUTDIR, "sim_summary.json"), "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()
