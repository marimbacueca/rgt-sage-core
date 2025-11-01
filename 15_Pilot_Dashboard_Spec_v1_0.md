---
version: 3.6.1
build: 2025-11-01T00:24:46
format: markdown
type: dual
description: RGT Sage – Reflexive Governance Theory Core (Signature Edition)
---
SHA256 (excluding this line): 9a9174e6f588a04928f7a00b3b4419ba2a8902ee925236dd78e1b1ceb40ce998

# Pilot Dashboard Spec (v3.6.1)

**Tiles.**
1) Pulse (r/κ, α, K, crisis dampener)
2) Legitimacy L (decomposition)
3) Coherence C (P, D, drift) + EPS + D*
4) Audits (batches, SLA, capacity scale)
5) Participation parity
6) Rights gate & Transparency Floor (hashes)

**UX.** Plain language; AA/AAA; one visual per concept.

## Automatic Data-Refresh Protocol (Quarterly)

**Schedule:** Every 90 days (RRULE:FREQ=QUARTERLY).

**Process:**
1) `web.search("official open data" + domain + date range)`
2) Extract summary statistics only (no PII); compute EPS.
3) Recompute \(\phi\) and \((\alpha,K)\) calibration; update \(q^\*, \tau, C^\*\) if indicated.
4) Append citation block with signed hash; update dashboard and manifest.

**Fallback:** On fetch failure, retain last stable calibration and flag for human review.

**Controls:** Manual override via `RGT_ADMIN: update off`.
