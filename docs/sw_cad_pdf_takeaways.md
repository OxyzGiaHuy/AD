# Takeaways From `Methode for SW-CAD.pdf`

Date: 2026-07-07

## One-Line Summary

The PDF is highly useful. It upgrades the current paper direction from "low-storage calibrated subspace detector with shift-aware reliability" to a stronger and more publishable framework:

> Shift-Aware Weighted Conformal Anomaly Detection (SW-CAD): frozen DINOv2 subspace residual ranking plus conformal p-values, patch-level FDR control, image-level false-alarm control, and density-ratio weighting under covariate/structured shift.

## What Is New Compared With Our Current Claim

Our current claim:

- PCA/subspace residual is the ranking score.
- Vector/Shift-Aware Platt calibration improves probability reliability.
- Evidence: VisA structured corruptions improve ECE for blur, brightness/contrast, JPEG.
- Limitation: Gaussian noise ECE not improved, no adversarial robustness.

The PDF suggests a stronger layer on top:

1. Convert residual scores into **conformal p-values**, not only calibrated probabilities.
2. Use patch-level conformal p-values for anomaly localization with **FDR control**.
3. Use image-level cross-conformal p-values for image decisions with **false alarm control**.
4. Use **density-ratio weighting** to handle covariate/structured shift.
5. Report **effective sample size** (`n_eff`) to quantify how much shift hurts the guarantee/resolution.
6. Use one estimated density ratio for both:
   - weighted conformal p-values;
   - shift-aware probability calibration.

This is much stronger than only adding shift descriptors to Platt scaling.

## Why This Helps Q1 Novelty

The current Shift-Aware claim is useful but still looks like post-hoc calibration engineering. SW-CAD gives it a clearer methodological identity:

- It has formal objects: p-values, FDR, false alarm control, density ratio, effective sample size.
- It addresses an industrial need: thresholding without anomaly labels.
- It explains why image-level conformal is hard in k-shot regimes through the `1/(k+1)` resolution floor.
- It justifies patch-level calibration as necessary, not just convenient.
- It unifies calibrated probability and guaranteed decision via one shift-awareness mechanism.

Potential stronger contribution:

> A two-granularity weighted conformal inference layer for low-storage DINOv2 subspace few-shot AD, giving calibrated probabilities plus interpretable p-values/false-alarm/FDR diagnostics under structured shift.

## Most Useful Components To Adopt

### 1. Out-of-sample support scoring

The PDF notes a key pitfall: if PCA is fit on all support patches and calibration residuals are computed on those same patches, calibration scores are deflated. This can produce anti-conservative p-values and inflated false alarms.

Adopt:

- k >= 2: leave-one-image-out (LOIO) support scoring.
- k = 1: spatial interleaved split.

This is a strong methodological detail and likely publishable because it directly addresses few-shot leakage/calibration bias.

### 2. Patch-level conformal p-values for localization

Use calibration residuals from support patches and compute p-values for test patches:

`p_j = (1 + # calibration residuals >= test residual_j) / (N_cal + 1)`

Then use BH or weighted conformal selection to produce anomaly masks at FDR level q.

This upgrades pixel anomaly maps from raw heatmaps to statistically interpretable maps.

### 3. Image-level cross-conformal decision

Because k <= 8, image-level calibration has poor resolution. The PDF explicitly states the resolution floor:

- k8 minimum p-value about `1/9 = 0.11`.
- k4 minimum p-value about `1/5 = 0.20`.
- k1 image-level conformal is nearly vacuous.

This is important: it explains why patch-level calibration is not optional.

### 4. Density-ratio weighting under shift

Instead of only adding shift descriptors, estimate a density ratio between support-domain features and unlabeled test-batch features.

Suggested mechanism:

- compress features through PCA coordinates;
- fit a logistic domain classifier: support covariates vs test-batch covariates;
- convert classifier output to density ratio `w_hat`;
- use `w_hat` in weighted conformal p-values and weighted Platt calibration.

This is a much more principled version of Shift-Aware Calibration.

### 5. Effective sample size

Report Kish effective sample size:

`n_eff = (sum w)^2 / sum(w^2)`

This gives a measurable statement:

- small shift: high `n_eff`, sharp p-values;
- severe shift: low `n_eff`, conservative/low-resolution p-values.

This can become a very nice figure/table for the paper.

## Risks And Caveats

1. Patch exchangeability is approximate because patches within an image are correlated.
2. Image-level conformal is weak for k <= 8 due to resolution floor.
3. Density-ratio estimation uses unlabeled test batches that may contain anomalies, so the estimated ratio is for a mixture, not purely normal Q/P.
4. Weighted conformal validity depends on density-ratio quality.
5. We should not overclaim formal guarantees under adversarial attacks.
6. WCS/Jin-Candes citation must be checked carefully before relying on it in final paper.

## Recommended New Paper Framing

Old framing:

> Low-storage calibrated subspace detector with Shift-Aware Platt calibration.

Stronger framing after PDF:

> Shift-Aware Weighted Conformal AD: a low-storage DINOv2 subspace detector with two-granularity conformal p-values, density-ratio weighted calibration under shift, and measured reliability/power trade-offs via effective sample size.

## Experiments To Add

### P0: Conformal smoke/prototype

- Implement LOIO calibration residuals for k >= 2.
- Implement patch-level conformal p-values.
- Compute empirical normal false alarm / patch FDR on held-out normal images.
- Compare in-sample calibration vs LOIO calibration to show leakage/anti-conservative behavior.

### P1: Weighted conformal under corruption

- Use VisA full corruption outputs.
- Estimate density-ratio weights using compressed PCA coordinates.
- Compare unweighted conformal vs weighted conformal:
  - empirical false alarm rate;
  - FDR/proxy pixel false discovery where masks exist;
  - `n_eff`;
  - power/recall trade-off.

### P2: Unified weighted Platt + conformal

- Replace heuristic Shift-Aware descriptors with density-ratio weighted Platt objective.
- Compare:
  - vector Platt;
  - current Shift-Aware Platt;
  - weighted Platt;
  - gated/weighted hybrid.

## Claim If Experiments Work

> SW-CAD provides low-storage few-shot anomaly ranking with statistically interpretable p-values and calibrated probabilities. Under structured shift, density-ratio weighting improves reliability and exposes the coverage-power trade-off through effective sample size.

This is materially stronger than the current claim and has a better chance of supporting a Q1 submission.
