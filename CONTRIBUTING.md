# Contributing to RGT Sage

Thanks for helping improve Reflexive Governance Theory (RGT)! This project favors clarity, legitimacy, and safety.

## How to contribute
1. **Discuss first** – Open an Issue describing the change (math, pedagogy, docs, or ops).
2. **Fork & branch** – Create a feature branch: `feat/<short-name>`.
3. **Standards**
   - Follow the 19-file structure; do not exceed 20 files.
   - Keep math changes in `13_Mathematical_Foundations_Appendix_v0_1.md` and reference them in the README.
   - Keep operating rules in `RGT_Sage_Operating_Instructions_v1.1.md`.
   - Add or update hashes via the manifest script if you change file bodies.
4. **Conventional Commits**
   - `feat:` new theorem/module
   - `fix:` math/ops corrections
   - `docs:` narrative/glossary updates
   - `chore:` plumbing, manifest refresh
   - `refactor:` structure without behavior change
5. **Pull requests**
   - One focused change per PR.
   - Add a short rationale and any citations (official sources preferred).
   - Keep any public examples anonymized; no PII.

## Hash verification
Run `verify_hashes.py` and include “OK” in your PR description.

## Code of Conduct
Be respectful. No harassment, hate speech, or disinformation campaigns.

## License
By contributing, you agree your work will be licensed under the repository’s LICENSE.
