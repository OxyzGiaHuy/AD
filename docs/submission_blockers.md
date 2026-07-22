# Submission blockers requiring author or GPU-server input

This file distinguishes work that can be completed locally from facts Codex
must not invent. The manuscript is not submission-ready until every critical
item below is closed.

## Critical author-supplied metadata

- [ ] Full author names in final order.
- [ ] Short author list.
- [ ] Affiliations, city, and country for each author.
- [ ] Corresponding-author email and marker.
- [ ] Valid ORCID identifiers; remove ORCID fields for authors without one.
- [ ] Biography of at most 100 words and a passport-type photograph for each
      author, supplied as separate editable/image files.
- [ ] Per-author CRediT roles approved by every author.
- [ ] Funding statement and grant numbers, or explicit confirmation of no funding.
- [ ] Acknowledgements approved by the named people; do not identify an advisor
      generically in the final manuscript.
- [ ] Competing-interest declaration confirmed by all authors.
- [ ] Every author reviews and approves the truthful Codex/AI-assistance
      disclosure in `sections/declarations.tex`.

Current placeholders are in `els-cas-templates/main.tex` and
`sections/declarations.tex`. They are intentionally not guessed.

## Critical evidence/artifact blockers

- [ ] Recover historical raw outputs or run the frozen GPU protocol in
      `docs/gpu_experiment_runbook.md`.
- [ ] Artifact audit passes for MVTec, VisA, and any third dataset.
- [ ] Regenerate cluster-aware discrete-grid diagnostics; retire old iid pooled
      Monte Carlo p-values.
- [ ] Regenerate calibrator comparisons with Holm-adjusted p-values.
- [ ] Run and report strict nested source certification, including zero-threshold
      failures and both image/category units.
- [ ] Run mandatory `k=1,2`; label `k=1` patch-split calibration separately from
      image-level LOIO.
- [ ] Run the implemented `condition_agnostic`/mismatched modes on GPU-exported
      artifacts, or narrow the deployment claim to condition-identifiable settings.
- [ ] Run MVTec-to-MPDD external validation, or state that it could not be
      completed; do not insert an undocumented partial dataset.
- [ ] Recover/regenerate the Figure 5 source CSV; the PDF-reconstructed fallback
      is presentation-only.
- [ ] Regenerate every affected table and numerical sentence after the revised
      statistical pipeline. No hand-editing a number to resemble the new method.

## Release blockers

- [ ] Create a reviewer-accessible repository/archive. Neurocomputing currently
      uses single-anonymized review, so author anonymity is not required by the
      journal; preserve an immutable review snapshot nonetheless.
- [ ] Insert its URL/DOI and immutable commit into Data/Code Availability.
- [ ] Include environment lock, dataset setup instructions, manifest/checksum
      files, per-image CSVs, and one-command CPU table/figure regeneration.
- [ ] Confirm dataset licenses. MPDD is CC BY-NC-SA 4.0 and raw images must not be
      bundled into the code artifact.
- [ ] Remove private absolute paths and test on a clean checkout.

## Final editorial blockers

- [ ] Replace all author/funding/repository placeholders.
- [ ] Reconcile Abstract, Highlights, Results, Conclusion, and captions with the
      final regenerated evidence, especially any failed nested gate.
- [ ] Rebuild figures from source CSVs and visually inspect the two-column PDF.
- [ ] Resolve material overfull boxes and confirm table legibility at 100% zoom.
- [ ] Run a final reference/DOI audit and editor/reviewer mock review.
- [ ] Check Neurocomputing's current Guide for Authors on the submission date.

## Current honest status (2026-07-22)

- CPU suite has passed 98 tests after the core reproducibility/statistical changes.
- LaTeX compiles in two-column CAS format.
- Abstract is 238 words.
- BibTeX has no missing-page warnings after representing page-less ICLR papers
  without invented page ranges.
- Historical paper numbers remain non-final because raw evidence is absent and
  the corrected GPU/statistical pipeline has not been run.
