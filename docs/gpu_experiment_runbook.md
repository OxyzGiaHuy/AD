# GPU experiment runbook for the Neurocomputing submission

Status: commands prepared, **not executed in the current CPU-only workspace**.  
Purpose: regenerate auditable evidence on a GPU server without silently changing
the protocol after seeing results.

## 0. Rules before any run

1. Run from a clean commit containing the restored `src/data` package, support
   manifests, `base_image_path`, nested SC3R evaluator, and passing CPU tests.
2. Record the commit SHA before launching. Never regenerate a table from a dirty
   tree without archiving the diff.
3. Freeze the following choices before looking at results:
   `k={1,2,4,8}`, seeds `{0,1,2,3,4}`, `rho=0.01`, image size 518,
   PCA components 64, maximum 120 evaluation images per class/cell, corruptions
   `{clean,gaussian_noise,blur,brightness_contrast,jpeg}`, alphas
   `{0.05,0.10,0.20}`, confidence delta `0.05`, maximum 20 proposed thresholds.
4. Primary certification unit is category. Image-level certification is a
   sensitivity analysis only. Do not switch the primary unit after seeing which
   passes.
5. Keep failed cells and zero-threshold fallbacks. Never overwrite a completed
   run with different parameters under the same run tag.
6. GPU nondeterminism and library versions must be recorded. Repeated seeds are
   support/sampling replicates, not independent datasets.
7. `k=1` uses an explicitly labeled patch-split calibration because image-level
   LOIO is impossible with one support image. It must be reported separately
   from `k>=2` LOIO and cannot be used as evidence for an image-exchangeable
   conformal guarantee.

## 1. Server variables and immutable metadata

Set server-specific paths; do not reuse the obsolete `/home/crl/AD` paths from
historical scripts.

```bash
export PROJECT_ROOT=/absolute/path/to/AD
export SCRATCH_ROOT=/absolute/path/to/fast-scratch/ad-neurocomputing
export RUN_TAG=nc_frozen_v1
cd "$PROJECT_ROOT"
mkdir -p "$SCRATCH_ROOT" "outputs/manifests/$RUN_TAG" "logs/$RUN_TAG"
git rev-parse HEAD | tee "outputs/manifests/$RUN_TAG/git_commit.txt"
git status --porcelain=v1 | tee "outputs/manifests/$RUN_TAG/git_status.txt"
python --version | tee "outputs/manifests/$RUN_TAG/python_version.txt"
python -m pip freeze | sort > "outputs/manifests/$RUN_TAG/pip_freeze.txt"
nvidia-smi -q > "outputs/manifests/$RUN_TAG/nvidia_smi.txt"
python -c 'import torch; print(torch.__version__, torch.version.cuda, torch.cuda.get_device_name(0))' \
  > "outputs/manifests/$RUN_TAG/torch_cuda.txt"
pytest -q | tee "logs/$RUN_TAG/cpu_tests_before_run.log"
```

Gate: working tree must be clean or `git_status.txt` plus the exact diff must be
archived and reviewed. CPU tests must report all tests passing.

## 2. Dataset and split audit

Expected roots:

- `data/mvtec/<class>/{train/good,test/*,ground_truth/*}` for all 15 classes;
- `data/visa/split_csv/1cls.csv` plus its referenced images/masks, or an
  equivalent MVTec-like layout, for all 12 classes.

Before GPU work, run a metadata-only load and save counts:

```bash
python - <<'PY' > "outputs/manifests/$RUN_TAG/dataset_counts.txt"
from collections import Counter
from scripts.generate_benchmark_grid import MVTEC_CLASSES, VISA_CLASSES
from src.data.datasets import load_records
for dataset, classes in (("mvtec", MVTEC_CLASSES), ("visa", VISA_CLASSES)):
    rows = load_records(dataset, f"data/{dataset}", classes)
    counts = Counter((r.category, r.split, r.label, bool(r.mask_path)) for r in rows)
    print(dataset, len(rows))
    for key, value in sorted(counts.items()): print(key, value)
PY
sha256sum data/visa/split_csv/1cls.csv > "outputs/manifests/$RUN_TAG/visa_split_sha256.txt"
```

Manually verify:

- every class has at least 8 train-normal images;
- train contains no anomaly label;
- test contains both labels;
- missing anomaly masks are counted and disclosed for pixel metrics;
- no symlink resolves outside the intended dataset version;
- official dataset version/license and download URL are recorded.

Gate: stop if class counts differ from the intended official splits. Do not fix
counts by silently dropping files.

## 3. P0 — Recover historical artifacts before recomputation

Search backups/server storage for the CSVs named in
`docs/neurocomputing_claim_audit.md`. Copy, do not move, them into a dated
read-only archive. For every recovered file save `sha256sum`, byte size, source
path, and modification time. Recovered results are acceptable for diagnosis,
but become final evidence only if their config, sampling manifest, and commit can
be established.

## 4. P1 — Export full per-image SC3R views (GPU)

Explicit class lists prevent the historical representative-class fallback.

```bash
MVTEC_CLASSES="bottle cable capsule carpet grid hazelnut leather metal_nut pill screw tile toothbrush transistor wood zipper"
VISA_CLASSES="candle capsules cashew chewinggum fryum macaroni1 macaroni2 pcb1 pcb2 pcb3 pcb4 pipe_fryum"

python -u scripts/export_sc3r_views.py \
  --base-config configs/generated/mvtec_full/calib_subspace_head_mvtec_bottle_k1_seed0.yaml \
  --dataset mvtec --classes $MVTEC_CLASSES \
  --k-shots 1 2 4 8 --seeds 0 1 2 3 4 \
  --corruptions clean gaussian_noise blur brightness_contrast jpeg \
  --max-images 120 --rho 0.01 --tmp-root "$SCRATCH_ROOT/corruptions" \
  --out "outputs/paper_tables/sc3r_views_mvtec_${RUN_TAG}.csv" \
  --support-out "outputs/paper_tables/sc3r_support_mvtec_${RUN_TAG}.csv" \
  --support-manifest-out "outputs/manifests/$RUN_TAG/support_mvtec.csv" \
  --resume 2>&1 | tee "logs/$RUN_TAG/export_mvtec.log"

python -u scripts/export_sc3r_views.py \
  --base-config configs/generated/visa_full/calib_subspace_head_visa_candle_k1_seed0.yaml \
  --dataset visa --classes $VISA_CLASSES \
  --k-shots 1 2 4 8 --seeds 0 1 2 3 4 \
  --corruptions clean gaussian_noise blur brightness_contrast jpeg \
  --max-images 120 --rho 0.01 --tmp-root "$SCRATCH_ROOT/corruptions" \
  --out "outputs/paper_tables/sc3r_views_visa_${RUN_TAG}.csv" \
  --support-out "outputs/paper_tables/sc3r_support_visa_${RUN_TAG}.csv" \
  --support-manifest-out "outputs/manifests/$RUN_TAG/support_visa.csv" \
  --resume 2>&1 | tee "logs/$RUN_TAG/export_visa.log"
```

The exporter now records `base_image_path`, view path, sampling seed, corruption
parameters, and exact support images. This is required to cluster repeated
views correctly.

Expected completeness:

- MVTec: `15 classes x 4 k x 5 seeds x 5 conditions = 1500` completed cells;
- VisA: `12 x 4 x 5 x 5 = 1200` completed cells;
- each cell has at most 120 rows and, when both labels exist, balanced sampling
  up to class availability.

After export:

```bash
sha256sum outputs/paper_tables/sc3r_views_*_${RUN_TAG}.csv \
  outputs/paper_tables/sc3r_support_*_${RUN_TAG}.csv \
  outputs/manifests/$RUN_TAG/support_*.csv \
  > "outputs/manifests/$RUN_TAG/sc3r_export_sha256.txt"
```

Run the fail-closed audit for each dataset:

```bash
python scripts/audit_sc3r_artifacts.py \
  --views "outputs/paper_tables/sc3r_views_mvtec_${RUN_TAG}.csv" \
  --support-stats "outputs/paper_tables/sc3r_support_mvtec_${RUN_TAG}.csv" \
  --support-manifest "outputs/manifests/$RUN_TAG/support_mvtec.csv" \
  --out "outputs/manifests/$RUN_TAG/audit_mvtec.json"
```

Repeat with the VisA paths. Gate: both commands must return exit code zero. They
check duplicate base-image cell keys, exact support counts, support-stat keys,
binary labels, finite scores, and support/evaluation overlap.

## 5. P2 — Target-only anchors and clustered uniformity (GPU export, CPU analysis)

LOIO support residual export uses the cached GPU features:

```bash
python -u scripts/export_support_loio_residuals.py \
  --base-config configs/generated/mvtec_full/calib_subspace_head_mvtec_bottle_k1_seed0.yaml \
  --dataset mvtec --classes $MVTEC_CLASSES --k-shots 1 2 4 8 --seeds 0 1 2 3 4 \
  --rho 0.01 --out "outputs/paper_tables/sc3r_loio_mvtec_${RUN_TAG}.csv" --resume

python -u scripts/export_support_loio_residuals.py \
  --base-config configs/generated/visa_full/calib_subspace_head_visa_candle_k1_seed0.yaml \
  --dataset visa --classes $VISA_CLASSES --k-shots 1 2 4 8 --seeds 0 1 2 3 4 \
  --rho 0.01 --out "outputs/paper_tables/sc3r_loio_visa_${RUN_TAG}.csv" --resume
```

The existing p-value view exporter/analysis must then be run with
`--cluster-cols class seed`. Category-only sensitivity is also required because
seeds reuse evaluation images. Do not report the old iid pooled Monte Carlo
p-values as confirmatory results.

Acceptance rule: CDF direction/gaps are descriptive. Any p-value statement must
name the simulated null and clustering unit; multiplicity across dataset/k/
condition cells must be adjusted or labeled exploratory.

## 6. P3 — Historical empirical SC3R analysis (CPU)

Run only to reproduce the existing paper tables, clearly labeled empirical:

```bash
python scripts/evaluate_source_validated_threshold.py \
  --inputs "outputs/paper_tables/sc3r_views_mvtec_${RUN_TAG}.csv" \
  --support-stats "outputs/paper_tables/sc3r_support_mvtec_${RUN_TAG}.csv" \
  --support-residuals "outputs/paper_tables/sc3r_loio_mvtec_${RUN_TAG}.csv" \
  --source-modes matched_condition clean_source --alphas 0.05 0.10 0.20 \
  --run-tag "mvtec_${RUN_TAG}"
```

Repeat for VisA and MVTec-to-VisA transfer. These outputs reproduce the
historical adaptive threshold and must not be called independently certified.

## 7. P4 — Strict nested SC3R certification (CPU; primary new gate)

```bash
python scripts/evaluate_nested_sc3r.py \
  --inputs "outputs/paper_tables/sc3r_views_mvtec_${RUN_TAG}.csv" \
  --support-stats "outputs/paper_tables/sc3r_support_mvtec_${RUN_TAG}.csv" \
  --support-residuals "outputs/paper_tables/sc3r_loio_mvtec_${RUN_TAG}.csv" \
  --source-mode matched_condition --alphas 0.05 0.10 0.20 \
  --delta 0.05 --max-candidates 20 --run-tag "mvtec_matched_${RUN_TAG}"

python scripts/evaluate_nested_sc3r.py \
  --inputs "outputs/paper_tables/sc3r_views_mvtec_${RUN_TAG}.csv" \
  --support-stats "outputs/paper_tables/sc3r_support_mvtec_${RUN_TAG}.csv" \
  --support-residuals "outputs/paper_tables/sc3r_loio_mvtec_${RUN_TAG}.csv" \
  --source-mode clean_source --alphas 0.05 0.10 0.20 \
  --delta 0.05 --max-candidates 20 --run-tag "mvtec_clean_${RUN_TAG}"

python scripts/evaluate_nested_sc3r.py \
  --inputs "outputs/paper_tables/sc3r_views_visa_${RUN_TAG}.csv" \
  --support-stats "outputs/paper_tables/sc3r_support_visa_${RUN_TAG}.csv" \
  --support-residuals "outputs/paper_tables/sc3r_loio_visa_${RUN_TAG}.csv" \
  --source-mode matched_condition --alphas 0.05 0.10 0.20 \
  --delta 0.05 --max-candidates 20 --run-tag "visa_matched_${RUN_TAG}"

python scripts/evaluate_nested_sc3r.py \
  --inputs "outputs/paper_tables/sc3r_views_mvtec_${RUN_TAG}.csv" \
           "outputs/paper_tables/sc3r_views_visa_${RUN_TAG}.csv" \
  --support-stats "outputs/paper_tables/sc3r_support_mvtec_${RUN_TAG}.csv" \
                  "outputs/paper_tables/sc3r_support_visa_${RUN_TAG}.csv" \
  --support-residuals "outputs/paper_tables/sc3r_loio_mvtec_${RUN_TAG}.csv" \
                      "outputs/paper_tables/sc3r_loio_visa_${RUN_TAG}.csv" \
  --source-mode matched_condition --source-dataset mvtec --target-dataset visa \
  --alphas 0.05 0.10 0.20 --delta 0.05 --max-candidates 20 \
  --run-tag "mvtec_to_visa_${RUN_TAG}"
```

Primary gate, evaluated separately for every `k` and condition:

- report proportion of target cells with a nonzero category-certified threshold;
- among nonzero cells, report target FAR, power, precision and category-level
  uncertainty without hiding zero-threshold cells;
- report all candidate UCBs and exact R/P/C partitions;
- require nonzero category-certified thresholds in at least 80% of target
  class--seed cells for an empirical operational pass; report the exact rate;
- if category certification almost always returns zero, formal certification is
  statistically underpowered. The paper must then retain an empirical SC3R
  claim and present this as a limitation/negative result.

Image-level Clopper--Pearson certificates target risk for the fixed source-image
mixture. Category-level Hoeffding certificates target a new-category
meta-population and are expected to be much wider with 12--15 classes. One
estimand cannot substitute for the other; a failed category certificate must be
reported even if the fixed-archive image certificate passes. The family delta
is divided across all declared alpha levels, both units, and candidate
thresholds within a target cell.

## 8. P5 — Condition-routing ablations (CPU implementation complete)

Run the strict nested evaluator once per routing rule:

```bash
for MODE in matched_condition clean_source condition_agnostic mismatched_condition; do
  python scripts/evaluate_nested_sc3r.py \
    --inputs "outputs/paper_tables/sc3r_views_mvtec_${RUN_TAG}.csv" \
    --support-stats "outputs/paper_tables/sc3r_support_mvtec_${RUN_TAG}.csv" \
    --support-residuals "outputs/paper_tables/sc3r_loio_mvtec_${RUN_TAG}.csv" \
    --source-mode "${MODE}" --alphas 0.05 0.10 0.20 \
    --delta 0.05 --max-candidates 20 --run-tag "mvtec_${MODE}_${RUN_TAG}"
done
```

The rules are frozen in `scripts/evaluate_nested_sc3r.py`. `matched_condition`
uses condition metadata and is an oracle/metadata-assisted upper operational
mode. `clean_source` always uses clean source normals. `condition_agnostic` is
the blind/pooled deployment mode: before any target metric is computed, it
takes the median normalized score across all available views of each
`base_image_path`. Thus each source image contributes exactly one unit even
when it has several corrupted views. `mismatched_condition` is a negative
control using the deterministic lexicographic successor of the target
condition. Do not relabel the latter as a realistic router.

For multiplicity-sensitive comparisons, assemble the paired method rows into a
single CSV and run:

```bash
python scripts/hierarchical_bootstrap_comparison.py \
  --input outputs/paper_tables/sc3r_all_methods_${RUN_TAG}.csv \
  --baseline target_only --candidates nested_sc3r \
  --metrics false_alarm_rate power alarm_precision \
  --iterations 20000 --family-alpha 0.05 --multiplicity bonferroni \
  --seed 0 --out outputs/paper_tables/sc3r_simultaneous_${RUN_TAG}.csv
```

The Bonferroni family is every emitted dataset--$k$--condition--source-mode--
$\alpha$--candidate--metric comparison in that invocation. Preserve the
`family_size`, `interval_alpha`, and `multiplicity_method` columns. Pointwise
intervals may be generated only as an explicitly labeled sensitivity analysis.

Acceptance gate: blind/pooled mode must retain meaningful sub-floor power and
must not materially exceed the FAR budget. Otherwise narrow the deployment
claim to identifiable-condition settings.

## 9. P6 — Baselines and ablations

Run under identical backbone features, sampled images, `k`, seeds, and condition
views:

- target-only deterministic LOIO;
- target-only randomized/smoothed conformal;
- pooled source conformal using all routed source normals (implemented in the
  strict evaluator as `pooled_source_conformal`);
- nested SC3R;
- weighted conformal only if a support-normal covariate/importance-weight
  protocol is frozen; effective sample size must be reported;
- scalar calibrators as secondary probability-calibration baselines.

Ablations:

- source class count and source image count;
- robust normalization: none, median/MAD, median/IQR;
- candidate cap `{5,10,20}` as a pre-specified sensitivity analysis;
- reference/proposal/certification allocation;
- top-fraction `rho`, but keep `rho=0.01` primary;
- `k={1,2}` is mandatory and cannot be relegated to supplement if the paper
  claims few-shot behavior.

Do not compare methods using different sampled images or anomaly prevalence.
Correct multiplicity for confirmatory gates; label all other ablations
exploratory.

`target_only`, `pooled_source_conformal`, and `nested_sc3r` are emitted in the
same detailed CSV when `--support-residuals` is supplied, so comparisons are
paired on dataset/class/k/seed/corruption/unit. The pooled baseline receives
the full routed source pool because it performs no candidate selection; do not
artificially restrict it to the nested reference subset.

Cross-conformal aggregation is not a distinct primary baseline for the current
scalar-score artifact: the score model is already fixed per target class and
folding the same source-normal calibration pool only creates an approximate
p-value aggregation without an additional fitted model. Do not introduce an
arbitrary mean-of-fold-p-values baseline and describe it as valid. Weighted
conformal is likewise deferred unless the GPU export includes a frozen
support-normal covariate representation and weights are learned without using
target anomaly labels or an anomaly-contaminated target mixture as if it were
normal data. This is a protocol boundary, not a favorable omitted result.

## 10. P7 — Third dataset: MPDD

MPDD is the frozen first choice. Its official repository describes more than
1000 metal-part images, pixel masks, anomaly-free training data, and a mixed
validation/test side. The repository license is CC BY-NC-SA 4.0. Record both:

- dataset/source: `https://github.com/stepanje/MPDD`;
- license: `https://github.com/stepanje/MPDD/blob/main/LICENSE`.

Do not redistribute raw MPDD images in the reviewer-accessible code artifact; provide
download/setup instructions, attribution, version date, and checksums. Confirm
the archive's actual class names and layout before using the commonly reported
six names (`bracket_black`, `bracket_brown`, `bracket_white`, `connector`,
`metal_plate`, `tubes`). The code accepts `dataset=mpdd` through the same
MVTec-like leakage-safe loader, but deliberately requires an explicit class
list so a changed archive cannot silently alter the benchmark.

MPDD has too few classes for the primary three-way within-dataset nested split
after excluding a target. Therefore:

- within-MPDD SC3R is an empirical replication only;
- the primary external test uses the 15 MVTec source classes partitioned into
  reference/proposal/certification sets and MPDD as target;
- MPDD never tunes `rho`, PCA dimension, corruption severity, candidates,
  `alpha`, or `delta`.

After verifying the archive:

```bash
MPDD_CLASSES="bracket_black bracket_brown bracket_white connector metal_plate tubes"
python -u scripts/export_sc3r_views.py \
  --base-config configs/generated/mvtec_full/calib_subspace_head_mvtec_bottle_k1_seed0.yaml \
  --dataset mpdd --classes $MPDD_CLASSES --k-shots 1 2 4 8 --seeds 0 1 2 3 4 \
  --corruptions clean gaussian_noise blur brightness_contrast jpeg \
  --max-images 120 --rho 0.01 --tmp-root "$SCRATCH_ROOT/corruptions" \
  --out "outputs/paper_tables/sc3r_views_mpdd_${RUN_TAG}.csv" \
  --support-out "outputs/paper_tables/sc3r_support_mpdd_${RUN_TAG}.csv" \
  --support-manifest-out "outputs/manifests/$RUN_TAG/support_mpdd.csv" --resume
```

Run the artifact audit, then strict MVTec-to-MPDD nested evaluation by passing
the MVTec and MPDD views/stats together with `--source-dataset mvtec
--target-dataset mpdd`. If official layout or license differs at download time,
stop and update the manifest; do not improvise an undocumented split.

## 11. Artifact acceptance checklist

Every final number must map to:

1. git commit and environment files;
2. dataset split checksum/counts;
3. support manifest;
4. per-image raw view with `base_image_path`;
5. source partition manifest;
6. candidate-level certification CSV;
7. detailed target metrics;
8. aggregation script and table/figure source CSV;
9. SHA-256 manifest of all above.

## 12. One-command CPU regeneration

After all GPU exports and LOIO residual files are immutable, copy and edit
`configs/submission_cpu_pipeline.example.json`. Add MPDD as another artifact
set/job if its audit passes. Then run:

```bash
python scripts/run_cpu_submission_pipeline.py \
  --config configs/submission_cpu_pipeline.final.json
```

The command performs the fail-closed dataset audit, runs all declared routing
modes and resource/normalization ablations, emits the paired target-only,
pooled-source and nested-SC3R methods, calculates family-wise Bonferroni
bootstrap intervals for analyses marked `confirmatory=true`, and writes SHA-256
checksums plus environment/git state to `cpu_pipeline_manifest_*.json`. It also
creates a paired-cell audit, zero-preserving summaries, an empirical target-gate
JSON, and per-job LaTeX table fragments. The table fragments are review inputs;
do not insert them into the manuscript until all failed gate rows have been
reconciled with the Results and Limitations text.

The CPU-only code path was verified with `requirements-cpu-lock.txt`. On the
GPU server, record the exact Python, PyTorch, torchvision, CUDA, cuDNN, driver,
GPU model, and DINOv2 code/weight identifiers in a separate lock/environment
file; do not replace the CUDA-specific environment with the CPU lock.

Required audit flags for the frozen primary grid are equivalent to:

```bash
python scripts/audit_sc3r_artifacts.py \
  --views VIEW.csv --support-stats SUPPORT.csv \
  --support-manifest SUPPORT_MANIFEST.csv \
  --expected-k-shots 1 2 4 8 --expected-seeds 0 1 2 3 4 \
  --expected-corruptions clean gaussian_noise blur brightness_contrast jpeg \
  --out AUDIT.json
```

Immediately before submission, run the separate package gate:

```bash
python scripts/audit_submission_package.py \
  --root els-cas-templates \
  --cpu-manifest outputs/submission_cpu/cpu_pipeline_manifest_RUN_TAG.json \
  --out outputs/submission_audit.json
```

This final command must return exit code 0. It intentionally fails for author,
repository, evidence, checksum, LaTeX-reference, or duplicate-anchor blockers.

Final manuscript rules:

- “proved” only for Proposition 1 and explicitly stated conditional bounds;
- “certified” only for cells passing the declared category-level UCB gate;
- “empirical” for historical SC3R and target transfer;
- never copy a number reconstructed from a PDF into a final evidence table;
- report negative and boundary cases, including `k=1,2`, heavy corruptions, and
  zero-threshold fallback frequency.
