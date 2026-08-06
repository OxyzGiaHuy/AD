# Mock review: feasibility-first manuscript

**Date:** 4 August 2026  
**Target:** Neurocomputing  
**Review posture:** skeptical reviewer; claims are assessed against the compiled manuscript and frozen artifacts, not against author intent.

## Provisional decision

**Major revision before submission.** The manuscript is scientifically coherent and within the broad Neurocomputing scope, but it is not yet upload-ready because the two pipeline figures, bibliography audit, author declarations, and immutable release snapshot remain open. The principal editorial risk is perceived novelty rather than a detected validity failure.

## Scorecard

| Dimension | Current assessment | Reason |
| --- | --- | --- |
| Technical correctness | strong, conditional | The proof directions, per-cell multiplicity allocation, fail-closed rule, and image/category estimands are internally consistent. Transfer is explicitly assumption-dependent. |
| Empirical integrity | strong | The old mixed-protocol `0.463` headline is removed; the current `0.341` result, controlled clean ranking/storage, and all primary audit tables are regenerated or re-aggregated automatically. Negative `0/960` results are retained, and the 960 configuration denominator is explicitly separated from the underlying target-category/seed cells. |
| Novelty | moderate | The integrated study-design contribution is useful, but the all-zero Bernoulli lower-bound argument is elementary and related to classical zero-failure intervals. CRESS uses established candidate testing and concentration tools. |
| Empirical breadth | moderate | Three industrial datasets and four controlled corruptions are useful, but no real production shift or category-rich archive demonstrates a transition to nonvacuous category certification. |
| Reproducibility | strong once released | Frozen revisions, manifests, per-image outputs, checksums, and automated audits exist. The final manuscript-derived artifacts still need an immutable public snapshot. |
| Presentation | strong except artwork | The feasibility-first order is clear, the subset aggregation ablation is explicitly scoped in the appendix, and the CAS double-column manuscript compiles cleanly. Two method figures remain placeholders. |
| Journal fit | plausible | The paper studies reliability limits for anomaly detectors built on frozen neural representations. The fit is stronger as learning-system reliability/study design than as a new anomaly-ranking model. |

## Red-team theory audit

### Proposition 1

The statement is valid only conditional on the reference and proposal stages and under the declared independence model for certification units. For the image analysis it now additionally conditions on fitted certification scorers. Candidate thresholds and the realized family size `M=|T|` are fixed before certification, the one-sided bound is applied at tail probability `delta/(2AM)`, and a union bound covers candidates, levels, and both unit definitions. Independence among the individual confidence events is not needed. This is a per-target/seed/source-view/condition statement; the manuscript explicitly rejects a simultaneous 95% interpretation over the complete grid. The zero fallback has zero alarm risk because the rank value is strictly positive.

The image case remains a conditional sensitivity analysis: equal weighting of retained images induces category weights proportional to retained image counts. The benchmark archive itself is stratified by category, and images within a category share a fitted scorer, so pooled iid Bernoulli alarms are an idealized model rather than a property guaranteed by the design. It is not a certificate for a uniformly sampled new category. Conversely, the category unit now explicitly includes its support construction and held-out views, so the fresh-target statement does not omit fitting randomness.

The benchmark contributes three or four distinct certification categories per cell; it does not empirically establish that they are independent draws from one meta-population. The manuscript now reserves `iid` for the explicit certificate model and no longer labels the observed categories independent as a design fact.

The category-level concentration step correctly places independence across complete category units rather than across images within a category. Arbitrary within-category dependence is compatible with treating the observed archive average as one bounded loss, although interpreting that average as future-view risk still requires representative within-category sampling.

### Proposition 2

The Hoeffding count is a necessary feasibility condition for the declared UCB, not a sufficient count for positive threshold selection. The table correctly applies integer ceilings. Its use is conservative but internally correct.

### Proposition 3

The Bernoulli counterexample correctly proves

`U_n(0,...,0) >= 1 - beta^(1/n)`

for deterministic uniformly valid distribution-free upper bounds over bounded iid losses. Rearrangement yields the stated category counts. The new confidence-direction interpretation is also correct: at `alpha=0.20`, three and four all-zero categories permit at most `48.8%` and `59.0%` confidence in the multiplicity-free setting; at `95%` confidence the unavoidable UCB floors are `0.632` and `0.527`.

The manuscript appropriately does not present the Bernoulli construction as a new generic inequality. Before submission, it should cite the classical zero-failure/rule-of-three lineage as well as the primary Clopper--Pearson and Hoeffding sources. Its category-unit positioning should also cite Dunn, Wasserman, and Ramdas's two-layer hierarchical conformal work, which already formalized prediction with exchangeable groups of repeated observations. A July 2026 preprint on hierarchical group-conditional conformal risk control should also be acknowledged as a terminology-adjacent guardrail: it controls known hierarchy nodes rather than transferring an anomaly threshold to a new category.

### Target transfer

Source-risk dominance can control one specified target only if the dominance assumption actually holds under the support construction being evaluated. The alternative marginal statement requires the complete target category-with-support-and-views unit to be a fresh independent draw from the same meta-population as the certification units; generic exchangeability alone is not invoked to justify Hoeffding concentration. Interpreting that archive mean as the alarm probability of a fresh normal view additionally requires representative within-category sampling. Normalization, routing, and source pooling prove none of these assumptions. The manuscript now states these boundaries consistently.

## Main reviewer objections and current defenses

### “CRESS fails in every category-certified configuration, so what method is being proposed?”

The paper should be judged as a feasibility and audit study, not as a successful universal thresholding method. CRESS is the protocol that makes the estimand and evidence split explicit; the `0/960` outcome is the predicted behavior of a fail-closed protocol when only three or four category units are available. The manuscript does not claim state of the art or unconditional target control.

This defense is credible only if the abstract, title, cover letter, and figures continue to lead with the category-budget question rather than with CRESS performance.

A different disjoint split does not remove the present obstruction. With nonempty reference and proposal roles, the 11-, 14-, and 15-category source pools can provide at most 9, 12, and 13 certification categories, respectively, still below the optimistic multiplicity-free count of 14 at risk level 0.20. This closes the objection that the result is caused only by the frozen 25% certification allocation; abandoning disjoint roles or adding assumptions would define a different procedure.

### “The theorem is just a rule-of-three argument.”

Substantively, this objection is partly correct. The defensible novelty is the integrated application to few-shot anomaly threshold certification: separating images from categories, deriving the candidate-family design calculus, demonstrating shift-induced target-only failure, and freezing a source protocol whose negative result matches that calculus. Citation and wording must make the classical lineage explicit.

### “The source archive leaks benchmark test information.”

CRESS uses known-normal held-out images from non-target categories, including benchmark normal evaluation partitions. It does not use target test images or labels to construct thresholds. This is a declared source-assisted setup, not the conventional target-category training-only benchmark protocol. The paper now discloses this explicitly and avoids comparing CRESS as if it followed a standard detector-training protocol.

The shared strict export is label-stratified and capped at 120 records per category, seed, and condition. Dataset labels therefore determine the retained evaluation strata. CRESS subsequently discards every anomalous source row, so source anomaly scores and target labels do not enter reference construction, proposal, certification loss, or threshold selection. This is transparent benchmark evaluation, not a claim of label-free archive acquisition.

### “The 960 failures inflate the evidence.”

The manuscript calls them frozen gate configurations, not independent trials. They share the same three/four-category obstruction. Their role is a boundary test across a declared grid, and the category result remains zero after excluding the `k=1` patch-split stress cells.

### “Why use p notation without automatic validity?”

They are finite rank values of conformal form. The manuscript retains conventional $p$ notation but now calls the outputs rank values unless validity conditions are invoked. It discloses the asymmetric LOIO construction, does not assume exchangeability, treats the CDF audit as descriptive, and uses “target-only rank transform” in the pipeline. Further wording changes should preserve this distinction.

### “Are the clean-baseline rows really comparable and reproducible?”

Only the controlled NN and PCA rows share the common feature, split, metric, and accounting protocol. Their class-by-seed means and storage are now rebuilt from complete run records by the core audit. The two local NN aliases are checked to be numerically identical and appear only once. AnomalyDINO-S and WinCLIP remain reported external references, are labeled as such, and are excluded from boldface comparisons. The paper has also removed the cached-feature latency claim because the surviving timings are dataset- and batching-dependent and are not needed for the certification contribution.

The PCA128 records require one further distinction: their historical wrapper stored an auxiliary calibration head, but the raw score used in the table is PCA-residual-only. The manuscript now states that its 0.189 MiB column measures the state required by the ranker, while the audit separately verifies the wrapper's 0.566 MiB total. This makes the favorable accounting explicit rather than presenting it as a logged end-to-end model size.

## Mandatory before upload

1. Replace both pipeline placeholders with legible final vector or high-resolution artwork whose flow exactly matches Method.
   If an AI tool contributes to an explanatory pipeline, identify its name, version, and role in each affected caption and in the general AI declaration. Data-derived heatmaps or residual maps must remain reproducible outputs rather than generated illustrations.
2. Complete the bibliography audit without changing scientific attribution: MPDD dataset paper; Clopper--Pearson; Hoeffding; zero-failure lineage; two-layer hierarchical conformal prediction; the July 2026 group-conditional risk-control preprint; HeAD-CP status; DOI/URL and capitalization cleanup.
3. Obtain both authors' approval for submission, declarations, CRediT roles, funding, acknowledgement, and AI disclosure.
4. Freeze and publish the final manuscript-derived tables, audit JSON, figure sources, checksums, and the now-aligned repository landing page.
5. Build and compile a fresh one-directory Editorial Manager package from a clean checkout.
6. Remove the explicit author-confirmation note from the cover letter only after confirmation is received.
7. Convert the four audited highlights to the separate Word document requested by Elsevier at final upload.

## Optional scientific upgrade with the highest value

A genuinely category-rich source archive could empirically test the transition predicted by the feasibility curves. The independent category count, not more seeds, corruption views, or images from the same categories, must increase. Such an extension may require new data and GPU inference, but it is not required to validate the current negative result. Re-running the same MVTec/VisA/MPDD categories cannot solve the category-count limitation and should not be presented as doing so.

## Bottom line

No current evidence supports guaranteeing acceptance, and no responsible editor can be “ensured” to accept a paper. The feasibility-first manuscript is nevertheless defensible: its strongest contribution is a quantitative study-design boundary plus an estimand-aware audit, not a new ranker or a successful universal certificate. After the mandatory release, bibliography, metadata, and artwork tasks are closed, the remaining risk is a reviewer judging that integrated contribution too incremental for Neurocomputing.
