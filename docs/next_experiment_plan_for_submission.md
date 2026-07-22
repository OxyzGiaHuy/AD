# Next Experiment Plan For Strengthening CRR Paper

Date: 2026-07-10

## Goal

Strengthen the current paper from an advisor-ready V1 into a more submission-ready Q1 story.

Current main claim:

> Conformal Reliability Routing (CRR) is a low-storage DINOv2 subspace detector that preserves PCA/subspace residual ranking while adding LOIO conformal reliability, substantially improving calibration under VisA corruption shift.

The next experiments should answer three reviewer-facing questions:

1. Does the conformal reliability result hold beyond VisA, especially on MVTec?
2. Does conformal reliability provide statistically useful false-alarm control, not just lower ECE?
3. Can SAGE-inspired/gated routing become a stronger method claim, or should it remain diagnostic?

---

## P0: Sanity And Rebuild Current Paper Artifacts

### Purpose

Make sure the current codebase and paper tables are internally consistent before launching expensive jobs.

### Commands

```bash
bash scripts/run_tests.sh
python scripts/build_paper_ready_tables.py --tables-dir outputs/paper_tables --out outputs/paper_tables/paper_ready_tables.md
python scripts/analyze_visa_full_conformal.py
```

### Expected Outputs

- `outputs/paper_tables/paper_ready_tables.md`
- Existing VisA conformal tables remain reproducible.
- No regressions in unit/smoke tests.

### Acceptance Criteria

- Tests pass or only known skipped tests remain.
- Paper table values still match `paper/tables/*.tex`.

---

## P1: Full MVTec Conformal Reliability

### Purpose

This is the most important missing experiment. Current full conformal evidence is VisA-heavy. A reviewer will ask whether LOIO conformal reliability also works on MVTec.

### Protocol

Dataset:

- MVTec AD, 15 classes.

Few-shot:

- Main: `k={4,8}`, seeds `{0,1,2,3,4}`.
- Optional if compute allows: `k=2` for low-shot stress.

Corruptions:

- `gaussian_noise`
- `blur`
- `brightness_contrast`
- `jpeg`

Evaluation cap:

- `--max-images 120` to match VisA full protocol and keep runtime manageable.

### Commands

```bash
python scripts/export_sw_cad_image_views.py \
  --dataset mvtec \
  --k-shots 4 8 \
  --seeds 0 1 2 3 4 \
  --corruptions gaussian_noise blur brightness_contrast jpeg \
  --max-images 120 \
  --tmp-root /home/crl/AD/tmp \
  --out-dir outputs/paper_tables \
  --run-tag mvtec_full_k4k8_s0s4 \
  --resume
```

After export, create or extend an analyzer analogous to the VisA one:

```bash
python scripts/analyze_mvtec_full_conformal.py \
  --input outputs/paper_tables/sw_cad_image_views_mvtec_full_k4k8_s0s4.csv \
  --out-dir outputs/paper_tables
```

If `analyze_mvtec_full_conformal.py` does not exist yet, implement it by adapting `scripts/analyze_visa_full_conformal.py`.

### Expected Outputs

- `outputs/paper_tables/sw_cad_image_views_mvtec_full_k4k8_s0s4.csv`
- `outputs/paper_tables/mvtec_full_conformal_extended_summary.csv`
- `outputs/paper_tables/mvtec_full_conformal_vs_baselines_k_corruption.csv`
- `outputs/paper_tables/mvtec_full_conformal_reliability_bins.csv`
- `outputs/figures/mvtec_full_loio_reliability_all.png`
- `outputs/figures/mvtec_full_ece_by_corruption_k4.png`
- `outputs/figures/mvtec_full_ece_by_corruption_k8.png`

### Claim Decision

If LOIO conformal improves ECE over Vector/Shift-Aware Platt on most MVTec cells:

> CRR improves reliability across both VisA and MVTec corruption shifts.

If MVTec is mixed:

> CRR is strongly supported on VisA and provides a diagnostic conformal reliability layer on MVTec; full MVTec reveals dataset-specific limitations.

### Acceptance Criteria

- At least 80% of MVTec k/corruption cells improve ECE over Vector Platt.
- AUROC/AP remain unchanged when only reliability view changes.
- No test anomaly labels are used to select the main reliability view.

---

## P2: False-Alarm Control From Conformal P-Values

### Purpose

ECE is useful but generic. Conformal p-values become much more compelling if we show false-alarm control on normal samples.

### Protocol

Use full VisA conformal rows first, then MVTec when P1 finishes.

Thresholds:

- `alpha={0.01,0.05,0.10,0.20}`.

Metrics:

- empirical false-alarm rate on normal images;
- coverage gap: empirical false alarm minus nominal alpha;
- anomaly detection rate at the same threshold;
- per-class and per-corruption false-alarm distribution;
- p-value histogram for normal images.

### Implementation

Create script:

```bash
scripts/evaluate_conformal_false_alarm.py
```

Input columns expected:

- `dataset`
- `class`
- `k_shot`
- `seed`
- `corruption`
- `label`
- `image_p_loio` or `conformal_prob_loio`
- optional `image_p_weighted`

Command:

```bash
python scripts/evaluate_conformal_false_alarm.py \
  --input outputs/paper_tables/sw_cad_image_views_visa_full_k4k8_s0s4_combined.csv \
  --dataset visa \
  --alphas 0.01 0.05 0.10 0.20 \
  --out-dir outputs/paper_tables \
  --run-tag visa_full
```

After MVTec:

```bash
python scripts/evaluate_conformal_false_alarm.py \
  --input outputs/paper_tables/sw_cad_image_views_mvtec_full_k4k8_s0s4.csv \
  --dataset mvtec \
  --alphas 0.01 0.05 0.10 0.20 \
  --out-dir outputs/paper_tables \
  --run-tag mvtec_full
```

### Expected Outputs

- `outputs/paper_tables/visa_full_conformal_false_alarm_summary.csv`
- `outputs/paper_tables/visa_full_conformal_false_alarm_by_corruption.csv`
- `outputs/paper_tables/visa_full_conformal_pvalue_histogram.csv`
- Same files for MVTec after P1.

### Claim Decision

If empirical false-alarm rate is close to nominal alpha:

> CRR provides interpretable false-alarm diagnostics, not only lower calibration error.

If false-alarm rate is conservative or anti-conservative:

> CRR exposes when support normals are not exchangeable with shifted test normals; this becomes a useful limitation/diagnostic result.

### Acceptance Criteria

- Table includes normal false-alarm rate by alpha, k, and corruption.
- Report anomaly detection rate at the same thresholds.
- No claim of guaranteed conformal coverage under corruption unless empirical evidence supports it.

---

## P3: Strengthen SAGE-Inspired No-Label Routing

### Purpose

Right now, gated/SAGE-inspired routing is mostly diagnostic because fixed LOIO is strongest. To make it a method contribution, we need a no-label gate that either improves reliability or safely avoids over-adaptation.

### Input

Use prediction tables with conformal views:

- `outputs/paper_tables/sage_sample_gate_representative_with_conformal_full.csv`
- Full VisA conformal table if compatible.
- Full MVTec conformal table after P1.

### Gate Variants

1. `fixed_loio`: safe anchor.
2. `vector_platt`: calibration baseline.
3. `shift_aware_vector_platt`: structured shift expert.
4. `weighted_conformal`: density-ratio/conformal expert.
5. `no_label_shift_neff_gate`: rule gate using shift descriptor and effective sample size.
6. `safe_anchor_gate`: only switch away from LOIO when confidence/shift rule is satisfied.

### Commands

Representative rerun:

```bash
python scripts/evaluate_validation_ece_gate.py \
  --predictions outputs/paper_tables/sage_sample_gate_representative_with_conformal_full.csv \
  --out-dir outputs/paper_tables \
  --run-tag representative_crr_gate \
  --experts vector_platt shift_aware_vector_platt conformal_prob_loio conformal_prob_weighted \
  --margin 0.01 \
  --grid-step 0.05
```

Selective reliability:

```bash
python scripts/evaluate_selective_reliability.py \
  --predictions outputs/paper_tables/sage_sample_gate_representative_with_conformal_full.csv \
  --out-dir outputs/paper_tables \
  --run-tag representative_crr_gate \
  --prob-cols vector_platt shift_aware_vector_platt conformal_prob_loio conformal_prob_weighted \
  --coverages 1.0 0.95 0.9 0.8 0.7
```

If full VisA/MVTec merged predictions exist, repeat with full tables.

### Expected Outputs

- `outputs/paper_tables/validation_ece_gate_representative_crr_gate_summary.csv`
- `outputs/paper_tables/selective_reliability_representative_crr_gate.csv`
- `outputs/paper_tables/risk_coverage_curves_representative_crr_gate.csv`

### Claim Decision

If no-label gate improves mean/worst ECE without hurting many cells:

> SAGE-inspired reliability routing safely selects between conservative conformal and shift-specialized calibration experts.

If not:

> Gated routing is kept as diagnostic analysis; fixed LOIO remains the main route.

### Acceptance Criteria

- Mean ECE improves over fixed LOIO or worst-case ECE improves meaningfully.
- No-harm rate vs fixed LOIO >= 80%.
- Gate does not use target anomaly labels in main protocol.

---

## P4: Full Official Baseline Alignment

### Purpose

Reduce reviewer concern that our baselines are local approximations.

### Minimum Scope

- Official SubspaceAD representative already exists.
- Extend official SubspaceAD to k `{4,8}` on representative classes: `bottle`, `cable`, `hazelnut`.
- If feasible, run additional object/texture classes.

### Expected Output

- `outputs/paper_tables/official_subspacead_representative_k_trend.csv`
- Add/update paper caveat table.

### Claim Decision

This will likely not strengthen AUROC claim, but it strengthens honesty and novelty positioning.

---

## P5: Paper Update After Experiments

After P1-P3:

1. Update `paper/tables/`:
   - add MVTec conformal table;
   - add false-alarm control table;
   - update routing table.
2. Update `paper/sections/results.tex`:
   - add subsection `False-Alarm Control`;
   - revise SAGE-inspired routing claim based on P3.
3. Update docs:
   - `docs/paper_v1_quality_review.md`;
   - `docs/research_log.md`;
   - `docs/experiment_findings.md`;
   - `docs/paper_claims_current.md`.

---

## Recommended Execution Order

1. Run P0 sanity.
2. Implement `evaluate_conformal_false_alarm.py` because it is fast and gives a new paper table immediately from existing VisA data.
3. Run P2 on existing VisA full conformal output.
4. Launch P1 full MVTec conformal export as a background job.
5. While P1 runs, run P3 representative routing/selective experiments.
6. After P1 finishes, run MVTec analyzer + false-alarm control.
7. Update paper tables and claims.

---

## Highest-Value Claims If Everything Works

Strong claim:

> CRR provides low-storage anomaly ranking with conformal reliability that improves calibration and yields interpretable false-alarm diagnostics under industrial corruption shifts.

Secondary claim:

> SAGE-inspired routing is useful as a safety mechanism for avoiding over-adaptation, but fixed LOIO conformal remains the strongest current default route unless full no-label gating improves.

Limitations to preserve:

- No MVTec AUROC SOTA claim.
- No adversarial robustness claim.
- No first conformal AD claim.
- No first DINOv2 subspace claim.
# Historical experiment plan — superseded

Do not execute this file as the final protocol. The frozen GPU/CPU boundary,
commands, negative-result rules, and acceptance gates are in
`gpu_experiment_runbook.md`.
