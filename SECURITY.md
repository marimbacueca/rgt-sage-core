# Security Policy

## Maintainer
**Katja Gantz**  
Primary Author and Maintainer of RGT Sage (Reflexive Governance Theory)  
GitHub: [@marimbacueca](https://github.com/marimbacueca)

---

## Supported Scope
This repository is a documentation corpus and mathematical framework.
It does **not** contain executable code beyond simple verification utilities.
Security considerations focus on:

- **Tamper attempts:** Modified files without manifest updates or broken SHA-256 verification.
- **Data integrity:** Use of unreliable or non-official data sources in public-data refreshes.
- **Privacy:** Respect for differential-privacy (DP) and Right-to-Partial-Reflexivity (RPR) policies.

---

## Reporting a Vulnerability
1. Open a **Private vulnerability report** in GitHub → *Security → Report a vulnerability*,  
   or email Katja Gantz using the contact listed on the GitHub profile.  
2. Include:
   - Affected file(s)
   - Risk description and reproduction steps (if applicable)
   - Suggested mitigation or correction

---

## Validation Steps
- Run `verify_hashes.py` to detect tampering or corruption.
- Validate that any referenced datasets are official, cited, and have EPS ≥ 0.6 (see files 08 & 15).

---

## Disclosure Policy
Vulnerability reports will receive acknowledgment within **48 hours**.  
Non-sensitive corrections will be documented transparently in the next release notes.

---

*RGT Sage maintains integrity through openness, verification, and ethical reflexivity.*
