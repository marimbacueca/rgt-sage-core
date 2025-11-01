---
version: 3.6.1
build: 2025-11-01T00:24:46
format: markdown
type: dual
description: RGT Sage – Reflexive Governance Theory Core (Signature Edition)
---
SHA256 (excluding this line): c11fe1d6d2f7e64bf3b18613afa353c738bb5226b6e21653c42b2a4583338880

# Resource Reciprocity Addendum (v3.6.1)

**Principle.** Publicly funded learning → public knowledge with provenance.

**Policy.**
- Quarterly release (auto-refresh) with lineage graphs and hashes.
- Two-key acceptance: KPI_A (performance) AND KPI_B (coherence C).

**Enforcement.**
- Missing provenance ⇒ block use; penalties exceed opacity gains.

## Automatic Data-Refresh Protocol (Quarterly)

**Schedule:** Every 90 days (RRULE:FREQ=QUARTERLY).

**Process:**
1) `web.search("official open data" + domain + date range)`
2) Extract summary statistics only (no PII); compute EPS.
3) Recompute \(\phi\) and \((\alpha,K)\) calibration; update \(q^\*, \tau, C^\*\) if indicated.
4) Append citation block with signed hash; update dashboard and manifest.

**Fallback:** On fetch failure, retain last stable calibration and flag for human review.

**Controls:** Manual override via `RGT_ADMIN: update off`.
