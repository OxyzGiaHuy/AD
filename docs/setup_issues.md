# Setup Issues

Record install problems, environment versions, CUDA/cuDNN/PyTorch mismatches,
and fixes here.

## Template

- Date:
- Command:
- Error:
- Root cause:
- Fix:
- Follow-up:


## 2026-06-27 sandbox bwrap issue

- Command: `python3 -m src.run_experiment --config configs/experiments/smoke_synthetic.yaml` and some `apply_patch` reads.
- Error: `bwrap: loopback: Failed RTM_NEWADDR: Operation not permitted`.
- Root cause: managed sandbox wrapper blocked Python/apply_patch execution in this environment.
- Fix: reran verification commands with approved escalation; used minimal workspace-local Python edit only when `apply_patch` repeatedly failed.
- Follow-up: prefer normal `apply_patch`; escalate Python verification when the same sandbox wrapper error appears.

## 2026-06-27 pytest ROS plugin autoload issue

- Command: `python -m pytest -q`.
- Error: `ModuleNotFoundError: No module named 'lark'` while importing `/opt/ros/jazzy/.../launch_testing`.
- Root cause: pytest auto-loaded globally installed ROS plugins unrelated to this repo; the active conda env did not contain the plugin dependency set.
- Fix: added repo-local `sitecustomize.py` with `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1`.
- Follow-up: run tests from repo root so Python sees the local startup file.

- Also added `pyproject.toml` pytest addopts `-p no:launch_testing -p no:launch_ros` and `scripts/run_tests.sh` as a robust fallback.

## 2026-06-28 dataset storage check

- `/home` has only about 6.5GB free, which is not enough for safe dataset download/extraction.
- `/tmp` has about 379GB free, so dataset script defaults to `/tmp/AD-data` and symlinks into repo `data/`.
- VisA URL used by script: `https://amazon-visual-anomaly.s3.us-west-2.amazonaws.com/VisA_20220922.tar`.
- MVTec AD still requires user-provided official URL after accepting the license/form.

## Dataset Download Note

- Downloaded VisA from official Amazon S3 URL.
- Archive: `/tmp/AD-data/archives/VisA_20220922.tar`
- Extracted: `/tmp/AD-data/visa`
- Repo link: `data/visa`

## 2026-06-28 Kaggle MVTec note

- Requested Kaggle dataset: `ipythonx/mvtec-ad`.
- Current machine does not have `kaggle` CLI or `/home/crl/.kaggle/kaggle.json`.
- Added `scripts/download_datasets.py --dataset mvtec_kaggle` support.
- Next step: install Kaggle CLI and provide API token before download.

## Dataset Download Note

- Downloaded MVTec AD from user-provided official/license URL.
- Archive: `/tmp/AD-data/archives/mvtec_ad.tar.xz`
- Extracted: `/tmp/AD-data/mvtec`
- Repo link: `data/mvtec`

## 2026-06-28 cannot move datasets into repo data

- Request: move datasets from `/tmp/AD-data` so they live directly under `/home/crl/AD/data`.
- Current free space on `/home`: about 4.0GB.
- Dataset sizes: MVTec about 5.0GB, VisA about 1.9GB.
- Result: cannot safely materialize both datasets, and cannot materialize MVTec alone, without freeing more `/home` space.
- Current workaround: keep `data/mvtec` and `data/visa` as symlinks to `/tmp/AD-data`.

## 2026-06-28 PatchCore memory issue

- Command: PatchCore/AnomalyDINO baseline on DINOv2 MVTec bottle cached features.
- Error: NumPy tried to allocate about 223 GiB for raw pairwise distances.
- Root cause: naive nearest-neighbor broadcasting over all eval patches and memory patches.
- Fix: replaced broadcasting with chunked squared-distance formula `||x||^2 + ||m||^2 - 2 x m^T`.

## 2026-06-28 MLP head reproducibility issue

- Finding: HeadPCA metrics changed between reruns because TorchMLPHead seeded NumPy but not PyTorch.
- Fix: added `torch.manual_seed(seed)` and `torch.cuda.manual_seed_all(seed)` before model initialization/training.

## 2026-06-28 VectorPlatt orientation guard

- Finding: `calib_subspace_head` normal_synthetic vector calibration produced near-zero probabilities for high anomaly scores on MVTec bottle k=1.
- Root cause: with one normal support image, synthetic calibration features can produce an inverted logistic orientation.
- Fix: added an orientation guard in `VectorPlattScaler.fit` that flips weights/bias if positive synthetic examples have lower mean probability than negatives.

## 2026-06-28 VectorPlatt low-variance feature issue

- Finding: `z_disagreement` was nearly constant in 1-shot synthetic calibration data, causing huge standardized values at eval time.
- Fix: clip `VectorPlattScaler` feature std to at least 1.0 for stable few-shot vector calibration.

## 2026-06-28 vector calibration stability note

- Issue: initial vector calibration produced degenerate probabilities under 1-shot because support-only feature std was nearly zero.
- Fix: normalize calibrator features using support normal plus synthetic feature anomalies, and constrain PCA residual coefficient to be non-negative.
- Remaining risk: normal_synthetic calibration is still overconfident; compare against normal_plus_anomaly_val and reliability diagrams.

## 2026-06-28 - Fixed `normal_plus_anomaly_val` Calibration Split

- Issue: `run_experiment.py` created a held-out anomaly calibration split via `split_calibration()` but discarded the returned calibration records. The upper-bound calibrator then sampled positives from the remaining eval set, which made the protocol ambiguous and risked leakage/misreporting.
- Fix: `run_once()` now encodes `calib_records` separately and passes held-out calibration features/scores into Platt or VectorPlatt calibration. Eval metrics/predictions are computed only on `eval_records` after removing held-out anomalies.
- Verification: `bash scripts/run_tests.sh` passed `14 passed, 1 skipped`; `smoke_synthetic_upper_bound` completed and wrote `calibration_anomaly_val_count: 1`.

## 2026-06-28 - Aggregator Calibration/Ablation Grouping Fix

- Issue: `scripts/aggregate_paper_tables.py` grouped by dataset/variant/k only, which could mix `normal_synthetic` with `normal_plus_anomaly_val` and also merge alpha ablations into the same `head_pca` row.
- Fix: parser now extracts `calibration_mode` and `experiment`; default grouping is `dataset,experiment,variant,k_shot,calibration_mode`.
- Verification: `outputs/paper_tables/mvtec_bottle_summary.csv` now separates `calib_subspace_mvtec_bottle`, `calib_subspace_mvtec_bottle_upper_bound`, and each `headpca_alpha_*` ablation row.


## 2026-06-29 sandbox patch limitation

- Issue: `apply_patch` still fails with `bwrap: loopback: Failed RTM_NEWADDR: Operation not permitted` in this managed sandbox.
- Impact: source edits through the preferred patch tool are blocked for now.
- Workaround used only for generated artifacts/docs: Python commands with escalation wrote paper table Markdown/CSV and appended research logs.
- Follow-up: when patching source is needed, retry `apply_patch`; if it remains blocked, record the exact source diff separately before applying any non-standard edit method.

## 2026-06-29 - Robustness runner engineering notes

- `apply_patch` and some read commands intermittently failed with `bwrap: loopback: Failed RTM_NEWADDR: Operation not permitted`; when this occurred, file edits were done with Python inside the workspace and immediately verified with `py_compile`/tests.
- Initial corruption runner fit the model separately per corruption, which was unnecessarily slow. Added `scripts/evaluate_corruptions_batch.py` so each config fits once and evaluates all missing corruptions.
- A first skip-fast patch accidentally iterated over an empty `pending_corruptions` list; caught by artifact audit (`185/1200` instead of expected growth), fixed, and added a unit test for the robustness aggregator.
- Full robustness was accelerated safely with 4 parallel subprocess workers after checking `nvidia-smi` showed DINOv2 was not active and GPU memory was low.



## 2026-06-30 - Long ablation runner resume behavior

- Full MVTec ablation grid had `2250` configs. The parallel runner completed in multiple segments because long shell sessions/process supervision detached or exited before the whole grid finished.
- No completed metrics were lost because `scripts/run_parallel_grid.py` skips existing `metrics.json` by run id.
- Resume checkpoints observed: `451/2250`, `715/2250`, `1119/2250`, then final resume completed all remaining runs.
- Practical fix: for future long grids, keep `run_parallel_grid.py` skip logic, periodically count `outputs/ablation_*/metrics.json`, and simply rerun the same command until skipped + completed equals expected total.

## 2026-06-30 - Markdown append shell quoting issue

- While appending docs with `python -c`, Markdown backticks inside a double-quoted shell string were interpreted by the shell as command substitution.
- Symptom: warnings such as `command not found` for metric values and paths, and the appended Markdown lost all inline-code content.
- Fix: replaced the broken section and used a single-quoted heredoc (`python - <<'PY'`) with a raw Python string.
- Reminder: use heredoc or `apply_patch` for Markdown containing backticks; avoid `python -c "...` for docs with inline code.


## 2026-07-02 - Artifact Script Dependency Notes

- `scripts/aggregate_selective_risk.py` initially imported `sklearn.metrics`, but the `ad` conda environment does not include `sklearn`. Fixed by using repo-native NumPy metrics from `src.evaluation.metrics`.
- `scripts/build_paper_ready_tables.py` initially used `pandas.DataFrame.to_markdown`, which requires optional dependency `tabulate`. Fixed by adding a minimal Markdown table renderer in the script.
- `apply_patch` intermittently failed with sandbox `bwrap: loopback: Failed RTM_NEWADDR`; small script fixes were applied with escalated Python commands and then verified with `python3 -m py_compile` plus `bash scripts/run_tests.sh`.


## 2026-07-02 - Official SubspaceAD Reproduction Setup And Representative Run

- Cloned official repository: `third_party/SubspaceAD` from `https://github.com/CLendering/SubspaceAD`.
- Official README confirms SubspaceAD is frozen DINOv2 + PCA/subspace residual and reports strong few-shot results; therefore our paper must not claim DINOv2 PCA residual as novel.
- Installed official requirements into `ad` env and installed package editable. Setup notes: `transformers`, `scikit-learn`, `opencv-python`, `kornia`, and `anomalib` were missing before install.
- Official default protocol is much stronger/different from our local baseline: `facebook/dinov2-with-registers-giant`, `image_res=672`, `aug_count=30`, `pca_ev=0.99`.
- Smoke issue: using `facebook/dinov2-with-registers-small` with default layers `-12..-18` fails because the small model has fewer hidden layers. Fixed smoke command with `--layers=-1,-2,-3,-4`.
- Representative official run, MVTec k=1 seed=0, classes `bottle cable hazelnut`, checkpoint `facebook/dinov2-with-registers-small`, image_res `224`, no augmentation: average image AUROC `0.9518`, image AUPR `0.9752`, pixel AUROC `0.9710`, AU-PRO `0.8685`. Output: `outputs/official_subspacead_small_threeclass/.../benchmark_results.csv`.
- Interpretation: even a lightweight official SubspaceAD variant is very strong. Main novelty must stay on calibration/low-storage/transfer diagnostics, not raw subspace accuracy.


## 2026-07-02 - Background Full Transfer Calibration Ablation

- Started full resume job with `setsid` after plain `nohup` did not keep the process alive.
- PID file: `outputs/logs/transfer_calibration_ablation_full.pid`; current PID at launch: `134364`.
- Log file: `outputs/logs/transfer_calibration_ablation_full.log`.
- Command: `/home/crl/miniconda3/envs/ad/bin/python -u scripts/evaluate_transfer_calibration_ablation.py --out-dir outputs/paper_tables --resume`.
- Output files update incrementally: `outputs/paper_tables/transfer_calibration_ablation_detailed.csv` and `outputs/paper_tables/transfer_calibration_ablation_summary.csv`.
