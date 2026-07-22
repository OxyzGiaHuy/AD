# Neurocomputing submission improvement plan

Status: active  
Started: 2026-07-22  
Target: a submission-ready CRR/SC3R manuscript for *Neurocomputing*.

## Non-negotiable integrity rules

1. Every central statement is tagged internally as one of: **proved**,
   **conditional**, **empirical**, or **hypothesis**.
2. “Control”, “guarantee”, and “valid” are used only when the assumptions and
   probability statement are explicit. Otherwise use “observed”, “estimated”,
   or “tracked on the evaluated benchmark”.
3. A changed statistical method requires regenerated results. Narrative edits
   must never be used to make stale results appear compatible with a new method.
4. Every reported number must be traceable to an immutable input table,
   sampling manifest, script, and configuration. Values reconstructed from a
   PDF are presentation fallbacks only and cannot serve as final evidence.
5. Negative, null, or boundary results are retained and reported. Failed gate
   criteria are not averaged away.
6. Source/target separation, image identity, repeated corruptions, class, and
   seed dependence are audited before selecting a statistical unit.
7. “Pre-registered” is used only if a timestamped artifact predating the final
   run exists; otherwise use “specified before the final evaluation”.

## Adversarial self-review protocol

For each milestone, record three positions before accepting it:

- **Author case:** strongest defensible reason the claim matters.
- **Reviewer case:** most serious novelty, leakage, validity, or fairness objection.
- **Resolution:** evidence or wording that resolves the objection; unresolved
  objections become limitations or blockers.

No milestone passes merely because tests compile. It must pass data-lineage,
statistical-unit, assumption, and claim-language checks.

## Work packages and exit criteria

### WP0 — Audit and risk register

- Inventory scripts, outputs, configs, datasets, tests, and manuscript claims.
- Map every central table/figure to its generating artifact.
- Identify missing outputs, reconstructed values, TODO metadata, and unverified
  references.
- Produce a claim-risk register with severity and required resolution.

Exit: every central claim has an owner artifact and a stated evidence class.

### WP1 — Submission blockers

- Reduce the abstract to at most 250 words.
- Remove or explicitly track author/affiliation/funding placeholders.
- Verify all bibliography metadata and remove unverifiable citations.
- Replace premature guarantee/control language and audit “exact” claims.
- Prepare an anonymized reproducibility statement suitable for review.

Exit: no hidden TODO or policy-format blocker remains in the review manuscript.

### WP2 — Formal SC3R specification

- Define the score, normalization, source folds, threshold candidates, safe
  anchor, and target application as an explicit algorithm.
- Add and prove the attainable-alpha proposition.
- Replace empirical threshold selection with an independent upper-confidence
  rule (candidate: exact binomial/Clopper–Pearson; compare with DKW).
- State a source-domain guarantee and a separate conditional target-transfer
  result. Do not claim unconditional target control under domain shift.
- Explicitly classify target-only LOIO as approximate unless a valid alternative
  is adopted.

Exit: theorem statements match the implementation and expose all assumptions.

### WP3 — Implementation and statistical verification

- Implement confidence-bound thresholding with deterministic tests.
- Add tests for monotonicity, ties, empty alarms, finite precision, fold leakage,
  and target exclusion.
- Re-run core SC3R results and regenerate all affected tables/text.
- Report uncertainty intervals for FAR, power, precision, and power gain.
- Correct repeated-testing procedures and document the resampling unit.

Exit: code, tests, tables, and claims agree; regressions and failed gates are visible.

### WP4 — Decisive experiments

- Evaluate the core method at k = 1 and k = 2.
- Run strict nested leave-one-target-class-out evaluation.
- Add source-pool-size and source-class-count ablations.
- Compare matched, clean, pooled, mismatched, and condition-unknown source modes.
- Add direct conformal baselines: randomized, pooled split/inductive,
  cross-conformal, weighted, and an auxiliary-task few-shot analogue where
  implementable under a fair data budget.
- Separate AURC summaries from risk–coverage operating points and prioritize
  operational selective risk over ECE.

Exit: the core novelty survives fair baselines and the hardest few-shot settings,
or the paper’s claim is narrowed accordingly.

### WP5 — External validity

- Assess a third industrial benchmark (prefer MPDD or BTAD) based on license,
  data availability, and protocol compatibility.
- Evaluate cross-dataset source archives and blind condition handling.
- Measure source-archive size, threshold-fit time, and inference overhead.

Exit: at least one credible out-of-benchmark transfer result, or a transparent
reason this evidence is unavailable.

### WP6 — Manuscript rewrite

- Center the narrative on SC3R; keep CRR as the surrounding reliability framework.
- Use one claim, one evidence block, and one boundary per Results paragraph.
- Shorten the introduction, abstract, conclusion, captions, and highlights.
- Move non-central calibration, FGSM, and novelty-audit material to supplement
  when it obscures the core contribution.
- Ensure figures and tables follow Elsevier conventions and remain legible in
  two-column layout.

Exit: a skeptical reader can identify the novelty, assumptions, evidence, and
limitations without reconstructing them across sections.

### WP7 — Reproducibility and final submission audit

- Release or prepare an anonymized repository with pinned environment,
  manifests, per-image predictions, and one-command regeneration.
- Verify author metadata, CRediT, funding, competing interests, AI disclosure,
  data/code statements, references, and highlights.
- Compile from a clean checkout and inspect every page.
- Run a final mock editor review and two mock reviewer reviews: conformal theory
  and industrial anomaly detection.

Exit: no unresolved critical blocker; remaining limitations are stated in the paper.

## Initial risk register

| Risk | Severity | Current evidence | Required action |
|---|---:|---|---|
| SC3R target “control” lacks an unconditional transfer theorem | Critical | empirical benchmark rates | conditional theorem + UCB threshold + restrained wording |
| LOIO scores are not exactly exchangeable | Critical | caveat and empirical audit | valid baseline/alternative or explicitly heuristic claim |
| Resolution-floor novelty may be viewed as elementary | High | direct p-value grid property | make it a proposition; center novelty on SC3R |
| Core method omits k = 1,2 | High | k = 4,8 results | run and report hardest few-shot cases |
| Matched-condition mode assumes condition knowledge | High | limitation only | pooled/blind/mismatched ablations |
| “Pre-registered” may lack public timestamped evidence | High | manuscript assertion | locate artifact or rename claim |
| Abstract exceeds Neurocomputing’s 250-word limit | High | approximately 298 words | rewrite to 220–240 words |
| Central plot fallbacks were reconstructed from vector PDFs | High | plotting fallback constants | recover/regenerate source result tables before final evidence |
| References and author metadata contain TODOs | High | source comments/placeholders | verify and finalize before submission |
| Two datasets may be viewed as limited external validity | Medium | MVTec + VisA | add MPDD/BTAD if feasible |
| Multiple dependent tests may overstate significance | Medium | paired tests/bootstrap | define unit, multiplicity correction, simultaneous intervals |
| Code/data promised only after publication | Medium | availability statement | anonymized review artifact before submission |

## Progress log

- 2026-07-22: Plan initialized. Figure 4 inset moved to the data-free lower-right
  region with its legend in the upper-left. Figure 5 was consolidated into one
  comparative axis; the AURC scalar was removed from the coverage axis.
- 2026-07-22: Initial code/claim audit completed in
  `docs/neurocomputing_claim_audit.md`. Raw `outputs/` evidence is absent and is
  now a critical lineage blocker. The existing SC3R threshold reuses pooled,
  dependent leave-one-class-out source p-values for selection; adding a
  pointwise binomial interval would not create a valid guarantee.
- 2026-07-22: The public Git history does not establish a timestamped
  preregistration predating the final results. Manuscript wording was corrected
  from “pre-registered” to “pre-specified”. Unconditional target-control
  language was removed. The abstract was reduced from approximately 298 to 238
  words, satisfying Neurocomputing's 250-word limit.
- 2026-07-22: A temporary audit environment was created and the focused
  statistical test suite passed (11 tests). Full test execution still requires
  the heavier project dependencies.
- 2026-07-22: Restored the missing `src/data` package with deterministic,
  leakage-safe MVTec/VisA/synthetic loading and sampling. Added layout/mask
  tests and updated removed NumPy integration aliases. The full CPU suite now
  passes 65 tests (subsequently extended further by SC3R certification tests).
- 2026-07-22: Froze the CPU/GPU boundary at the user's request. No new detector
  experiment is being run locally. `docs/gpu_experiment_runbook.md` records the
  full server protocol, commands, manifests, acceptance gates, and negative-
  result policy.
- 2026-07-22: Added a formal SC3R design in
  `docs/sc3r_formal_specification.md`: Proposition 1 proves the attainable-alpha
  floor; a nested reference/proposal/certification design replaces the invalid
  idea of adding a pointwise interval after adaptive threshold selection.
  Simultaneous Hoeffding certification is implemented and tested at image and
  class units. Target transfer remains explicitly conditional.
- 2026-07-22: Replaced the iid pooled discrete-grid test in the analysis code
  with a shared-calibration cluster-null simulator. Manuscript claims of an
  “exact” pooled test and universal rejection were removed pending artifact
  regeneration. This changes the analysis method, so the old numerical
  p-values are not treated as current evidence.
- 2026-07-22: Extended the SC3R exporter to record support-image manifests,
  base-image identity, and corruption parameters. Added a CPU-only strict
  nested evaluator that writes source partitions and candidate-level bounds.
- 2026-07-22: Added a fail-closed artifact auditor, explicit `k=1`
  `patch_split_conformal` metadata, Holm-adjusted Wilcoxon analysis, and an MPDD
  adapter/test path for the frozen MVTec-to-MPDD external protocol. No dataset
  or detector experiment was executed locally.
- 2026-07-22: Final CPU checkpoint passed 79 tests. The two-column CAS PDF
  compiled to 20 pages and was inspected as a full contact sheet; Figure 4
  insets remain inside the lower-right white regions and Figure 5 is one
  combined axis. BibTeX has no empty-page or unresolved-reference warnings.
  Remaining CAS `maketitle` anchor/overfull warnings are template/front-matter
  related and must be rechecked after real author metadata replaces placeholders.
- 2026-07-22: Author-controlled and GPU-controlled blockers are enumerated in
  `docs/submission_blockers.md`. Historical numerical claims remain non-final
  until the revised GPU pipeline and artifact audits are completed.
- 2026-07-22: Completed the remaining CPU-side routing implementation.
  `condition_agnostic` median-collapses all condition views by base-image
  identity; `mismatched_condition` is a deterministic negative control. Added
  family-wise Bonferroni-adjusted hierarchical bootstrap intervals and kept
  pointwise output only as an explicitly labeled option. Generator captions
  now preserve the historical/non-independent caveats. The full suite passes
  82 tests; no detector experiment or numerical result was fabricated.
- 2026-07-22: Added the direct `pooled_source_conformal` baseline to the strict
  evaluator and optional paired `target_only` rows from immutable LOIO
  residuals. Added deterministic source-class/image-count and normalization
  ablations. The artifact audit now verifies finite values, paired corruption
  identity, label stability, nested support sets, and the exact frozen grid.
  Added a JSON-driven one-command CPU pipeline with input/output SHA-256,
  environment/git provenance, and a single Bonferroni confirmatory family.
  A separate fail-closed submission-package audit remains red until real author
  metadata, a clean GPU manifest, and a reviewer-accessible repository are supplied.
- 2026-07-22: Reconciled the manuscript with the strict implementation. Removed
  the nonexistent “safe-anchor defer” path from Method/Figure 1; added the
  nested R/P/C algorithm, a conditional simultaneous source certificate, and a
  separate target-transfer corollary whose dominance/exchangeability assumption
  is explicit. Support sampling now uses nested prefixes across k. Added
  configurable candidate-cap and R/P/C-allocation sensitivities, runtime fields,
  current Elsevier author-guide checks, and three adversarial mock reviews.
  The expanded CPU suite passes 98 tests after the post-GPU aggregation and
  exact-binomial certification additions.
- 2026-07-22: Added a zero-preserving post-GPU aggregation layer. It rejects
  unpaired/missing methods, retains every zero-threshold target cell, freezes an
  80% nonzero category-threshold operational gate, joins simultaneous power
  intervals, and emits gate JSON plus compile-tested LaTeX fragments. Replaced
  image-level Hoeffding with a sharper exact Clopper--Pearson source-mixture
  bound while retaining category-level Hoeffding as a distinct new-category
  stress test; family delta is now shared across alpha levels, both units, and
  candidates within a target cell.
