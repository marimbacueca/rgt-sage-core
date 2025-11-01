#!/usr/bin/env python3
"""
Reflexive_Metrics_Validator.py — Invariant checks for RGT Sage (v1.0)

Validates recorded metrics (CSV or JSON) against core invariants:
  • ΔV_R ≤ 0 for accepted steps
  • ρ(Γ) < 1 (stability)
  • H_R monotone non-decreasing
  • τ < μ/L^2 for VI solver
  • Cone feasibility HF − α‖others‖ ≥ 0 (rate threshold)
"""

import argparse, json, math, sys, os
from typing import Dict, Any, List

try:
    import pandas as pd
    HAVE_PANDAS = True
except Exception:
    HAVE_PANDAS = False

def load_metrics(path: str) -> Dict[str, Any]:
    if path.lower().endswith(".json"):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    if path.lower().endswith(".csv"):
        if not HAVE_PANDAS:
            raise RuntimeError("pandas required for CSV input")
        import pandas as pd
        df = pd.read_csv(path)
        return {"table": df.to_dict(orient="list")}
    raise ValueError("Unsupported file type; use .json or .csv")

def check_delta_vr(data: Dict[str, Any]) -> bool:
    seq = data.get("DeltaV_R") or data.get("ΔV_R") or data.get("delta_vr")
    if seq is None and "table" in data:
        table = data["table"]
        seq = table.get("DeltaV_R") or table.get("ΔV_R")
    if seq is None:
        return True  # missing -> neutral
    return all(x <= 1e-12 for x in seq)

def check_rho_gamma(data: Dict[str, Any], bound: float=1.0) -> bool:
    rho = data.get("rho_Gamma") or data.get("ρ(Γ)") or data.get("rho")
    if rho is None:
        if "table" in data and "rho_Gamma" in data["table"]:
            rho = max(data["table"]["rho_Gamma"])
    if rho is None:
        return True
    return float(rho) < bound

def check_entropy_monotone(data: Dict[str, Any]) -> bool:
    seq = data.get("H_R")
    if seq is None and "table" in data:
        seq = data["table"].get("H_R")
    if seq is None:
        return True
    return all(seq[i+1] >= seq[i]-1e-12 for i in range(len(seq)-1))

def check_vi_stepsize(data: Dict[str, Any]) -> bool:
    mu = data.get("mu"); L = data.get("L"); tau = data.get("tau")
    if mu is None or L is None or tau is None:
        if "table" in data:
            t = data["table"]
            mu = (t.get("mu") or [None])[-1]
            L  = (t.get("L") or [None])[-1]
            tau= (t.get("tau") or [None])[-1]
    if mu is None or L is None or tau is None:
        return True
    return float(tau) < float(mu)/(float(L)**2 + 1e-12)

def check_cone_feas_rate(data: Dict[str, Any], alpha: float=0.5, min_rate: float=0.95) -> bool:
    rate = data.get("cone_feasible_rate")
    if rate is None and "table" in data:
        rate = (data["table"].get("cone_feasible_rate") or [None])[-1]
    if rate is None:
        return True
    return float(rate) >= min_rate

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("metrics_file", help="JSON or CSV with recorded metrics")
    ap.add_argument("--alpha", type=float, default=0.5, help="Cone alpha")
    ap.add_argument("--min-cone-rate", type=float, default=0.95, help="Min feasibility rate")
    ap.add_argument("--rho-bound", type=float, default=1.0, help="Upper bound for rho(Gamma)")
    args = ap.parse_args()

    data = load_metrics(args.metrics_file)
    checks = {
        "DeltaV_R<=0": check_delta_vr(data),
        "rho(Gamma)<bound": check_rho_gamma(data, bound=args.rho_bound),
        "H_R monotone": check_entropy_monotone(data),
        "tau<mu/L^2": check_vi_stepsize(data),
        "cone feasibility rate": check_cone_feas_rate(data, alpha=args.alpha, min_rate=args.min_cone_rate),
    }
    all_ok = all(checks.values())
    report = {"file": args.metrics_file, "ok": all_ok, "checks": checks}
    print(json.dumps(report, indent=2))
    sys.exit(0 if all_ok else 2)

if __name__ == "__main__":
    main()
