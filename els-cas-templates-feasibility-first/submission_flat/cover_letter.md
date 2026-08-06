# Cover Letter — Neurocomputing

4 August 2026

Dear Editors of *Neurocomputing*,

We submit the manuscript **“How Many Categories Are Enough? Distribution-Free Certification Limits for Few-Shot Anomaly Thresholds”** for consideration as an original research article.

Few-shot anomaly detectors are commonly evaluated as rankers, although deployment requires an alarm threshold with a defensible false-alarm interpretation. Our manuscript studies the evidence needed for that second task. At nominal level 0.20, the target-only LOIO rule reaches an empirical FAR of 0.341 on Gaussian-corrupted MVTec at four shots. The result is reported as a dataset-level synthetic-shift observation, not as a population failure probability.

The central contribution is a category-count feasibility calculus for source-assisted threshold certification. Even after zero observed category losses, a deterministic, uniformly valid, distribution-free 95% upper bound requires at least 14 independent categories at risk level 0.20 in the optimistic one-candidate, no-multiplicity case. The requirement rises under simultaneous candidate testing. We instantiate the audit through CRESS, which separates source categories into reference, proposal, and certification roles. With only three or four certification categories, all 960 frozen gate configurations fail closed, as predicted by the calculus. Image-unit sensitivity bounds can be nonzero, but they target a selected source-image mixture and are not presented as new-category certificates.

We believe the manuscript fits *Neurocomputing* because it contributes to the analysis and reliable use of learning systems built on frozen neural representations. It combines a formal feasibility result, an estimand-aware evaluation protocol, and audits on MVTec, VisA, and MPDD. The PCA residual ranker and generic confidence-bound primitives are explicitly treated as prior art; the novelty claim is limited to the category-budget analysis, the source-category protocol, and the empirical boundary test. Negative and conditional findings are retained rather than reframed as unconditional target control.

This manuscript is original, has not been published, and is not under consideration elsewhere. Both authors have approved the submission and declare no competing interests. Public datasets, code, frozen revisions, and derived evaluation artifacts are identified in the manuscript.

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
