# 2026-07-11 Audit: claim đang được nâng cấp

Claim CRR dựa chủ yếu trên ECE cần hạ thành evidence phụ vì 1-p là anomaly extremeness, không mặc nhiên là posterior probability, và ECE thay đổi mạnh theo anomaly prevalence. Main operational evidence phải chuyển sang false-alarm, power và risk-coverage.

Candidate contribution mới là Support-Conditioned Cross-Category Reliability Routing (SC3R). Pilot source-class-validated threshold trên MVTec representative k4 đạt mean FAR/power 0.044/0.120 tại alpha 0.05 và 0.076/0.307 tại alpha 0.10 trong matched-condition mode, không dùng target anomaly label. Kết quả chưa universal: Gaussian noise và JPEG còn vi phạm FAR theo cell. Chỉ nâng SC3R thành main claim sau stratified rerun, class-held-out/full-grid evaluation, hierarchical CI và no-harm gate.

Local PatchCore/AnomalyDINO rows không phải official reproductions; chúng phải được gọi là Controlled DINOv2 nearest-neighbor memory-bank baseline.

# Current Paper Claims For Q1 Draft

This note is the short claim tracker after P0, P1 core, and the extended transfer calibration ablation completed.

## Main Framing

Main framing: **Calibration + Efficiency + Transfer/Robustness Diagnostics**.

Recommended main claim:

> A decoupled calibrated subspace head provides competitive few-shot anomaly detection with much lower storage than memory-bank methods, improves probability calibration as support grows, and exposes transfer/robustness failure modes under a unified benchmark.

## Defensible Claims

| Claim | Evidence | Caveat |
| --- | --- | --- |
| Competitive low-storage MVTec detector | MVTec AUROC k1/k4/k8: `0.9038/0.9371/0.9452`; storage about `0.472 MB` vs PatchCore/AnomalyDINO `2-6 MB`. | Does not beat PatchCore/AnomalyDINO on all MVTec k. |
| Strong VisA clean result in this benchmark | VisA AUROC k1/k4/k8: `0.8226/0.8696/0.8796`, above PatchCore/AnomalyDINO in current tables. | Phrase as benchmark-specific, not universal SOTA. |
| Vector/decoupled calibration helps reliability | MVTec vector Platt ECE improves to `0.1538` at k8, better than scalar Platt k8 `0.3097`. | Calibration remains imperfect at low-shot. |
| Transfer calibration is measurable and difficult | MVTec-transfer to VisA AUROC k1->k8: `0.8226 -> 0.8824`; ECE `0.4319 -> 0.2324`. | Target VisA normal-synthetic calibration is better at k8 ECE `0.2066`; upper-bound anomaly-val is best at k1 ECE `0.3787`. |
| Pixel ranking is strong | MVTec pixel AUROC for `calib_subspace_head`: k1 `0.9436`, k8 `0.9599`, higher than memory-bank rows in current table. | Pixel AP is not uniformly better; report both AUROC and PRO/AP. |
| Robustness diagnostic, not robustness solution | FGSM sweep and audit show severe collapse and objective sensitivity. | Report as `label-aware PCA-residual FGSM surrogate`; do not claim adversarial robustness. |

## Required Prior-Work Positioning

| Prior work | What it already covers | What we must not claim |
| --- | --- | --- |
| AnomalyDINO | Frozen DINOv2 few-shot AD with patch similarity/memory bank. | DINOv2 few-shot memory bank novelty. |
| SubspaceAD | Frozen DINOv2 + PCA/subspace residual, training-free. Official representative run is strong: avg image AUROC `0.9518`, pixel AUROC `0.9710` on bottle/cable/hazelnut k1. | DINOv2 PCA/subspace residual novelty or raw subspace SOTA. |
| Khan & Krawczyk 2025 | Calibration/ECE/Platt scaling and FGSM fragility for DINOv2-based few-shot AD. | First calibration benchmark, first FGSM benchmark, Platt scaling novelty. |

## Do Not Write

- Do not write `SOTA on MVTec`.
- Do not write `first calibration benchmark`.
- Do not write `adversarially robust`.
- Do not write `DINOv2 PCA residual is novel`.
- Do not keep `trainable adapter` as a main contribution unless LoRA/adapter experiments are actually completed.

## Next Highest-Value Work

1. Freeze paper tables and figures from existing artifacts.
2. Run official SubspaceAD representative k4/k8 only if compute is available.
3. Run VisA PCA128 representative to test whether accuracy-storage tradeoff transfers.
4. Run no-cache runtime audit on representative classes to separate cached-feature and end-to-end costs.


## P2 Official SubspaceAD k-Trend Update

- Representative official SubspaceAD, same lightweight protocol, average over `bottle/cable/hazelnut`:
  - k1 image AUROC / pixel AUROC / AU-PRO: `0.9518` / `0.9710` / `0.8685`.
  - k4 image AUROC / pixel AUROC / AU-PRO: `0.9625` / `0.9737` / `0.8844`.
  - k8 image AUROC / pixel AUROC / AU-PRO: `0.9639` / `0.9743` / `0.8908`.
- Claim impact: treat official SubspaceAD as a strong accuracy baseline. Our paper should compete on calibrated probabilities, storage/latency tradeoff, transfer calibration, and robustness diagnostics.


## P2 Priority Probe Update

- VisA PCA128 representative supports an accuracy-storage Pareto story: AUROC improves by `+0.0186` to `+0.0233` over PCA64 on the same representative subset, while storage remains below `0.6 MB`.
- Shift-Aware Calibration is the most promising new novelty direction: on VisA representative classes it reduces ECE from `0.3090 -> 0.2183` at k4 and `0.2152 -> 0.1148` at k8 without changing ranking.
- MVTec Shift-Aware results are mixed, so phrase the claim as calibration under dataset/shift conditions, not universal calibration dominance yet.
- No-cache runtime audit shows end-to-end setup cost is seconds per run, while cached-feature scoring remains millisecond-level. Keep both cost definitions separate in the paper.


## Full VisA Priority Update

The two priority directions requested for deeper testing are now complete.

| Finding | Evidence | Paper Use |
| --- | --- | --- |
| PCA128 improves the VisA accuracy-storage Pareto | Full VisA AUROC delta vs PCA64: k1 `+0.0110`, k2 `+0.0150`, k4 `+0.0156`, k8 `+0.0171`; storage `0.566 MB` vs `0.472 MB`. | Use as a low-storage accuracy tradeoff ablation. |
| Shift-Aware Calibration improves reliability at moderate/high k | Full VisA ECE vs vector Platt: k4 `0.2839 -> 0.2032`, k8 `0.2066 -> 0.1447`; AUROC unchanged by design. | Use as the cleanest new calibration mechanism claim. |
| k1 remains difficult | Full VisA k1 ECE slightly worsens under Shift-Aware: `0.4295 -> 0.4320`, though NLL improves `4.3117 -> 4.0028`. | State low-shot calibration caveat explicitly. |

Updated recommended claim:

> A low-storage calibrated subspace detector can trade a small PCA storage increase for consistent VisA AUROC gains, while a shift-aware vector calibrator substantially improves probability reliability at moderate/high shot without replacing subspace ranking.

This strengthens the Q1 story around calibration under dataset shift and accuracy-storage tradeoffs. It still does not justify claiming MVTec SOTA, adversarial robustness, or novelty of DINOv2 PCA/subspace residual itself.


## Full VisA Corruption Shift-Aware Update

The full VisA corruption calibration grid is complete: `960/960` rows over 12 classes, k `{4,8}`, 5 seeds, and corruptions `{gaussian_noise, blur, brightness_contrast, jpeg}`.

| Finding | Evidence | Paper Use |
| --- | --- | --- |
| Shift-Aware preserves ranking | AUROC/AP deltas are `0.0` for every corruption/k. | Emphasize decoupled ranking vs probability calibration. |
| Structured corruptions improve strongly | ECE improves for blur by `-0.0733/-0.0640` at k4/k8, brightness/contrast by `-0.0727/-0.0554`, JPEG by `-0.0579/-0.0554`. | Main evidence for calibration under structured corruption/domain shift. |
| Gaussian noise is not improved by ECE | Gaussian ECE worsens slightly: k4 `+0.0067`, k8 `+0.0013`; NLL still improves. | Important limitation; do not claim universal OOD calibration. |

Updated Shift-Aware claim:

> Shift-aware vector calibration improves probability reliability under structured corruption/domain shift such as blur, brightness/contrast, and JPEG compression while preserving PCA/subspace anomaly ranking; it is not a universal fix for additive Gaussian noise.

## 2026-07-09 Update: Conformal Reliability Routing Becomes Main Claim

Main paper framing should now prioritize **Calibration + Efficiency + Conformal Reliability Routing**.

Current strongest claim:

> A low-storage decoupled DINOv2 subspace detector can preserve PCA/subspace residual ranking while adding LOIO conformal p-value views as a reliability layer. On representative MVTec/VisA transfer and class-held-out protocols, fixed LOIO conformal reliability reduces ECE by about `0.19-0.21` absolute versus Vector Platt, with no observed harm in the reported split groups.

Evidence:

- `outputs/paper_tables/conformal_routing_protocols_full_summary.csv`
- `outputs/paper_tables/conformal_routing_claim_evidence.md`
- `docs/conformal_reliability_routing_claim.md`
- `docs/conformal_novelty_verification.md`

Important caveat:

- This is not a claim of first conformal AD or MVTec AUROC SOTA.
- Ranking remains PCA/subspace residual.
- SAGE is cited as routing inspiration, not as copied architecture.
- Full VisA scale-up is running and should become the next main-table check.

## 2026-07-10 Full VisA Conformal Evidence

Full VisA conformal benchmark is complete: `480/480` cases and `56,000` image rows.

Main result:

- LOIO conformal overall ECE: `0.0766`.
- k=4 ECE: `0.0391`.
- k=8 ECE: `0.1140`.
- Vector Platt ECE by k/corruption is around `0.190-0.288`; Shift-Aware Platt is around `0.144-0.276`; LOIO is lower in every tested k/corruption cell.

Updated claim strength:

- Stronger than representative-only evidence: full VisA now supports conformal reliability as a main contribution.
- Keep caveat: k=8 has higher ECE than k=4 because normal conformal probability increases too much.
- Weighted conformal is not main; it is an ablation with mixed behavior.

## 2026-07-11 P1/P2 False-Alarm Update

P1 has now completed the MVTec representative conformal false-alarm check on `bottle/cable/hazelnut`, k `{4,8}`, seeds `{0..4}`, and four corruptions. This is not a full 15-class MVTec result yet.

Updated claim status:

- Full VisA remains the strongest main evidence for CRR calibration: LOIO conformal ECE is `0.0766` overall and beats Vector/Shift-Aware Platt in every tested k/corruption cell.
- MVTec representative supports conformal p-values as an operating-point diagnostic: LOIO separates normal/anomaly p-values by `0.3185`; alpha `0.20` gives false-alarm `0.1057`, detection `0.4558`, precision `0.8680`; alpha `0.25` gives false-alarm `0.3337`, detection `0.9261`, precision `0.8089`.
- Weighted conformal is too conservative for the main detector but useful as a safe diagnostic mode: alpha `0.50` gives false-alarm `0.0464` and detection `0.1010`.

Paper-safe wording:

> CRR adds an interpretable conformal reliability layer to a low-storage DINOv2 subspace detector, providing calibrated probabilities and explicit false-alarm/detection operating tradeoffs under corruption shift.

Do not claim exact conformal false-alarm control under non-exchangeable corruption shift. The stronger next experiment is randomized/smoothed few-shot p-values or normal-only threshold selection.

## 2026-07-11 (evening) Update: SC3R Gate Passes (Scoped), Attainable Alpha, Float32 Fix

### SC3R promotion decision

The pre-registered stratified gate was evaluated on `sc3r_views_mvtec_repr_stratified.csv` (bottle/cable/hazelnut, k=4, seeds 0-2, 5 corruptions, label-stratified random sampling). Verdict: **conditional PASS for matched_condition mode** — promoted to a main contribution with a scoped claim.

Paper-safe SC3R claim:

> SC3R uses matched-condition normal images from other categories to source-validate conformal alarm thresholds, unlocking operating points below the target-only attainable-alpha floor 1/(k+1) without target anomaly labels. On stratified MVTec representative classes at k=4 it controls mean false alarms (0.067/0.098/0.204 at alpha 0.05/0.10/0.20, within alpha+0.02) with power 0.16/0.34 where target-only conformal is structurally silent, and no-harm rates of 93/82/84%. Gaussian noise and JPEG violate the false-alarm budget and are reported as limitations; at alpha >= 1/(k+1) the target-only anchor is preferred.

Evidence: `source_validated_threshold_sc3r_mvtec_repr_stratified_{detailed,summary}.csv`, `sc3r_mvtec_repr_stratified_hierarchical_ci.csv`. Full 15-class extension queued (`sc3r_views_mvtec_full15_stratified.csv`) to firm up the CI criterion before submission.

### Attainable-alpha claim (new)

> With k support images, LOIO conformal p-values are quantized on {j/(k+1)}; no alarm can fire below alpha = 1/(k+1). Reporting near-zero false-alarm rates at nominal alphas below the floor as "conservative coverage" is a resolution artifact, not a safety property.

Evidence: `attainable_alpha_{visa_full,mvtec_representative}_{summary,detailed}.csv` + new `scripts/analyze_attainable_alpha.py`.

### Corrected false-alarm numbers (float32 fix)

All k=4 alpha=0.20 false-alarm/detection cells previously reported as 0/0 were a float32 comparison artifact (1/5 stored as 0.20000000298 fails `p <= 0.20`). Corrected VisA full k=4 alpha=0.20: FAR 0.142-0.157, detection 0.585-0.610, precision ~0.81 across corruptions. The paper now states the tolerance rule explicitly.

### Prevalence-stress claim (promoted to main-text warning)

> ECE computed on conformal-derived scores is strongly prevalence-sensitive (VisA LOIO 0.404 at 1% prevalence vs 0.149 at 50%; method rankings reverse). ECE is a secondary metric; operational false-alarm/power/precision metrics are primary.

## 2026-07-12 Update: Full-Scale Evidence — SC3R Promoted, MVTec Full15 Conformal Complete

### SC3R final claim (gate FULL PASS at 15 classes)

> On all 15 label-stratified MVTec classes (k=4, seeds 0-2, five conditions, 675 cells), matched-condition SC3R tracks nominal false-alarm rates almost exactly (mean FAR 0.050/0.105/0.216 at alpha 0.05/0.10/0.20) with power 0.216/0.416 at sub-floor alphas where target-only LOIO is structurally silent, precision > 0.90, no-harm 89/82/89%, and hierarchical class-seed power-gain CIs excluding zero for every corruption condition. At alpha=0.20 the target-only anchor over-alarms under corruption (FAR up to 0.46) while SC3R stays near nominal.

Scope caveats to keep: k=4 only, seeds 0-2, per-condition exceedances jpeg@0.10 (0.121) and gaussian/jpeg@0.20 (0.226/0.235), requires multi-category deployment with matched conditions.

### MVTec full15 conformal claim

> LOIO conformal reliability replicates across datasets: overall ECE 0.0684 on all 15 MVTec classes (vs 0.0766 on full VisA), beating Vector Platt and Shift-Aware Platt in every k-corruption cell on both benchmarks with ranking unchanged.

### Operational asymmetry claim (new, important)

> At the first attainable operating point (alpha=0.20, k=4) target-only LOIO alarms are conservative on VisA (FAR 0.14-0.16) but anti-conservative on corrupted MVTec (FAR 0.31-0.46). Attainability of an operating point does not imply false-alarm control under shift; source validation restores it.

### Official baseline claim hygiene

Official AnomalyDINO (released code, 3 seeds) MVTec image AUROC k1/k4/k8: 0.9652/0.9756/0.9803 — reported as explicit accuracy reference rows; CRR does not claim MVTec ranking superiority.
# Historical claims snapshot — superseded

Despite the filename, this is not the current claim ledger. It predates the
nested source certification and multiplicity audit. Current claims are governed
by `neurocomputing_claim_audit.md` and the manuscript itself; numerical claims
here must not be copied into a submission without regenerated artifacts.
