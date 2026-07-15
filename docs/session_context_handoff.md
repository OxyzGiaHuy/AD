# Session Context Handoff

Last updated: 2026-07-14

This document is the high-level handoff for the few-shot anomaly detection paper workspace. Read this first in a new session before running experiments or editing the paper.

## 0a. 2026-07-14 Status Snapshot (read this first)

The paper now lives in **`latex/`** (Springer sn-jnl, target: Neural Computing and Applications) and compiles clean with `cd latex && tectonic main.tex` (25 pp, 0 errors/overfull/unresolved). The `paper/` IEEE tree is legacy V2. All four pre-submission items from 2026-07-12 are DONE:

1. **Standard scalar calibrators (advisor 2.6.i)**: `src/calibration/scalar.py` (temperature/isotonic/histogram + scalar Platt) fit per cell on the exact synthetic protocol and applied offline to views-CSV `raw_score` (reuse verified exact, `verify_ok 0.00e+00`). LOIO beats all of them on both benchmarks/k: Wilcoxon p <= 2.5e-4 in 16/16, <= 4.8e-8 in 14/16; closest isotonic k=8. Tables: `tab_scalar_calibrators.tex`; script `scripts/evaluate_scalar_calibrator_baselines.py` + `build_ncaa_tables.py`.
2. **SC3R k=8 full15**: sub-floor power 0.547/0.693 (alpha 0.05/0.10), power-gain CIs exclude zero for every corruption; FAR budget passes at 0.05 (0.052), marginal miss at 0.10 (0.121, no-harm 74%), gaussian/jpeg drive exceedances (same as k=4). No-harm definition: FAR_SC3R <= max(alpha, FAR_anchor)+0.02. Paper states k=4 full pass + k=8 boundary honestly (`tab_sc3r_k8.tex`).
3. **Figures**: 4 vector PDFs in `latex/figures/` from `scripts/plot_paper_v2_figures.py` (Q-Q uniformity, risk-coverage, reliability, ECE-by-corruption; Okabe-Ito, print fonts).
4. **Ablations**: PCA128 vs PCA64 hierarchical CI excludes zero at all k (`analyze_pca_components_ci.py`); Agg ablation spread 0.01–0.02 AUROC (`evaluate_agg_ablation.py`).

Tests: 60 passed. Remaining before submission: real author block in `latex/main.tex` (placeholder TODO), advisor review, optional WinCLIP + cross-dataset SC3R (kept in limitations). sn-jnl gotcha: do NOT use `\resizebox` around tabular — breaks in sn-jnl tables; use `\footnotesize`.

**Update (2026-07-14 later)**: three more results are IN the paper (see research_log same date): (1) SC3R replicates on all 12 VisA classes (FAR 0.051/0.095/0.192, CIs exclude zero at sub-floor alphas, no-harm 89/84/78%); (2) cross-dataset source archives MVTec→VisA transfer conservatively (FAR 0.013–0.098 below nominal, ~half power, no-harm 93–97%, CIs exclude zero) via new `--source-dataset/--target-dataset` flags in `evaluate_source_validated_threshold.py` — the old "cross-dataset untested" limitation is now a positive result (`tab_sc3r_visa.tex`, Table 10); (3) official AnomalyDINO VisA k=1/4/8×3 seeds (AUROC 0.857/0.912/0.926, matches published) fills the VisA official rows in Table 1; layout `data/visa_pytorch/` built by symlinks from split_csv/1cls.csv. Declarations/Acknowledgements section added (Springer-required); abstract exactly 250 words; cover letter drafted at `latex/cover_letter.md`. Long GPU jobs MUST be launched `setsid nohup` + sentinel file (agent teardown kills session-attached processes; see `scripts/run_visa_sc3r_chain.sh`). Tests: 62 passed. PDF: 26 pp clean. Only remaining: author block + advisor review + optional WinCLIP.

## 0. 2026-07-12 Status Snapshot (superseded by 0a where they conflict)

Major update: all P1/P2 experiments and the SC3R audit are COMPLETE, and the paper is at V2.

1. **SC3R passed its pre-registered gate on all 15 MVTec classes (matched_condition, k=4, seeds 0-2)** and is promoted to a main contribution. Mean FAR `0.050/0.105/0.216` at alpha `0.05/0.10/0.20`; power `0.216/0.416` at sub-floor alphas; no-harm `89/82/89%`; hierarchical power-gain CIs exclude zero for every corruption. Evidence: `source_validated_threshold_sc3r_mvtec_full15_stratified_*.csv`, `sc3r_mvtec_full15_stratified_hierarchical_ci.csv`.
2. **MVTec full 15-class conformal benchmark complete**: LOIO ECE `0.0684` overall, beats Vector/Shift-Aware Platt in 8/8 cells. Target-only alpha=0.20 alarms are ANTI-conservative on corrupted MVTec (FAR up to 0.46) unlike VisA — this asymmetry is in the paper and motivates SC3R.
3. **Attainable-alpha analysis** (`scripts/analyze_attainable_alpha.py`): k-shot LOIO p-values cannot alarm below 1/(k+1); this is now a paper section + table.
4. **Float32 p-value bug fixed**: stored p-values (float32) exceed exact rationals, so `p <= alpha` at the floor silently dropped all alarms; all false-alarm analyses re-run with 1e-6 tolerance. Old k=4 alpha=0.20 rows reporting 0/0 were artifacts.
5. **Official AnomalyDINO MVTec k1/k4/k8 x 3 seeds complete** (plotting bug patched): AUROC `0.9652/0.9756/0.9803`. In `tab_clean_efficiency` as separate official rows.
6. **Paper V2 compiles** with `tectonic` (installed in the `ad` conda env): `cd paper && tectonic main.tex`. New tables via `scripts/build_paper_v2_tables.py --mvtec-full-tag mvtec_full15 --sc3r-detailed source_validated_threshold_sc3r_mvtec_full15_stratified_detailed.csv`.
7. Tests: `PYTHON_BIN=/home/crl/miniconda3/envs/ad/bin/python bash scripts/run_tests.sh` — 50 passed. (System python lacks pandas; always set PYTHON_BIN.)
8. Gotcha: `export_sw_cad_image_views.py` silently falls back to REPRESENTATIVE classes if `--classes` is omitted — always pass the explicit class list.

Remaining before submission: SC3R k=8/more seeds, cross-dataset source archives, figures for MVTec full15 reliability, advisor review of V2 claims. Sections below describe the pre-07-12 state; where they conflict with this snapshot, the snapshot wins.

## 1. Research Goal

The project aims to build a paper-grade few-shot industrial anomaly detection benchmark and method around frozen DINOv2 features.

Original idea:

- Use frozen DINOv2 ViT-S/14 patch features.
- Replace memory-heavy nearest-neighbor memory banks with a smaller trainable head/subspace method.
- Add calibration, uncertainty, corruption/adversarial robustness evaluation.
- Compare against PatchCore, AnomalyDINO, SubspaceAD.
- Target: Q1-level paper if novelty and evidence are strong enough.

The goal has evolved after many experiments and novelty checks. The current strongest direction is not pure AUROC SOTA. It is:

> A low-storage decoupled calibrated DINOv2 subspace detector with shift-aware/gated reliability diagnostics, evaluated under few-shot, transfer, corruption, and conformal-style false-alarm control protocols.

## 2. Current Main Claim Framing

The current defensible paper framing is:

1. **Low-storage decoupled calibrated subspace detector**
   - Use frozen DINOv2 patch features.
   - Use PCA/subspace residual as the ranking anomaly score.
   - Use a small head/calibrator only for probability and uncertainty, not for replacing ranking.
   - This is much lower-storage than memory-bank methods.

2. **Calibration and reliability under shift**
   - Vector Platt / decoupled calibration improves probability reliability compared with scalar/raw calibration, especially as k increases.
   - Shift-aware and gated calibration help on VisA, transfer, and structured corruptions.
   - The claim must be careful: it is not universal robustness.

3. **Transfer and robustness diagnostics**
   - MVTec-to-VisA transfer calibration shows calibration under dataset shift is hard but measurable.
   - Entropy, expert disagreement, conformal p-values, and source-conditioned thresholding provide useful reliability diagnostics.

4. **Conformal/SW-CAD-inspired diagnostic layer**
   - Conformal p-values are useful as false-alarm / reliability diagnostics.
   - Do not present `1 - p-value` as a calibrated posterior probability.
   - Main conformal metrics should be false alarm rate, power, attainable alpha, precision, p-value histogram, and risk-coverage.

5. **Candidate stronger novelty: SC3R**
   - Working name: **Support-Conditioned Cross-Category Reliability Routing (SC3R)**.
   - Idea: calibrate/threshold target support residuals using source-class normal support statistics and matched corruption/source conditions.
   - This may become a stronger Q1 contribution only if stratified representative experiments show good no-harm behavior and controlled false alarm rates.

## 3. Claims To Avoid

Do not write or imply these unless new evidence changes them:

- Do not claim **SOTA on MVTec AUROC**.
- Do not claim **adversarial robustness**.
- Do not claim **first DINOv2 + PCA/subspace residual**.
- Do not claim **first DINOv2 few-shot memory-bank anomaly detector**.
- Do not claim **first calibration/adversarial benchmark for DINOv2 few-shot AD**.
- Do not claim **first conformal anomaly detection**.
- Do not claim local `AnomalyDINO` baseline is official unless using the code under `third_party/AnomalyDINO`.
- Do not treat ECE on `1 - conformal p-value` as posterior calibration; it is prevalence-sensitive and should be secondary.

## 4. Prior Work / Novelty Collision Audit

Important novelty checks already performed:

- **AnomalyDINO** (`arXiv:2405.14529`)
  - DINOv2 + patch similarity + memory bank.
  - Training-free few-shot anomaly detection.
  - Therefore, DINOv2 memory-bank few-shot AD is not novel.

- **SubspaceAD** (`arXiv:2602.23013`)
  - Frozen DINOv2 + PCA/subspace residual.
  - Training-free, non-memory-bank style.
  - Official representative results are very strong.
  - Therefore, DINOv2 + PCA residual alone is not novel.

- **Khan & Krawczyk 2025** (`arXiv:2510.13643`)
  - Calibration, ECE, Platt scaling, FGSM robustness for DINOv2-based few-shot anomaly detection.
  - Therefore, calibration or FGSM benchmarking alone is not novel.

- **Conformal anomaly detection prior**
  - Leave-one-out/bootstrap/cross-conformal AD: `arXiv:2402.16388`.
  - Weighted conformal low-data/resolution/effective sample size: `arXiv:2603.23205`.
  - Nonconform CAD toolkit: `arXiv:2605.13642`.
  - Few-shot conformal auxiliary tasks: `arXiv:2102.08898`.
  - Industrial-image VAE+CAD exists in ECNDT 2026.
  - Therefore, conformal AD, LOIO, cross-conformal, and weighted conformal are not first-of-kind claims.

The novelty must be positioned as the combination of low-storage decoupled calibration, shift-aware/gated reliability routing, and unified empirical evidence in few-shot industrial AD.

## 5. Important Experimental Results So Far

### MVTec / VisA Clean And Efficiency

- `calib_subspace_head` is competitive but does not beat PatchCore/AnomalyDINO/SubspaceAD on all MVTec classes.
- On VisA, `calib_subspace_head` performs better than the controlled local PatchCore/AnomalyDINO baseline in the current benchmark.
- Storage is a strong point:
  - `calib_subspace_head` around `0.472 MB` in prior summaries.
  - Memory-bank baselines around `2-6 MB` depending on support/cache.
- Cached-feature latency is very low, around `0.0013s/image` in earlier audit. End-to-end no-cache latency should be reported separately.

### Calibration

- Vector Platt over `[subspace_score, head_score, disagreement]` improves calibration over scalar Platt in several settings.
- Example prior result:
  - Vector Platt ECE around `0.154` at k=8.
  - Scalar Platt ECE around `0.310` at k=8.
- Calibration gains are more defensible than AUROC gains.

### Transfer Calibration

- MVTec-to-VisA transfer calibration ablation completed `720/720` runs.
- MVTec-transfer calibrator to VisA:
  - AUROC k1 to k8 approximately `0.823 -> 0.882`.
  - ECE improves as k increases: around `0.432 -> 0.232`.
- VisA normal-synthetic target calibration:
  - ECE around `0.429 -> 0.207`.
- Upper-bound anomaly-val calibration improves ECE at k1 (`~0.379`) but does not improve AUROC.
- Takeaway: transfer calibration is hard in low-shot, but normal-synthetic target calibration becomes better with more support.

### Official SubspaceAD Representative

Official representative comparison is strong:

- k1 image AUROC `0.9518`, pixel AUROC `0.9710`.
- k4 image AUROC `0.9625`, pixel AUROC `0.9737`.
- k8 image AUROC `0.9639`, pixel AUROC `0.9743`.

This means we should not claim DINOv2+PCA/subspace novelty or AUROC superiority over SubspaceAD unless a new method beats it under the same protocol.

### Official AnomalyDINO

Official AnomalyDINO code was downloaded to:

- `third_party/AnomalyDINO`

`faiss-cpu 1.14.3` was installed in the `ad` conda environment.

Completed official AnomalyDINO MVTec k1 seed0:

- Metrics file:
  - `third_party/AnomalyDINO/results_MVTec/dinov2_vits14_448/1-shot_preprocess=agnostic/metrics_seed=0.json`
- Mean image AUROC: `0.9701926131`.
- Mean AP: `0.9848747966`.
- Mean F1: `0.9621457314`.

The run exited with code 1 only after metric computation due to sample plotting `FileNotFoundError`. Metrics are valid, but plotting should be disabled/patched before k4/k8.

### FGSM / Adversarial

- FGSM causes large AUROC drops.
- Do not claim adversarial robustness.
- Use as diagnostic/failure-case evidence.
- Note caveat: some FGSM results were non-monotonic and should be reported as surrogate/diagnostic unless fully audited.

### Conformal / SW-CAD

Matched LOIO k4 representative MVTec, older sampling:

- Clean FAR matched `.2458` vs legacy `.1695`; power `.9056` vs `.8944`.
- Blur FAR `.2458` vs `.1723`; power `.9019` vs `.8926`.
- Brightness FAR `.2571` vs `.1751`; power `.9074` vs `.9037`.
- Gaussian FAR `.3701` vs `.3249`; power `.9130` vs `.9167`.
- JPEG FAR `.3842` vs `.3333`; power `.9148` vs `.9093`.

Conclusion: matched LOIO did not clearly improve false-alarm control. Do not promote as main method yet.

Prevalence stress:

- Full VisA LOIO ECE changes from `.403877` at 1% prevalence to `.149337` at 50%.
- Weighted conformal changes from `.265531` to `.210201`.
- Representative MVTec LOIO `.490352 -> .219531`; weighted `.202578 -> .254787`.

Takeaway: ECE on conformal-derived scores is highly prevalence-dependent. Use operational metrics instead.

### Source-Conditioned / SC3R Pilot

Old sampling pilot:

- MVTec k4 alpha `.1`, source_pool FAR `.049-.068`, power `.108-.111`.
- Target-only alpha `.1` produced `0/0` due p-value minimum issue.
- Full VisA k8 alpha `.1`, source_pool FAR `.0478`, power `.2299`, precision `.8304`.

Support-normalized residual pooling old sampling:

- AUROC around `.88` vs target p around `.79`.
- Direct source-pool FAR too high.

Source-class-validated threshold old sampling:

- Matched-condition k4:
  - alpha `.05`: FAR `.0444`, power `.1196`.
  - alpha `.10`: FAR `.0759`, power `.3067`.
- Clean-source:
  - alpha `.05`: FAR `.0444`, power `.1259`.
  - alpha `.10`: FAR `.1531`, power `.4963`.

Interpretation:

- Structured clean/blur/brightness shift signal is promising.
- Gaussian/JPEG violate FAR more often.
- Not yet universal.

## 6. Current Blocker / Last Runtime State

The environment recently blocked experiment execution with:

```text
bwrap: loopback: Failed RTM_NEWADDR: Operation not permitted
```

This is a sandbox/environment issue, not a research-code conclusion.

The goal was marked blocked after repeated failures. If a new session has a working executor, resume from the SC3R stratified experiment.

Current partially written SC3R stratified files:

- `outputs/paper_tables/sc3r_views_mvtec_repr_stratified.csv`
- `outputs/paper_tables/sc3r_support_mvtec_repr_stratified.csv`

The job had completed some bottle cases and started cable seed 0 before stopping.

Resume command:

```bash
PYTHONUNBUFFERED=1 /home/crl/miniconda3/envs/ad/bin/python -u scripts/export_sc3r_views.py \
  --dataset mvtec --classes bottle cable hazelnut \
  --k-shots 4 --seeds 0 1 2 \
  --corruptions clean gaussian_noise blur brightness_contrast jpeg \
  --max-images 120 \
  --out outputs/paper_tables/sc3r_views_mvtec_repr_stratified.csv \
  --support-out outputs/paper_tables/sc3r_support_mvtec_repr_stratified.csv \
  --resume
```

Then evaluate:

```bash
/home/crl/miniconda3/envs/ad/bin/python -u scripts/evaluate_source_validated_threshold.py \
  --inputs outputs/paper_tables/sc3r_views_mvtec_repr_stratified.csv \
  --support-stats outputs/paper_tables/sc3r_support_mvtec_repr_stratified.csv \
  --source-modes matched_condition clean_source \
  --alphas 0.05 0.10 0.20 \
  --run-tag mvtec_k4_stratified
```

Decision criteria for SC3R:

- nonzero power at alpha `.05` / `.10`;
- FAR <= alpha + `.02` on average;
- no target anomaly labels for tuning;
- no-harm >= `80%`;
- hierarchical class-seed confidence interval supports the gain.

If these pass, SC3R can be promoted to a main contribution. If not, keep it as diagnostic/failure analysis.

## 7. Important Code Files

Core method/model code:

- `src/models/baselines.py`
  - Local `AnomalyDINO(PatchCoreNN)` currently does not override scoring.
  - Therefore local PatchCore and local AnomalyDINO are identical controlled DINOv2 nearest-neighbor baselines.
  - Rename/report as controlled DINOv2 NN unless using official third-party AnomalyDINO.

- `src/conformal.py`
  - Contains conformal utilities including `MatchedLOIOResult` and `matched_loio_image_p_values`.

Main experiment/evaluation scripts:

- `scripts/export_sc3r_views.py`
  - Efficient SC3R exporter.
  - Fits support PCA once per class/k/seed.
  - Supports LOIO support stats, stratified sampling, incremental CSV/resume.

- `scripts/evaluate_source_validated_threshold.py`
  - Evaluates source-class validated thresholding for SC3R-style reliability.

- `scripts/evaluate_source_conditioned_routing.py`
  - Evaluates source-conditioned routing variants.

- `scripts/export_support_calibration_stats.py`
  - Exports support calibration statistics.

- `scripts/export_matched_loio_views.py`
  - Exports matched LOIO views.

- `scripts/evaluate_prevalence_stress.py`
  - Shows prevalence sensitivity of ECE-like metrics on conformal-derived scores.

- `scripts/evaluate_validation_ece_gate.py`
  - Validation-class ECE gate.

- `scripts/evaluate_selective_reliability.py`
  - Risk-coverage / selective reliability.

- `scripts/export_sw_cad_image_views.py`
  - SW-CAD-inspired per-image conformal views.

- `scripts/hierarchical_bootstrap_comparison.py`
  - Paired hierarchical class-seed bootstrap.

- `scripts/evaluate_corruptions.py`
  - Corruption benchmark.
  - Was updated to deterministic label-stratified random sampling instead of first sorted images.

## 8. Important Output Artifacts

Paper tables and summaries live mostly in:

- `outputs/paper_tables/`

High-value files:

- `outputs/paper_tables/final_claim_evidence.md`
- `outputs/paper_tables/paper_ready_tables.md` if present
- `outputs/paper_tables/mvtec_full_clean_summary.csv`
- `outputs/paper_tables/visa_full_clean_summary.csv`
- `outputs/paper_tables/transfer_calibration_ablation_summary.csv`
- `outputs/paper_tables/calibration_ablation_summary.csv`
- `outputs/paper_tables/pixel_metrics_summary.csv` if present
- `outputs/paper_tables/mvtec_fgsm_sweep_summary.csv`
- `outputs/paper_tables/visa_full_conformal_main_table.md`
- `outputs/paper_tables/visa_full_conformal_extended_summary.csv`
- `outputs/paper_tables/sw_cad_visa_full_k4k8_s0s4_conformal_summary.csv`
- `outputs/paper_tables/validation_ece_gate_representative_conformal_full_summary.csv`
- `outputs/paper_tables/selective_reliability_representative_conformal_full.csv`
- `outputs/paper_tables/gated_shift_aware_summary.csv`
- `outputs/paper_tables/gated_shift_aware_delta.csv`
- `outputs/paper_tables/gated_shift_aware_oracle_gap.csv`
- `outputs/paper_tables/sc3r_mvtec_k4_hierarchical_ci.csv`
- `outputs/paper_tables/source_validated_threshold_mvtec_k4_support_normalized_summary.csv`
- `outputs/paper_tables/source_conditioned_routing_mvtec_k4_support_normalized_summary.csv`
- `outputs/paper_tables/sc3r_views_mvtec_repr_stratified.csv`
- `outputs/paper_tables/sc3r_support_mvtec_repr_stratified.csv`

Official baseline:

- `third_party/AnomalyDINO/results_MVTec/dinov2_vits14_448/1-shot_preprocess=agnostic/metrics_seed=0.json`

## 9. Important Docs

Main docs:

- `docs/research_log.md`
  - Timeline of findings and decisions.

- `docs/experiment_findings.md`
  - Experiment findings and caveats.

- `docs/paper_claims_current.md`
  - Current paper claims.

- `docs/current_claims_synthesis_v3.md`
  - Vietnamese synthesis of current claim direction.

- `docs/novelty_claims.md`
  - Short novelty/claim notes.

- `docs/novelty_claims_explained.md`
  - Longer onboarding explanation.

- `docs/novelty_claim_explained_2.md`
  - Updated post-P0/P1 status.

- `docs/q1_claim_and_protocol_audit_2026_07_11.md`
  - Important audit document for Q1 readiness and protocol issues.

- `docs/setup_issues.md`
  - Should be updated with faiss install and official AnomalyDINO plotting failure.

- `docs/sw_cad_experiment_plan.md`
- `docs/gated_shift_aware_plan.md`
- `docs/sw_cad_and_gated_results.md`

This handoff file should be kept updated whenever major claims or decisions change.

## 10. Paper Files

Paper workspace:

- `paper/`

Important files likely include:

- `paper/main.tex`
- `paper/sections/abstract.tex`
- `paper/sections/introduction.tex`
- `paper/sections/related_work.tex`
- `paper/sections/method.tex`
- `paper/sections/experiments.tex`
- `paper/sections/results.tex`
- `paper/sections/conclusion.tex`
- `paper/tables/`
- `paper/references.bib`

Known paper issues to fix:

- Some V1 text overstates ECE and conformal reliability.
- ECE should be framed as secondary and prevalence-sensitive for conformal-derived scores.
- CRR/SC3R should not be main-claimed until stratified audit passes.
- Related work should explicitly cite conformal AD prior.
- Official AnomalyDINO k1 result should be added and local controlled-NN rows should not be mislabeled.
- Tables need bold/highlight for best or claim-relevant numbers.
- Some tables had missing numbers in earlier draft; audit before sending to advisor.
- References were previously too few; need more than 6 references for a serious submission.

Bibliography entries that still need to be added if not already present:

- Hennhoefer & Preisach 2024, "Leave-One-Out-, Bootstrap- and Cross-Conformal Anomaly Detectors", ICKG.
- Hennhoefer & Preisach 2026, weighted conformal low-data/resolution/effective sample size, `arXiv:2603.23205`.
- Hennhoefer, Kirsch, Preisach 2026, nonconform CAD toolkit, `arXiv:2605.13642`.
- Fisch et al. ICML 2021, few-shot conformal auxiliary tasks, `arXiv:2102.08898`.
- AnomalyDINO, `arXiv:2405.14529`.
- SubspaceAD, `arXiv:2602.23013`.
- Khan & Krawczyk 2025, `arXiv:2510.13643`.
- DINOv2, PatchCore, MVTec AD, VisA, Platt scaling, conformal prediction foundations.

## 11. Test Status

Recent full test suite passed:

- `47 passed, 3 warnings`

Important test files:

- `tests/test_prevalence_stress.py`
- `tests/test_source_conditioned_routing.py`
- `tests/test_corruption_sampling.py`
- `tests/test_hierarchical_bootstrap_comparison.py`
- `tests/test_source_validated_threshold.py`
- `tests/test_conformal_and_gated.py`

After code edits, run:

```bash
bash scripts/run_tests.sh
```

## 12. Recommended Next Steps For New Session

Priority 1: Resume and finish SC3R stratified audit.

1. Run `scripts/export_sc3r_views.py` with `--resume`.
2. Run `scripts/evaluate_source_validated_threshold.py`.
3. Summarize FAR/power by alpha, corruption, class, seed.
4. Run hierarchical bootstrap if SC3R looks promising.
5. Decide whether SC3R is a main contribution or diagnostic-only.

Priority 2: Clean official baseline positioning.

1. Patch official AnomalyDINO plotting issue or disable plotting.
2. Run official AnomalyDINO k4/k8 representative or full if feasible.
3. Add official baseline table separately from controlled local NN.
4. Update `docs/setup_issues.md`.

Priority 3: Paper V2.

1. Rewrite contributions around defensible claims only.
2. Add prior work citations for conformal and DINOv2 baselines.
3. Add paper-ready tables with bold/highlight.
4. Add prevalence-stress warning for ECE.
5. Add limitations: no MVTec AUROC SOTA, no adversarial robustness, SC3R status if not fully validated.
6. Compile IEEE PDF and inspect formatting.

## 13. Suggested Final Contribution Set If SC3R Passes

If SC3R stratified audit passes:

1. **Decoupled low-storage DINOv2 subspace detector**
   - PCA residual for ranking, vector/gated calibrator for probability and uncertainty.

2. **Shift-aware/gated reliability calibration**
   - Gated routing improves or protects calibration under selected transfer/structured shifts.
   - Inspired by SAGE-style routing but adapted to industrial AD reliability.

3. **Support-conditioned cross-category reliability routing**
   - Uses source-class/support statistics to set reliability thresholds without target anomaly labels.
   - Reports operational FAR/power and no-harm behavior under corruption.

4. **Unified reliability benchmark**
   - Clean, calibration, transfer, corruption, FGSM diagnostic, conformal false-alarm control, risk-coverage.

If SC3R does not pass:

1. Keep method contribution as low-storage decoupled calibrated subspace detector.
2. Keep gated shift-aware calibration as selected-shift reliability improvement.
3. Use conformal/SC3R as diagnostic analysis and limitation.
4. Aim for a more moderate Q1/Q2 venue unless additional novelty is added.

## 14. One-Sentence Project Summary

This paper should be positioned as a reliability-first few-shot industrial anomaly detection study: it does not claim to beat every memory-bank/subspace method on AUROC, but it offers a low-storage decoupled DINOv2 detector and a careful calibration/shift/conformal diagnostic framework that exposes when few-shot AD scores can and cannot be trusted.

