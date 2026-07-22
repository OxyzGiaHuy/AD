# Neurocomputing claim and evidence audit

Audit date: 2026-07-22  
State: active audit; raw `outputs/` artifacts remain absent. CPU code tests pass,
but historical numerical results are not yet independently reproducible.

## Evidence labels

- **P — proved:** follows from a stated mathematical argument.
- **C — conditional:** valid only under explicit assumptions.
- **E — empirical:** supported on the evaluated samples; no population guarantee.
- **H — hypothesis:** mechanism or explanation not yet isolated experimentally.
- **B — blocked:** required source artifact is unavailable.

## Central claim matrix

| Manuscript claim | Current label | Evidence/code | Main objection | Required resolution |
|---|---|---|---|---|
| A target-only conformal p-value from k calibration scores cannot be below 1/(k+1) | P | Eq. (6), attainable-alpha tests/table | elementary rather than major novelty | state as a proposition with a short proof; use it to define the problem, not as the sole novelty |
| Target-only LOIO provides conformal false-alarm control | Not currently claimable | `src/conformal.py`, `evaluate_target_only` | calibration scores use k-1-fit models while test uses a k-fit model; not exchangeable | call it approximate/empirical or replace with a formally valid construction |
| The discrete uniformity diagnostic follows an ideal exchangeable reference | E/B | cluster-aware simulator implemented; result CSV absent | class/seed/base-image dependence remains and LOIO itself is asymmetric | regenerate views; report CDF gaps descriptively and both class-seed/category sensitivity; do not reuse old iid p-values |
| SC3R source validation controls target FAR | E, not unconditional C/P | `evaluate_source_validated_threshold.py`; result CSV absent | threshold selection and validation reuse the same dependent leave-one-class-out source p-values; source-to-target transfer is unproved | independent fit/certification source split or valid simultaneous cluster-aware bound; separate source guarantee from conditional target transfer |
| SC3R tracks nominal FAR on MVTec/VisA | E/B | manuscript tables and research log; raw detailed CSV absent | cannot recompute intervals or verify sampling lineage | recover or regenerate per-image views, manifests, detailed results, and uncertainty intervals |
| Power gain CI excludes zero for every corruption | E/B | hierarchical-bootstrap script/log; CI CSV absent | bootstrap unit and multiplicity across corruptions require audit | recover data; audit class/seed/image dependence; report simultaneous or multiplicity-adjusted intervals |
| Cross-dataset MVTec-to-VisA transfer is conservative | E/B | manuscript table/log; detailed CSV absent | one direction and one target dataset do not establish general safe transfer | recover artifact, state one-direction scope, add reverse/third-dataset evidence if feasible |
| LOIO improves ECE over scalar calibrators | E/B | table/log; per-image views absent | ECE is prevalence-sensitive; calibration samples and repeated corruptions are dependent | retain as secondary evidence, recover views, correct multiplicity and emphasize operational metrics |
| Low-storage detector remains competitive in ranking/localization | E/B | clean/pixel tables; raw outputs absent | controlled baselines are not all official; ranking is inherited prior art | keep as supporting substrate and precisely label official vs controlled rows |
| Entropy abstention improves selective reliability | E/B | Figure 5 and text; source CSV absent | current plotting fallback was reconstructed from the old vector PDF; ECE is not the primary deployment loss | recover CSV, report AURC separately, add selective FAR/power if possible |

## Initial implementation findings

### SC3R threshold selection

Current `conservative_threshold` chooses the largest observed p-value whose
empirical source FAR is at most alpha. The p-values are obtained by holding out
each source class and conformalizing it against all remaining source classes.

**Author case:** class-held-out scoring is substantially better than evaluating
the source observations against a pool containing their own class, and it makes
the target class absent from the source pool.

**Reviewer case:** all held-out-class p-values are pooled, share overlapping
reference sets, and are then reused to choose the threshold. The empirical
constraint is neither an independent certification nor an iid binomial sample.
A pointwise Clopper–Pearson interval added after selection would not fix this.

**Resolution direction:** introduce a deterministic outer split of source
classes. One subset proposes threshold candidates; a disjoint certification
subset evaluates the fixed candidate. Certification must operate at a declared
unit (preferably held-out class or class-seed cluster), and the finite-sample
statement must match that unit. Cross-fitting can later recover efficiency, but
only after a valid aggregation rule is specified.

### Target transfer

**Author case:** per-class median/MAD normalization and matched-condition source
images are designed to reduce cross-category shift; empirical cross-dataset
results are conservative.

**Reviewer case:** normalization does not imply stochastic dominance or equal
distributions. No distribution-free method can infer unconditional target FAR
control from unrelated source categories without a transfer assumption.

**Resolution direction:** prove source certification only; state target control
conditionally under exchangeability/dominance of normalized target normal
scores. Treat observed target FAR as external validation of this assumption,
not as proof that it always holds.

## Data-lineage blockers

The following artifacts are referenced in logs/manuscript but are absent:

- per-image SC3R view CSVs and support residual/statistics CSVs;
- detailed and summary source-validated-threshold CSVs;
- hierarchical confidence-interval CSVs;
- p-value uniformity Q-Q/test CSVs;
- selective-risk CSVs used by Figure 5;
- per-image calibration views used for paired calibrator tests;
- sampling manifests and cached feature/result provenance.

Until recovered or regenerated, manuscript tables are preserved as historical
results but are not considered final auditable evidence.

## Submission-format blockers

- Abstract has been reduced below Neurocomputing's 250-word limit.
- Author, affiliation, ORCID, email, CRediT, and acknowledgement placeholders remain.
- Audited bibliography TODOs were resolved against primary metadata sources;
  a final full-reference pass is still required.
- Git history did not establish public preregistration before results;
  manuscript wording now uses “pre-specified”.
- Code/data are promised after publication rather than available for anonymous review.

## CPU reproducibility status

- Missing `src/data` implementation restored and tested for MVTec-like and VisA
  CSV layouts, masks, deterministic support selection, and calibration leakage.
- NumPy compatibility fixed without changing metric definitions.
- Full suite passed before the later certification additions; the final suite
  must be rerun after each subsequent change.
- Strict nested SC3R certification and shared-calibration Monte Carlo code have
  synthetic unit tests. These tests validate implementation invariants, not the
  paper's empirical conclusions.
- GPU experiment execution is intentionally deferred. Exact commands and gates
  are in `docs/gpu_experiment_runbook.md`.
