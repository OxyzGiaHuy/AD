# Neurocomputing claim and evidence audit

Audit updated: 2026-07-23
State: GPU handoff complete and checksum-verified. Strict category certification
is a documented negative result; historical SC3R values remain empirical.

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
| The discrete uniformity diagnostic follows an ideal exchangeable reference | E | clustered class-seed and category outputs in `outputs/paper_tables/` | LOIO remains asymmetric and the simulated null is idealized | report CDF gaps descriptively; do not call the diagnostic a validity proof |
| Strict SC3R gives useful new-category certification | Negative/P | 0/960 gate pass; Propositions 3--4 feasibility bounds | only 3--4 categories versus at least 14 even for a multiplicity-free distribution-free all-zero bound at alpha 0.20 (22 under the most favorable frozen allocation; 60 for declared Hoeffding) | report zero fallback and sample-size barrier; do not substitute the image estimand |
| Historical SC3R tracks nominal FAR on MVTec/VisA | E | regenerated detailed/summary artifacts plus original tables | selection and assessment were not independent | retain only as an explicitly historical empirical diagnostic |
| Power gain CI excludes zero for every corruption | E/B | hierarchical-bootstrap script/log; CI CSV absent | bootstrap unit and multiplicity across corruptions require audit | recover data; audit class/seed/image dependence; report simultaneous or multiplicity-adjusted intervals |
| Cross-dataset transfer is generally conservative | Not claimable | audited MVTec-to-VisA and MVTec-to-MPDD artifacts | two target archives do not prove a general transfer property | report both directions as empirical stress tests only |
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

## Data-lineage status

The GPU handoff declares 811 deliverables; all exist and all SHA-256 values
verify. Fail-closed audits pass for MVTec, VisA, and MPDD. Per-image views,
support residuals/statistics, support and partition manifests, nested candidate
tables, detailed outputs, clustered uniformity files, simultaneous comparisons,
and the one-command CPU manifest are present. Raw datasets and large feature
caches are intentionally excluded.

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
- GPU execution P0--P7 is complete. The local CPU-only reconstruction passes 97
  tests with the PyTorch-dependent test skipped; the frozen GPU environment
  passed all 98 tests.
