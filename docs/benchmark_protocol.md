# Benchmark Protocol

## Datasets

- MVTec AD: class folders with `train/good`, `test/<defect>`, and optional
  `ground_truth/<defect>` masks.
- VisA: support both MVTec-like folders and CSV-indexed layouts when added.

## Few-shot Protocol

- Use k normal support images per category for k in `{1,2,4,8}`.
- Use seeds `{0,1,2,3,4}`.
- Never leak test images into support or calibration.

## Calibration

- `normal_synthetic`: calibrate from normal support and synthetic anomalies.
- `normal_plus_anomaly_val`: upper-bound mode with a small anomaly validation
  split, reported separately.

## Cross-dataset

- In-dataset: train/calibrate/evaluate separately per dataset.
- MVTec to VisA: tune hyperparameters and fit calibrator on MVTec; on VisA use
  only k normal support images for target PCA/memory structures.


## Paper Q1 Method Variant

- Main method name in code: `calib_subspace_head`.
- Raw ranking score: max PCA residual over DINOv2 patch tokens.
- Calibration features: `[pca_score, head_score, z_disagreement]`.
- Main calibration mode: `normal_synthetic`; `normal_plus_anomaly_val` remains upper-bound only.
- Main claim should emphasize calibration/efficiency/robustness, not guaranteed AUROC dominance.

## Full Benchmark Generation

- Generate MVTec full configs with `python scripts/generate_benchmark_grid.py`.
- Aggregate paper tables with `python scripts/aggregate_paper_tables.py --pattern "*" --out outputs/tables/mvtec_summary.csv`.
- Corruption smoke/full runs use `python scripts/evaluate_corruptions.py --config <config> --corruption gaussian_noise`.

## Calibration Split Implementation Note

- `normal_synthetic` remains the main calibration setting for paper claims.
- `normal_plus_anomaly_val` is an upper-bound setting only: a small held-out test-anomaly validation subset is removed from evaluation, encoded separately, and used only to fit the calibrator with k-shot normal support. Report this table separately from the main no-anomaly-label protocol.

## Aggregation Rule

- Paper tables should group by at least `dataset,experiment,variant,k_shot,calibration_mode` unless intentionally merging repeated seeds of the same exact experiment.
- Do not mix `normal_synthetic` and `normal_plus_anomaly_val`; report the latter as an upper-bound calibration table.
- Do not merge ablation experiment names such as `headpca_alpha_0p0` into the main `head_pca` row.


## MVTec Full Clean Table Artifact

- Clean aggregation source: `configs/generated/mvtec_full/run_list.txt`.
- Audit result: `1500/1500` metrics present.
- CSV table: `outputs/paper_tables/mvtec_full_clean_summary.csv`.
- Markdown table: `outputs/paper_tables/mvtec_full_clean_summary.md`.
- Use the clean table for paper reporting, not broad glob tables such as `*mvtec*`, because old smoke/upper-bound artifacts can contaminate broad pattern aggregation.

## Robustness Artifact Status - 2026-06-29

MVTec corruption robustness for the main method `calib_subspace_head` is now complete. The official artifact set for this phase is:

- Raw run metrics: `outputs/robustness/calib_subspace_head_mvtec_*_calib_subspace_head_k*_seed*_*/metrics.json`
- Detailed joined table: `outputs/paper_tables/mvtec_calib_subspace_head_robustness_detailed.csv`
- Paper summary table: `outputs/paper_tables/mvtec_calib_subspace_head_robustness_summary.csv` and `.md`

The table joins each corrupted run to its matching clean `normal_synthetic` calibration run by `(class, k_shot, seed)` and reports absolute/relative AUROC drop, AP drop, ECE delta, and entropy shift.

