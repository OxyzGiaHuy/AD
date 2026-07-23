# Cover Letter — Neurocomputing

23 July 2026

Gia Huy Thai  
University of Science, VNU-HCM  
Ho Chi Minh City, Vietnam

Anh Nguyen  
Faculty of Information Technology, Van Lang School of Technology  
Van Lang University  
Ho Chi Minh City, Vietnam  
Email: anh.nt@vlu.edu.vn

Dear Editors of Neurocomputing,

We are pleased to submit our manuscript, **"Conformal Reliability Routing for Low-Storage Few-Shot Industrial Anomaly Detection,"** for consideration as an original research article.

## What this work teaches about learning systems

The paper answers a question about few-shot learned detectors themselves, with industrial inspection as the testbed: **what can an alarm calibrated on only k normal examples of a frozen deep representation guarantee, and where does it structurally fail?** Our contributions are a matched pair of problem and mechanism:

1. **An exact resolution law for few-shot conformal alarms.** No alarm calibrated on k supports can fire below α = 1/(k+1); we make this floor and its shift-induced failure directions exact and checkable with discrete uniformity tests (conservative on VisA, anti-conservative on corrupted MVTec), and show that the textbook remedy — randomized p-values — crosses the floor but inherits the invalidity (false-alarm rates up to 2.3× nominal).

2. **SC3R, a source-validated cross-category thresholding mechanism** that enables alarms below the target-only floor using normal examples of other categories. Historical experiments on MVTec and VisA show sub-floor power with observed false-alarm rates near the pre-specified budget in several settings. We explicitly separate this empirical evidence from strict nested source certification, use multiplicity-aware uncertainty in the revised protocol, and do not claim unconditional target-domain control under transfer.

Supporting these claims, the leave-one-image-out conformal route improves calibration over the complete standard toolbox — Platt-family calibrators plus temperature scaling, isotonic regression, and histogram binning, all fit on an identical label-free calibration set — under paired Wilcoxon tests on 93,000+ image evaluations, while leaving the detector's ranking untouched.

## Fit to Neurocomputing

The work sits in the journal's core territory of learning systems and their reliability: it analyzes a structural property of decision rules built on learned representations, explains the mechanism behind its failure modes, and validates the proposed remedy with ablations, sensitivity studies, and paired statistical tests rather than single benchmark numbers. It complements recent Neurocomputing work on zero-/few-shot anomaly detection with foundation models (e.g., ClipSAM, Neurocomputing 2025; cross-modal prompt regularization, Neurocomputing 2026) by addressing the question those detectors leave open: how much their alarms can be trusted. Negative results (adversarial fragility, weighted-conformal instability, an audited 20-point gap between WinCLIP's reported numbers and its only public reimplementation) are reported explicitly, and all datasets are public with code to be released upon publication.

## Declarations

This manuscript is original, has not been published, and is not under consideration elsewhere. All authors approved the submission and declare no competing interests.

<!-- TODO (optional but recommended): suggest 3–5 reviewers working on conformal anomaly detection or industrial AD calibration, with emails. -->

Thank you for your consideration.

Sincerely,

Gia Huy Thai and Anh Nguyen  
Corresponding author: Anh Nguyen
