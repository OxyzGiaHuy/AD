# Cover Letter — Neurocomputing

4 August 2026

Dear Editors of *Neurocomputing*,

We submit the manuscript **“How Many Categories Are Enough? Distribution-Free Certification Limits for Few-Shot Anomaly Thresholds”** for consideration as an original research article.

Few-shot anomaly detectors are commonly evaluated as rankers, although deployment requires an alarm threshold with a defensible false-alarm interpretation. Our manuscript studies the evidence needed for that second task. At nominal level 0.20, the target-only leave-one-image-out (LOIO) rule reaches an empirical false-alarm rate (FAR) of 0.341 on Gaussian-corrupted MVTec at four shots. The result is reported as a dataset-level synthetic-shift observation, not as a population failure probability.

The central contribution is a category-count feasibility calculus for source-assisted threshold certification. Even after zero observed category losses, a deterministic, uniformly valid, distribution-free 95% upper bound requires at least 14 independent and identically distributed category draws at risk level 0.20 in the optimistic one-candidate, no-multiplicity case. The requirement rises under simultaneous candidate testing. We instantiate the audit through Cross-category Reliability Estimation with Source Support (CRESS), which separates source categories into reference, proposal, and certification roles. With only three or four distinct certification categories, all 960 frozen gate configurations fail closed, consistent with the count calculation. These configurations share the same category-count boundary and are not treated as independent trials; the confidence allocation applies within each fixed cell rather than simultaneously over the grid. This is not solely a consequence of the frozen split: any disjoint reallocation with nonempty reference and proposal roles leaves at most 9 to 13 certification categories in the available source pools, still below 14. Image-unit sensitivity bounds can be nonzero, but they target a selected source-image mixture and are not presented as new-category certificates.

We believe the manuscript fits *Neurocomputing* because it contributes to the analysis and reliable use of learning systems built on frozen neural representations. It combines a formal feasibility result, an estimand-aware evaluation protocol, and audits on MVTec, VisA, and the Metal Parts Defect Dataset. The image-unit result is explicitly presented as an idealized independent-image sensitivity analysis, not as a design-based property of the stratified source archive. The principal-component residual ranker and generic confidence-bound primitives are explicitly treated as prior art; the novelty claim is limited to the category-budget analysis, the source-category protocol, and the empirical boundary test. Negative and conditional findings are retained rather than reframed as unconditional target control.

Public datasets, code, frozen revisions, and derived evaluation artifacts are identified in the manuscript.

**Author confirmation required before upload:** confirm that the manuscript is original, has not been published, is not under consideration elsewhere, has been approved for submission by both authors, and that the competing-interest statement is accurate. Replace this note with the confirmed declaration before submission.

Thank you for your consideration.

Sincerely,

Gia Huy Thai  
University of Science, VNU-HCM  
Ho Chi Minh City, Vietnam  
23120008@student.hcmus.edu.vn

Anh Nguyen, corresponding author  
Faculty of Information Technology, Van Lang School of Technology  
Van Lang University  
Ho Chi Minh City, Vietnam  
anh.nt@vlu.edu.vn
