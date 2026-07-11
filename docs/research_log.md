# Research Log

Use this file for paper notes, useful observations, and decisions that affect
the scientific story.

For a concise claim tracker, see [`novelty_claims.md`](novelty_claims.md).
For an onboarding-friendly explanation of the current novelty and claims, see
[`novelty_claims_explained.md`](novelty_claims_explained.md).
For the latest post-P0/P1 claim status, see
[`novelty_claim_explained_2.md`](novelty_claim_explained_2.md).

## Initial scaffold

- Goal: compare frozen DINOv2 few-shot memory-bank methods with small
  trainable HeadPCA and LoRAHeadPCA variants.
- Required axes: AUROC/AP/F1, calibration, robustness, inference memory, and
  cross-dataset transfer.



## 2026-06-29 MVTec full result interpretation

- Full-grid MVTec aggregation is complete and clean: 1500/1500 expected metrics found.
- Main method `calib_subspace_head` is not an AUROC winner against PatchCore/AnomalyDINO on the full mean, but it is much better calibrated at larger k and far cheaper than memory-bank baselines.
- Recommended Q1 framing: decoupled calibrated subspace scoring as a low-storage calibrated alternative to memory-bank few-shot anomaly detection.
- Next benchmark priority: corruption robustness on full MVTec for `calib_subspace_head`, then selected baselines for clean-vs-corrupt drops.

## 2026-06-29 - MVTec full corruption robustness complete

- Completed full MVTec corruption robustness for `calib_subspace_head`: 15 classes x k `{1,2,4,8}` x 5 seeds x 4 corruptions = `1200/1200` metrics.
- Added `scripts/evaluate_corruptions_batch.py` to fit the model once per config and evaluate multiple corruptions, then used a 4-worker wrapper after confirming GPU utilization was idle and DINOv2 features were cached.
- Added `scripts/aggregate_robustness.py` and generated:
  - `outputs/paper_tables/mvtec_calib_subspace_head_robustness_detailed.csv`
  - `outputs/paper_tables/mvtec_calib_subspace_head_robustness_summary.csv`
  - `outputs/paper_tables/mvtec_calib_subspace_head_robustness_summary.md`
- Verification: `bash scripts/run_tests.sh` -> `16 passed, 1 skipped`.


## 2026-06-30 - Paper benchmark expansion complete

- Completed VisA full clean benchmark: 12 classes x k `{1,2,4,8}` x 5 seeds x 5 variants = `1200/1200` metrics.
- Generated `outputs/paper_tables/visa_full_clean_summary.csv`.
- VisA supports a stronger AUROC story than MVTec for the calibrated subspace family:
  - `calib_subspace_head` vs PatchCore/AnomalyDINO AUROC: k1 `0.8226` vs `0.8038`, k2 `0.8534` vs `0.8387`, k4 `0.8696` vs `0.8619`, k8 `0.8796` vs `0.8729`.
  - Storage remains small: `0.4722 MB` for `calib_subspace_head` vs PatchCore/AnomalyDINO `2.0054-6.0000 MB`.
  - ECE improves with k for `calib_subspace_head` (`0.4295 -> 0.2047`) and is much better than PatchCore/AnomalyDINO at k4/k8, but `head_pca` has even lower ECE/NLL in this implementation.
- Completed all-variant MVTec corruption robustness aggregation:
  - `outputs/paper_tables/mvtec_robustness_all_detailed.csv`
  - `outputs/paper_tables/mvtec_robustness_all_summary.csv`
  - `outputs/paper_tables/mvtec_robustness_all_summary.md`
  - Total paired clean/corruption rows: `6000`.
- Completed MVTec FGSM image-space surrogate benchmark for `calib_subspace_head`: `300/300` runs.
  - Output: `outputs/paper_tables/mvtec_fgsm_summary.csv` and `.md`.
  - FGSM `epsilon=8/255` causes severe AUROC collapse: clean `0.9038-0.9452` to attacked `0.4397-0.4489`, relative drop about `49.8-52.6%`.
  - Paper claim should not say adversarial robustness is solved. Better claim: the benchmark exposes adversarial fragility and reports calibration/uncertainty degradation under a unified protocol.

## 2026-06-30 - Full MVTec ablations complete

- Completed full ablation grid: 15 classes x k `{1,4,8}` x 5 seeds x 10 ablation settings = `2250/2250` metrics.
- Added and ran `scripts/aggregate_ablations.py`.
- Generated:
  - `outputs/paper_tables/mvtec_ablation_detailed.csv`
  - `outputs/paper_tables/mvtec_ablation_summary.csv`
  - `outputs/paper_tables/mvtec_ablation_summary_compact.csv`
  - `outputs/paper_tables/mvtec_ablation_summary.md`
- Ablation result: decoupling is justified.
  - `alpha=0.0`/PCA-only ranking gives strong AUROC: k1 `0.9038`, k4 `0.9371`, k8 `0.9452`.
  - Increasing alpha toward head-only improves calibration metrics but hurts AUROC, especially k1 (`alpha=1.0` AUROC `0.8016`).
  - This supports the method design: keep PCA/subspace residual as ranking score, use head/calibrator for probability/uncertainty rather than replacing the ranking score.
- PCA components:
  - `16` components underfit badly (`0.8615-0.8682` AUROC).
  - `64` is the balanced default (`0.9038/0.9371/0.9452` for k1/k4/k8).
  - `128` improves AUROC (`0.9003/0.9418/0.9517`) and storage modestly (`0.5659 MB`), so include as an ablation and possible high-accuracy setting.
- Upper-bound calibration:
  - `normal_plus_anomaly_val` reduces ECE strongly: k1 `0.2114`, k4 `0.1400`, k8 `0.1103`.
  - This is an upper-bound only because it uses held-out anomaly labels; main claim should use `normal_synthetic`.
- Final verification after ablations: `bash scripts/run_tests.sh` -> `16 passed, 1 skipped`.

## 2026-07-01 - Post-P0/P1 novelty status

- Added `docs/novelty_claim_explained_2.md` to capture the current Q1 paper framing after P0/P1.
- P0 is complete: pixel metrics `1500` rows, calibration ablation `900` rows, heatmap tooling available, and tests currently pass with `19 passed, 1 skipped`.
- P1 main artifacts are complete: MVTec to VisA transfer `240` rows, VisA robustness aggregation, and FGSM sweep `900/900` runs across eps `{2/255,4/255,8/255}`.
- Updated claim: calibrated low-storage subspace detector plus transfer and robustness diagnostics. Do not claim MVTec SOTA AUROC or adversarial robustness.
- Important caveat: FGSM sweep is severely damaging but non-monotonic (`2/255` gives lower AUROC than `8/255`), so attack direction/objective and surrogate score sign need audit before making strong robustness statements.


## 2026-07-02 - P1/P2 test-plan refresh and artifact finalization

- Re-ran verification after quota reset: `bash scripts/run_tests.sh` -> `19 passed, 1 skipped`.
- Refreshed benchmark artifacts: FGSM sweep (`900` runs), MVTec robustness (`6000` paired runs), VisA robustness (`2872` paired runs), uncertainty aggregation (`14745` rows), runtime audit (`4737` runs), pixel metrics (`1500` runs), and calibration ablation (`900` rows).
- Added paper artifact scripts: `scripts/generate_calibration_curves.py`, `scripts/aggregate_selective_risk.py`, and `scripts/build_paper_ready_tables.py`. Generated `calibration_reliability_bins_*`, `selective_risk_*`, and `paper_ready_tables.md`.
- Rendered representative heatmaps for MVTec clean, MVTec brightness/contrast, MVTec FGSM 8/255, and VisA clean into `outputs/figures/`.
- New caution: selective-risk analysis supports entropy as a diagnostic signal, but low-entropy 50% coverage does not consistently improve AUROC versus full coverage. Do not claim selective prediction/risk reduction yet.


## 2026-07-02 - FGSM Objective Audit

- Added and ran `scripts/audit_fgsm_objective.py` on representative MVTec classes (`bottle`, `cable`, `hazelnut`, k=1 seed=0, 20 eval images each).
- Output: `outputs/paper_tables/fgsm_objective_audit_summary.csv` and per-class CSV/JSON under `outputs/paper_tables/fgsm_audit_cases/`.
- Finding: current FGSM `ascent` objective is label-aware BCE on PCA residual logits. It increases normal scores more strongly than anomaly scores, directly compressing or reversing anomaly ranking. Across the three audit cases, mean AUROC under ascent is roughly `0.217` at `2/255`, `0.220` at `4/255`, and `0.553` at `8/255` on the 20-image audit subset.
- Interpretation: severe FGSM collapse is expected for this label-aware ranking attack, but the non-monotonic epsilon behavior is plausibly caused by clipping/saturation and the surrogate objective, not necessarily a clean robustness law.
- Paper rule: report this as `label-aware PCA-residual FGSM surrogate` and avoid claiming standard adversarial robustness. Keep it as a diagnostic/failure-case table unless we implement an additional standard attack protocol.


## 2026-07-02 - Official SubspaceAD Reproduction Setup And Representative Run

- Cloned official repository: `third_party/SubspaceAD` from `https://github.com/CLendering/SubspaceAD`.
- Official README confirms SubspaceAD is frozen DINOv2 + PCA/subspace residual and reports strong few-shot results; therefore our paper must not claim DINOv2 PCA residual as novel.
- Installed official requirements into `ad` env and installed package editable. Setup notes: `transformers`, `scikit-learn`, `opencv-python`, `kornia`, and `anomalib` were missing before install.
- Official default protocol is much stronger/different from our local baseline: `facebook/dinov2-with-registers-giant`, `image_res=672`, `aug_count=30`, `pca_ev=0.99`.
- Smoke issue: using `facebook/dinov2-with-registers-small` with default layers `-12..-18` fails because the small model has fewer hidden layers. Fixed smoke command with `--layers=-1,-2,-3,-4`.
- Representative official run, MVTec k=1 seed=0, classes `bottle cable hazelnut`, checkpoint `facebook/dinov2-with-registers-small`, image_res `224`, no augmentation: average image AUROC `0.9518`, image AUPR `0.9752`, pixel AUROC `0.9710`, AU-PRO `0.8685`. Output: `outputs/official_subspacead_small_threeclass/.../benchmark_results.csv`.
- Interpretation: even a lightweight official SubspaceAD variant is very strong. Main novelty must stay on calibration/low-storage/transfer diagnostics, not raw subspace accuracy.


## 2026-07-02 - Cross-Dataset Calibration Ablation Started

- Added `scripts/evaluate_transfer_calibration_ablation.py` for three VisA calibration modes: `mvtec_transfer_normal_synthetic`, `visa_normal_synthetic`, and `visa_anomaly_val_upper_bound`.
- Smoke passed on `candle`, k=1 seed=0, all 3 modes.
- Partial foreground run was stopped after 41/720 rows to avoid occupying the interactive session for more than an hour; CSV is resume-safe.
- Complete sanity subset for k=1 seed=0 over all 12 VisA classes was saved to `outputs/paper_tables/transfer_calibration_ablation_k1_seed0_summary.csv`.
- k=1 seed0 result: MVTec-transfer ECE `0.4309`, VisA normal-synthetic ECE `0.4299`, upper-bound anomaly-val ECE `0.3784`; AUROC remains about `0.822` across modes, as expected because calibration does not change ranking.


## 2026-07-02 - Background Full Transfer Calibration Ablation

- Started full resume job with `setsid` after plain `nohup` did not keep the process alive.
- PID file: `outputs/logs/transfer_calibration_ablation_full.pid`; current PID at launch: `134364`.
- Log file: `outputs/logs/transfer_calibration_ablation_full.log`.
- Command: `/home/crl/miniconda3/envs/ad/bin/python -u scripts/evaluate_transfer_calibration_ablation.py --out-dir outputs/paper_tables --resume`.
- Output files update incrementally: `outputs/paper_tables/transfer_calibration_ablation_detailed.csv` and `outputs/paper_tables/transfer_calibration_ablation_summary.csv`.

## 2026-07-02 - Parallel finding audit while transfer calibration ablation runs

- Background transfer calibration ablation continued from `180/720` to at least `211/720` while CPU-only artifact aggregation was run.
- Added `scripts/summarize_parallel_findings.py` to collect representative official SubspaceAD results and high-signal ablation findings into paper-table artifacts.
- Regenerated `outputs/paper_tables/mvtec_ablation_summary.csv` from `2250` ablation runs and rebuilt `outputs/paper_tables/paper_ready_tables.md`.
- New artifacts:
  - `outputs/paper_tables/official_subspacead_representative.csv`
  - `outputs/paper_tables/parallel_findings_for_claims.csv`
- Official SubspaceAD representative check on MVTec k=1 seed=0, classes `bottle/cable/hazelnut`, small register DINOv2, no augmentation: average image AUROC `0.9518`, image AUPR `0.9752`, pixel AUROC `0.9710`, AU-PRO `0.8685`.
- Claim impact: official SubspaceAD is strong enough that the paper should not claim raw DINOv2+PCA/subspace novelty. The stronger angle remains calibrated low-storage subspace detection plus transfer/robustness diagnostics.
- Ablation finding: PCA128 improves AUROC at k=4/k=8 with storage still below `0.6 MB`; alpha/head-score mixing improves ECE when head dominates but hurts AUROC, supporting decoupled ranking and calibration.


## 2026-07-02 - Transfer Calibration Ablation Completed And Paper Claims Updated

- Full transfer calibration ablation completed: `720/720` runs.
- Outputs: `outputs/paper_tables/transfer_calibration_ablation_detailed.csv` and `outputs/paper_tables/transfer_calibration_ablation_summary.csv`.
- MVTec-transfer calibrator to VisA keeps ranking strong: AUROC k1 `0.8226`, k8 `0.8824`.
- Transfer ECE improves with k: `0.4319 -> 0.2324` from k1 to k8.
- VisA normal-synthetic calibration has the same ranking but better high-k ECE: k8 `0.2066`.
- VisA anomaly-val upper-bound is best at k1 ECE `0.3787`, but it does not improve AUROC and must be reported separately.
- Current paper framing is locked to Calibration + Efficiency + Transfer/Robustness Diagnostics. Do not claim MVTec SOTA AUROC, first calibration benchmark, adversarial robustness, or DINOv2 PCA residual novelty.
- Added paper artifacts: `docs/paper_claims_current.md`, `outputs/paper_tables/final_claim_evidence.md`, and `outputs/figures/figure_manifest.md`.


## 2026-07-02 - Official SubspaceAD Representative k-Trend Completed

- P2 official SubspaceAD representative k4/k8 completed for `bottle/cable/hazelnut` using the same lightweight setting as k1: small register DINOv2, image resolution 224, layers `-1,-2,-3,-4`, no augmentation, seed 0.
- Output: `outputs/paper_tables/official_subspacead_representative_k_trend.csv`.
- Average image AUROC trend: k1 `0.9518`, k4 `0.9625`, k8 `0.9639`.
- Average pixel AUROC trend: k1 `0.9710`, k4 `0.9737`, k8 `0.9743`.
- Average AU-PRO trend: k1 `0.8685`, k4 `0.8844`, k8 `0.8908`.
- Interpretation: official SubspaceAD remains very strong as k increases. This further weakens any pure accuracy/SOTA claim for our method and strengthens the need to frame the paper around calibration, storage-efficiency, transfer calibration, and diagnostic benchmarking.


## 2026-07-02 - P2 Priority Experiments Completed

- Completed all three priority P2 probes requested after the official SubspaceAD k-trend run.
- VisA PCA128 representative grid: `27` runs over classes `candle/cashew/pcb1`, k `{1,4,8}`, seeds `{0,1,2}`.
  - Compared against PCA64 on the exact same subset, PCA128 improves AUROC by about `+0.0233` at k1, `+0.0218` at k4, and `+0.0186` at k8.
  - Storage rises modestly from `0.472 MB` to `0.566 MB`.
  - Interpretation: this supports an accuracy-storage Pareto claim on VisA representative classes; do not overgeneralize until full VisA PCA128 is run.
- Shift-Aware Calibration representative grid: `90` rows over VisA `candle/cashew/pcb1` and MVTec `bottle/cable`, k `{1,4,8}`, seeds `{0,1,2}`, comparing vector Platt vs shift-aware vector Platt.
  - VisA ECE improves strongly at k4 (`0.3090 -> 0.2183`) and k8 (`0.2152 -> 0.1148`), with unchanged AUROC because ranking is unchanged.
  - MVTec is mixed: k8 improves (`0.1581 -> 0.1518`), but k4 worsens (`0.2448 -> 0.2606`) and k1 is similar.
  - Interpretation: Shift-Aware Calibration is promising specifically for transfer/VisA calibration under shift; it should be tested on full VisA and corruptions before becoming a main method claim.
- No-cache runtime representative audit: `6` runs on MVTec `bottle/cable` and VisA `candle`, k `{1,8}`.
  - End-to-end wall-clock including feature extraction/model fit/output is roughly `9-10s` for MVTec representative cases and `14-17s` for VisA candle cases on this machine, while cached scoring latency remains around milliseconds/image.
  - Interpretation: paper must distinguish cached-feature latency from end-to-end setup/runtime.
- New artifacts: `visa_pca128_representative_summary.csv`, `visa_pca64_vs_pca128_representative_delta.csv`, `shift_aware_calibration_representative_summary.csv`, and `runtime_no_cache_representative_summary.csv`.


## 2026-07-02 - Full VisA PCA128 And Shift-Aware Calibration Completed

- Completed the two priority full-grid directions requested after the P2 representative probes.
- Full VisA PCA128 grid completed: `240` runs over 12 VisA classes, k `{1,2,4,8}`, seeds `{0,1,2,3,4}`.
- Full Shift-Aware Calibration grid completed: `480` rows comparing `vector_platt` and `shift_aware_vector_platt` over the same VisA grid.
- Outputs:
  - `outputs/paper_tables/visa_pca128_full_visa_detailed.csv`
  - `outputs/paper_tables/visa_pca128_full_visa_summary.csv`
  - `outputs/paper_tables/visa_pca64_vs_pca128_full_visa_delta.csv`
  - `outputs/paper_tables/shift_aware_calibration_full_visa_detailed.csv`
  - `outputs/paper_tables/shift_aware_calibration_full_visa_summary.csv`
  - `outputs/paper_tables/shift_aware_calibration_full_visa_delta.csv`
- PCA128 full VisA result: AUROC improves over PCA64 by `+0.0110`, `+0.0150`, `+0.0156`, `+0.0171` at k1/k2/k4/k8, with storage increasing only from about `0.472 MB` to `0.566 MB`.
- Shift-Aware Calibration full VisA result: AUROC is unchanged by design, but calibration improves strongly at k4 and k8. ECE changes vs vector Platt: k1 `+0.0025`, k2 `-0.0013`, k4 `-0.0807`, k8 `-0.0619`.
- Interpretation: this supports a stronger, more specific paper claim: PCA128 gives a low-storage accuracy-storage Pareto improvement on VisA, and Shift-Aware Calibration improves reliability for moderate/high-shot VisA without changing ranking. Keep k1 as a caveat.


## 2026-07-02 - Shift-Aware Corruption Calibration Started

- Added official model variant `shift_aware_calib_subspace_head` in `src/models/head_pca.py` and registered it in `src/models/baselines.py`.
- Added runner `scripts/evaluate_shift_aware_corruption_calibration.py` to compare `vector_platt` vs `shift_aware_vector_platt` under corrupted evaluation images.
- Added unit coverage for the shift-aware variant; test suite passes with `20 passed, 1 skipped`.
- Smoke experiment passed on VisA `candle`, k=1, seed=0, Gaussian noise, `max_images=10`.
- Started full background job for the main corruption-calibration claim:
  - dataset: VisA;
  - classes: all 12 VisA classes;
  - k: `{4,8}`;
  - seeds: `{0,1,2,3,4}`;
  - corruptions: Gaussian noise, blur, brightness/contrast, JPEG;
  - methods: vector Platt vs shift-aware vector Platt;
  - total expected rows: `960`.
- Background PID file: `outputs/logs/shift_aware_corruption_visa_k4k8_full.pid`.
- Background log: `outputs/logs/shift_aware_corruption_visa_k4k8_full.log`.
- Main outputs:
  - `outputs/paper_tables/shift_aware_corruption_calibration_visa_k4k8_full_corruptions_detailed.csv`
  - `outputs/paper_tables/shift_aware_corruption_calibration_visa_k4k8_full_corruptions_summary.csv`
  - `outputs/paper_tables/shift_aware_corruption_calibration_visa_k4k8_full_corruptions_delta.csv`
- Novelty check saved in `docs/shift_aware_novelty_verification.md`. Guardrail: this is not first calibration-under-shift or first DINOv2 few-shot calibration; the defensible novelty is shift-aware vector calibration for low-storage DINOv2 subspace few-shot industrial AD under transfer/corruption shift.


## 2026-07-03 - Shift-Aware Corruption Calibration Full VisA Completed

- Full VisA shift-aware corruption calibration completed: `960/960` rows.
- Grid: 12 VisA classes, k `{4,8}`, seeds `{0,1,2,3,4}`, corruptions `{gaussian_noise, blur, brightness_contrast, jpeg}`, methods `{vector_platt, shift_aware_vector_platt}`.
- Outputs:
  - `outputs/paper_tables/shift_aware_corruption_calibration_visa_k4k8_full_corruptions_detailed.csv`
  - `outputs/paper_tables/shift_aware_corruption_calibration_visa_k4k8_full_corruptions_summary.csv`
  - `outputs/paper_tables/shift_aware_corruption_calibration_visa_k4k8_full_corruptions_delta.csv`
- AUROC/AP are unchanged by design because Shift-Aware Calibration does not change the PCA/subspace ranking.
- ECE improves strongly under structured corruptions:
  - blur k4/k8: `0.2844 -> 0.2111`, `0.2078 -> 0.1439`.
  - brightness/contrast k4/k8: `0.2845 -> 0.2118`, `0.2086 -> 0.1532`.
  - JPEG k4/k8: `0.2876 -> 0.2297`, `0.2119 -> 0.1564`.
- Gaussian noise is the caveat: ECE slightly worsens at k4/k8: `0.2695 -> 0.2762`, `0.1900 -> 0.1913`, although NLL still improves slightly.
- Interpretation: Shift-Aware Calibration is useful for structured/domain-style shifts such as blur, illumination/contrast, and compression, but it is not a universal fix for stochastic additive noise. This should be stated explicitly in the paper.


## 2026-07-07 - Anchored Gated Shift-Aware Calibration

Implemented SAGE-inspired anchored gated calibration. Vector Platt is used as a safe anchor and shift-aware/weighted experts are applied as corrections: `p_final = p_vector + lambda(x) * (p_expert_mix - p_vector)`. Representative results: on VisA, `anchored_soft_gate_adaptive` improves mean ECE from `0.2711` to `0.2597` with no-harm `8/8`; on representative MVTec it stays near vector (`0.2562` to `0.2598`) with no-harm `8/8`. Direct shift-aware/weighted experts remain strong on VisA but harmful on MVTec, supporting the claim that dynamic calibration routing is necessary. See `docs/gated_shift_aware_universal_results.md`.

## 2026-07-08 - Full MVTec Gated Shift-Aware Completed

- Ran full MVTec Gated Shift-Aware grid: 15 classes, k `{4,8}`, seeds `{0,1,2}`, corruptions `{gaussian_noise, blur, brightness_contrast, jpeg}` = `360/360` cases.
- Had to move tmp-root from `/tmp` to `/home/crl/AD/tmp/shift-aware-corruptions` because `/tmp` filled the root partition. Metrics/docs were preserved; only temp corruption/cache files were deleted.
- Final MVTec result: Vector Platt ECE `0.1952`; `anchored_structured_gate` ECE `0.1954`; direct `shift_aware_vector_platt` ECE `0.2164`; `weighted_platt` ECE `0.2169`; oracle best ECE `0.1853`.
- Interpretation: MVTec does not support universal improvement over Vector Platt. It supports the need for gated/anchored routing because direct shift-aware/weighted experts over-adapt.

## 2026-07-09 - SAGE-Style Offline Gate Tests

- Added dependency-free offline SAGE-style gate evaluation: logistic top-1/top-2, risk-aware margin gate, and hierarchical shared/dynamic gate.
- Added a view-expert pool beyond calibrator-only experts: safe Vector Platt, shift descriptor view, density-ratio view, and anchored routing view.
- Tests pass: `30 passed, 1 skipped`.
- Leave-one-class-out over full VisA+MVTec shows strong signal: risk-aware gate improves ECE by about `-0.022` vs Vector Platt over `648` cases.
- Cross-dataset remains asymmetric: MVTec -> VisA improves, while VisA -> MVTec needs conservative hierarchical thresholding to avoid over-adaptation.
- Updated interpretation: SAGE-style gate is promising as a reliability-layer router, but current result is offline case-level evidence, not yet a deployed sample-level gate.

## 2026-07-09 - Sample-Level SAGE Gate Representative

- Completed sample-level SAGE-style gate representative grid: 112/112 cases, 12128 per-image predictions, 126 evaluation rows.
- Best signal: cross MVTec -> VisA, `sample_sage_hier_t0.5` ECE `0.2190`, better than weighted/shift-aware around `0.230-0.232`.
- VisA -> MVTec improves mildly over Vector Platt: `0.3035 -> 0.2988` with conservative hierarchical threshold `0.6`.
- LOCO gains are modest. Sample-level gate is promising but not yet a decisive main claim; objective should be ECE/risk-aware rather than NLL-only.

## 2026-07-09 - Brier/No-Harm Sample Gate Update

- Added `BrierMixtureGate`, a soft expert mixture trained directly on Brier with optional anchor/no-harm penalties.
- Tests pass: `31 passed, 1 skipped`.
- Reran sample-level representative evaluation from cached predictions: `162` evaluation rows.
- Brier/no-harm gates did not beat the best SAGE hierarchical gate on ECE. Best current sample-level result remains `sample_sage_hier_t0.5` for MVTec -> VisA (`0.2190` ECE) and `sample_sage_hier_t0.6` for VisA -> MVTec (`0.2988` ECE).
- Finding: Brier/no-harm is still misaligned with ECE; next gate objective should optimize group ECE/risk-coverage or validation-class ECE directly.



## 2026-07-09 - P0-P3 Reliability Routing Plan Completed

- Completed remaining tests for the three-direction Q1 novelty plan. Test suite passes: `36 passed, 1 skipped`.
- P2 SW-CAD image views completed on the representative grid:
  - VisA: `64/64` cases, `7360` image rows.
  - MVTec: `48/48` cases, `4768` image rows.
  - Combined: `12128` rows, merged with sample-gate predictions with `missing_conformal=0`.
- Fixed two infrastructure issues during the run:
  - `/tmp/AD-feature_cache` filled the root partition; removed regenerable feature cache and moved cache back into `/home/crl/AD/outputs/feature_cache`.
  - `torch.hub.load` attempted GitHub access and hit HTTP 504; patched DINOv2 loader to prefer local Torch Hub cache.
- P3 Gated + Conformal View full representative result is strong:
  - LOCO ECE: Vector `0.3039` -> gate `0.1156`, delta `-0.1883`, no-harm `1.0`.
  - Within split ECE: Vector `0.3606` -> gate `0.1537`, delta `-0.2068`, no-harm `1.0`.
  - MVTec -> VisA ECE: Vector `0.3014` -> gate `0.0985`, delta `-0.2028`, no-harm `1.0`.
  - VisA -> MVTec ECE: Vector `0.3035` -> gate `0.1019`, delta `-0.2016`, no-harm `1.0`.
- Gate consistently selects `conformal_prob_loio`, so the new strongest idea is conformal reliability routing rather than calibrator-only SAGE gating.
- Selective reliability with conformal views is also strong at 80% coverage: all `40.9%` ECE reduction, VisA `49.7%`, MVTec `64.6%` in the best representative settings.
- Caveat: current validation-ECE gate uses validation labels to select the conformal view. For paper-grade main protocol, lock a held-out validation protocol or develop a normal-only/no-label routing rule.

## 2026-07-09 - Six-Item Follow-up Started and Core Items Completed

- Locked the method framing to **low-storage decoupled DINOv2 subspace detector with conformal reliability routing**.
- Added `scripts/evaluate_conformal_routing_protocols.py` to compare fixed/no-label/validation protocols.
- Ran protocol evaluation on `sage_sample_gate_representative_with_conformal_full.csv`: `80` detailed rows over `12128` images.
- Key result: `fixed_conformal_loio` does not need validation-label expert selection and still improves ECE strongly over Vector Platt across representative LOCO, within, MVTec -> VisA, and VisA -> MVTec splits.
- Created `outputs/paper_tables/conformal_routing_claim_evidence.md`.
- Created docs:
  - `docs/conformal_reliability_routing_claim.md`
  - `docs/conformal_novelty_verification.md`
- Started full VisA conformal-view scale-up job: PID `2329967`, log `logs/sw_cad_image_views_visa_full_k4k8_s0s4.log`.

## 2026-07-10 - Full VisA Conformal Benchmark Completed

- Completed full VisA conformal export: `480/480` cases, `56,000` image rows.
- Merged shard outputs into `outputs/paper_tables/sw_cad_image_views_visa_full_k4k8_s0s4_combined.csv` with no duplicate rows.
- Generated full analysis artifacts:
  - `outputs/paper_tables/visa_full_conformal_main_table.md`
  - `outputs/paper_tables/visa_full_conformal_extended_summary.csv`
  - `outputs/paper_tables/visa_full_conformal_vs_baselines_k_corruption.csv`
  - `outputs/paper_tables/visa_full_conformal_reliability_bins.csv`
  - `outputs/paper_tables/visa_full_conformal_selective_reliability.csv`
  - `outputs/figures/visa_full_conformal_figure_manifest.md`
- LOIO conformal full VisA result: overall ECE `0.0766`, k4 ECE `0.0391`, k8 ECE `0.1140`.
- LOIO beats Vector Platt and Shift-Aware Platt in every tested k/corruption ECE cell.
- Weighted conformal is mixed: useful for some k8 structured corruptions, bad for k4 and Gaussian noise.
- Freed regenerable feature cache and temporary corruptions after completion; `/home` returned to about `90GB` free.

## 2026-07-10 - First Paper Draft Scaffold Created

- Created first LaTeX manuscript scaffold under `paper/` with abstract, introduction, related work, method, experiments, results, limitations, and conclusion.
- Generated LaTeX tables from current artifacts:
  - `paper/tables/tab_visa_full_conformal.tex`
  - `paper/tables/tab_visa_ece_by_corruption.tex`
  - `paper/tables/tab_protocol_routing.tex`
- Draft references full VisA reliability figures from `outputs/figures/`.
- Wrote `docs/paper_draft_status.md` to summarize draft status and next paper tasks.
- `pdflatex` was not available in PATH, so no local PDF compile was attempted.
