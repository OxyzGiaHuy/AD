# Cover Letter — Neural Computing and Applications

<!-- TODO: fill in author names, affiliation, and date before submission. -->

Dear Editors of Neural Computing and Applications,

We are pleased to submit our manuscript, **"Conformal Reliability Routing for Low-Storage Few-Shot Industrial Anomaly Detection,"** for consideration as an original research article.

## Summary

Few-shot industrial anomaly detectors built on frozen foundation features (DINOv2 memory banks, PCA/subspace residuals) rank defects well, but their raw scores are not trustworthy alarm probabilities — a gap that matters directly in deployment. Our paper proposes and evaluates a decoupled reliability layer for such detectors, making three contributions:

1. **A conformal reliability route evaluated by conformal-native evidence.** Leave-one-image-out (LOIO) conformal p-values computed only from the k normal support images improve calibration over the complete standard toolbox — Vector/Shift-Aware Platt, temperature scaling, isotonic regression, and histogram binning, all fit on an identical label-free calibration set — with paired Wilcoxon support across full corruption benchmarks on all 12 VisA and all 15 MVTec classes (93,000+ image rows). Crucially, we do not treat expected calibration error as the primary evidence: we audit the conformal false-alarm promise directly with empirical false-alarm rates at fixed levels, exact discrete uniformity tests, and risk–coverage curves, and we show that ECE on conformal-derived scores is strongly prevalence-sensitive.

2. **An attainable-alpha analysis of few-shot conformal alarms.** With k supports, no alarm can fire below α = 1/(k+1); we make this resolution floor explicit and show the first attainable operating point is conservative on VisA but anti-conservative on corrupted MVTec, with exact discrete uniformity tests localizing the direction of the exchangeability violation.

3. **SC3R, a source-validated cross-category thresholding scheme** that pools normal images from other categories to unlock operating points below the target-only floor without target anomaly labels. Against a pre-registered decision gate on all 15 MVTec classes, SC3R tracks nominal false-alarm rates almost exactly, and hierarchical class–seed bootstrap intervals for its power gains exclude zero under every corruption condition.

## Fit to the journal

The paper addresses reliability of neural feature–based detection systems under deployment shift — a core Neural Computing and Applications topic — and follows the journal's emphasis on rigorous, application-relevant evaluation: every headline claim carries a paired statistical test or bootstrap interval, negative results (adversarial fragility, weighted-conformal instability, honest boundaries of SC3R at k=8) are reported explicitly, and all datasets are public with code to be released upon publication.

## Declarations

This manuscript is original, has not been published, and is not under consideration elsewhere. All authors approved the submission and declare no competing interests.

<!-- TODO (optional but recommended): suggest 3–5 reviewers working on conformal anomaly detection or industrial AD calibration, with emails. -->

Thank you for your consideration.

Sincerely,
The Authors
