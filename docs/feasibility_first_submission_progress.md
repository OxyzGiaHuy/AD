# Feasibility-first Neurocomputing submission progress

**Last updated:** 7 August 2026  
**Goal status:** completed for the requested scientific/LaTeX editing scope; final pipeline artwork integrated  
**Working manuscript:** `els-cas-templates-feasibility-first/`  
**Protected comparison copy:** `els-cas-templates/`

## Non-negotiable scientific rules

1. Proved, conditional, empirical, and diagnostic statements remain distinct.
2. Image-unit evidence is never substituted for independent-category evidence.
3. A source-domain certificate is not presented as unconditional target control.
4. The 960 cells are frozen configurations, not independent statistical replications.
5. Negative and fail-closed results remain visible.
6. A new abbreviation is written in full at its first occurrence in the paper and only the abbreviation is used thereafter.
7. Numerical claims must be reproducible from the declared frozen artifacts; narrative convenience is not sufficient.
8. The two final pipeline figures must remain traceable to the author-supplied `fig` branch assets and included in the flat submission package.

## Phase status

| Phase | Status | Current result |
| --- | --- | --- |
| 1. Empirical lineage audit | completed for core claims | Target-only, strict CRESS, controlled clean ranking, and analytic storage values are now regenerated or re-aggregated from run-level records. |
| 2. Theory and estimand audit | completed within author-declared bibliography boundary | Propositions 1 to 3 and Corollary 1 were rechecked; image-mixture, archive-level category, and fresh-view transfer estimands are separated. A category unit now explicitly includes its support construction and held-out views, while the pooled image model is labeled idealized rather than implied by the stratified archive. The 95% family guarantee is explicitly per fixed cell, not simultaneous over the experimental grid. The author retains the final bibliography pass. |
| 3. Feasibility-first narrative | completed | Results now follow shift audit → feasibility → strict CRESS → pooled reference → supporting ranker. |
| 4. Legacy-result pruning | completed | Historical calibration, routing, abstention, FGSM, and non-independent CRESS analyses are not compiled into the evidentiary manuscript. |
| 5. Abbreviation/terminology audit | completed for compiled paper | Every declared full-form/abbreviation pair occurs exactly once in prose; later prose uses the abbreviation, and the audit fails on repeated full forms. |
| 6. Tables and numerical captions | completed for compiled paper | Captions are self-contained; storage accounting, target-only values, realized candidate-family accounting, strict-CRESS configuration versus underlying-cell denominators, pooled-cell averaging, and the subset scope of the aggregation ablation are explicit. A 77-check claim-surface audit traces printed values, qualifiers, and the three contribution-to-evidence links to the upstream reports. |
| 7. Neurocomputing/Elsevier LaTeX audit | completed provisionally | `cas-dc`, A4, two columns, official `cas-model2-names` bibliography style, 17 pages after final artwork integration; PDF has no undefined references or content overflows. |
| 8. Submission documents | content completed; upload conversion pending | The feasibility-first cover letter and four compliant highlights are present. The final upload still requires the approved author declaration and conversion of the controlled highlight text to a separate Word document. |
| 9. Pipeline artwork | completed | `CRESS_ab.pdf` and `CRESS_c.pdf` from `origin/fig` are integrated as Figures 2 and 3; source-asset hashes are preserved exactly and publication-size rendering has been inspected. |
| 10. Author metadata and final release | blocked on author confirmation | CRediT, funding/acknowledgement confirmation, MPDD scholarly citation, and final immutable manuscript snapshot remain. |
| 11. Final mock review | completed provisionally | The skeptical review finds no current validity failure but recommends major revision before upload because artwork, foundational-statistics citations, author declarations, and the immutable release remain open; novelty perception is the principal scientific risk. |
| 12. Editorial Manager package | builder completed and independently retested; final package pending | A clean temporary flat build reproduces the current 17-page PDF with byte-identical extracted text, portable metadata, no undefined citations or references, and no content overflow. The builder includes both final pipeline PDFs, the compiled appendix, aggregation table, `references.bib`, and generated `main.bbl`. The present `submission_flat/` is stale and must not be uploaded. |
| 13. Public repository presentation | completed locally; publication pending | The root README now matches the feasibility-first title, states the negative/conditional result without overclaiming, distinguishes the historical scaffold from manuscript evidence, and gives the exact paper-facing audit commands. The aligned page must still be included in the immutable public snapshot and tested from a clean checkout. |

## Current stopping condition

The compiled scientific manuscript is stable at 17 A4 two-column pages with both final pipeline figures integrated and no placeholders. All six audit layers pass, and a fresh one-directory Elsevier build contains both pipeline PDFs and reproduces byte-identical extracted PDF text. Author-owned bibliography corrections, title approval, CRediT/funding/acknowledgement approval, AI-artwork disclosure confirmation, and the immutable release remain submission-administration tasks rather than unresolved manuscript calculations; no GPU job is required.

## Critical scientific corrections made

### Target-only lineage correction

The earlier headline FAR `0.463` came from a fold-matched LOIO column and an older support-sampling protocol, whereas Method defines asymmetric LOIO with full-support test scores. It was therefore retired rather than rationalized. The current audit is regenerated from:

- `matched_loio_views_mvtec_nc_gpu_20260722_e7f1759.csv`
- `matched_loio_views_visa_nc_gpu_20260722_e7f1759.csv`
- p-value field `image_p_loio_legacy`, which matches Eq. (4)
- five nested support seeds.

The reproducible headline is now MVTec Gaussian noise, `k=4`, `alpha=0.20`, FAR `0.341`. It is approximately 1.7 times nominal and is described as the largest dataset-level aggregate in the frozen grid, not as a population FAR. Category heterogeneity is now explicit: median `0.215`, IQR `0.169–0.481`, and 9 of 15 categories exceed `0.20`.

### Statistical-inference correction

The previous class-and-seed Monte Carlo reference did not preserve the dependence created by the same test images appearing across support seeds. No Monte Carlo p-value is now used in the manuscript. The p-value CDF figure is explicitly descriptive.

The confidence allocation in Proposition 1 covers candidates, reported risk levels, and the two statistical-unit definitions within one fixed target/seed/source-view/condition cell. It does not cover all target cells or the 960 gate configurations in one simultaneous 95% event. This scope is stated in Experiments, Results, and Limitations and enforced by the manuscript audit.

The target-transfer corollary has also been narrowed from generic category exchangeability to the assumption actually used by the concentration argument: the complete target unit must be a fresh independent draw from the same category meta-population as the certification units. For a fixed realized target, source-risk dominance must hold under the support construction being evaluated. Neither route yields category-conditional control for every target.

The manuscript now calls the three or four observed certification categories distinct rather than asserting that the benchmark design makes them independent. Independence and common distribution are explicit modeling assumptions for the feasibility curves and source certificate. The Highlights state this compactly as “independent same-population categories,” while Figure 1 and Limitations state the assumption in full.

### Reproducibility-specification correction

The compiled Method and Experiments now state details previously available only in code or manifests:

- local DINOv2 ViT-S/14 preprocessing uses a direct 518 by 518 RGB resize, ImageNet normalization, a 37 by 37 token grid, and 384-dimensional normalized patch tokens;
- the operational score is the mean of the 14 largest residuals, exactly `ceil(0.01 * 1369)`, while the separate clean benchmark uses the patch maximum;
- support sets are nested across `k` within each of five sampling seeds;
- corruptions use Gaussian standard deviation 0.05, box-filter radius one, brightness/contrast transform `1.15(x-0.5)+0.55`, and a JPEG quality-60 round trip, followed by 8-bit PNG materialization;
- the strict export applies a deterministic label-stratified cap of 120 evaluation records per category/seed/condition, then excludes all anomalous source rows before reference, proposal, or certification construction;
- mismatched source routing uses the lexicographic successor with wraparound, and category-count rounding uses largest remainders with ties resolved toward certification.

These additions do not change any result. They close reproducibility gaps and disclose exactly where benchmark labels determine evaluation-archive composition while preserving the claim that target labels and source anomaly scores do not enter threshold selection.

### Image-unit certificate correction

Image-unit Clopper–Pearson results are conditional on an idealized iid source-image model and target the selected source mixture. The benchmark archive is stratified by category and images within a category share a support-fitted scorer, so iid pooled alarm indicators are not presented as a design-based property. Proposition 1 conditions the image analysis on fitted certification scorers. These bounds are no longer called partial evidence for a new-category certificate. The category result continues to require independent category units and a transfer condition.

The category-unit definition now includes the category, its support-set construction, and its held-out normal-view mechanism. The exchangeable-target statement in Corollary 1 carries the same complete unit, preventing the support randomness used for fitting and normalization from disappearing from the estimand.

The Method now also places the independence requirement at the correct level. Once the within-category archive average is treated as the bounded loss $L_c$, the category-level Hoeffding step does not require the individual views inside that category to be independent; it requires iid sampling across complete category units. Representativeness of the within-category archive remains a separate condition for interpreting that average as future-view alarm risk.

### Storage correction

The old PCA64 storage value `0.472 MiB` included a legacy synthetic-anomaly MLP that CRESS does not use. The clean-ranking table now counts only the category-specific PCA mean and basis:

- PCA64: `0.095 MiB`
- PCA128: `0.189 MiB`.

No auxiliary calibration head is included in those values.

The remaining PCA128 provenance detail is now explicit. Its historical run wrapper stored 0.566 MiB because it included an auxiliary probability-calibration head and normalization state, although the wrapper's raw `score_images` path uses only PCA residuals. Table 6 reports 0.189 MiB because its declared estimand is the state required by the reported ranker. The core audit now verifies both the 0.566 MiB historical wrapper total and the 0.189 MiB PCA-only accounting instead of silently ignoring the discrepancy.

### Clean-ranking provenance correction

The controlled clean table is no longer trusted as a manually copied summary. The core audit re-aggregates all class-by-seed run notes: 300 cells per MVTec method and 240 per VisA method across the four declared values of $k$. PCA64 is taken from the pure local PCA-residual configuration, while the two local memory-bank aliases are verified numerically identical before being represented by the single label “Controlled DINOv2 NN.” This also corrected the full VisA PCA64 $k=8$ mean to AUROC/AP `0.882/0.894`.

The deleted official-code CSVs do not support a repository-auditable reproduction claim. The AnomalyDINO-S (448) rows are therefore now explicitly labeled “reported” and use the values in the cited WACV paper under its own protocol. They are not bolded or mixed into controlled-protocol comparisons.

Cached-feature runtime varied materially by dataset and batching in the surviving run records. Because runtime is not central to the feasibility claim and the prior sentence reported only the favorable MVTec range without saying so, the manuscript now makes no runtime claim. The efficiency comparison is restricted to category-specific state with an explicit formula.

### Aggregation-sensitivity scope correction

The compiled paper now cites the aggregation ablation in the appendix rather than leaving its source file uncompiled. Its caption names the exact subset—MVTec bottle, cable, and hazelnut; VisA candle, cashew, pcb1, and pipe fryum—and seeds from 0 to 2. The Results report the largest displayed gap to the best tested aggregator as `0.018`, but explicitly restrict the conclusion to this subset and grid. The paper therefore justifies checking the max-versus-top-1% protocol difference without claiming full-dataset invariance to patch aggregation.

### Scope correction

The compiled paper no longer uses historical ECE/calibrator, routing, abstention, FGSM, or non-independent CRESS tables as evidence. Their source files are preserved for traceability, but the manuscript is narrower and protocol-consistent.

### Related-work identity correction

The author-owned bibliography handoff now distinguishes two July 2026 records that had been at risk of conflation. arXiv:2607.25273 is HeAD-CP by Lam and Nguyen and concerns graph diffusion for conformal prediction sets. arXiv:2607.24562 is Salem et al.'s hierarchical group-conditional conformal risk control for language-model selective prediction; its primary arXiv class is `cs.AI`, not `cs.LG`. Dunn, Wasserman, and Ramdas remains the closest established two-layer hierarchical prediction-set precedent. These works narrow CRESS's novelty without solving its new-category anomaly-threshold estimand.

### Rank-value terminology correction

The target-only construction and source-reference map retain conventional $p$ notation, but the compiled manuscript now calls their outputs conformal-form rank values unless validity assumptions are explicitly invoked. This prevents the notation itself from implying exchangeability or finite-sample p-value validity. The Results compare the empirical rank-value CDF with the exchangeable discrete-uniform reference and state that this comparison is descriptive.

### Available-category interpretation

Proposition 3 is now also expressed in the confidence direction. At `alpha=0.20`, three and four all-zero categories can support at most `48.8%` and `59.0%` confidence in the optimistic multiplicity-free setting. If confidence is fixed at `95%`, their unavoidable all-zero UCB floors are `0.632` and `0.527`. This is a restatement of the necessary bound, not a new sufficient certificate.

The split-ratio objection is now resolved explicitly. The eligible source pools contain 14 within-MVTec, 11 within-VisA, or 15 transfer-source categories. Because the reference and proposal roles must remain nonempty in the disjoint protocol, even a certification-heavy reallocation leaves at most 12, 9, or 13 certification categories. All remain below the optimistic multiplicity-free requirement of 14 at `alpha=0.20`; the frozen 25% certification allocation is therefore not the sole cause of the category-level failure.

### Source-archive transparency

The paper now states that the image-unit mixture weights each retained source image equally, whereas the category estimand weights each certification category equally. It also discloses that the benchmark source archive uses known-normal held-out views from non-target categories, including normal evaluation partitions. This is a source-assisted protocol, not the conventional target-category training-only benchmark protocol.

### Current Elsevier AI-policy alignment

Elsevier's [journal AI policy updated in June 2026](https://www.elsevier.com/en-au/about/policies-and-standards/generative-ai-policies-for-journals) permits AI assistance for explanatory workflow diagrams, but requires the specific tool, version, and use to be disclosed in each affected caption and in the general AI declaration. It permits AI-supported plots or heatmaps only when they are directly derived from underlying data through a reproducible method; it does not permit fabricated or altered research images. The compiled paper now uses Elsevier's current declaration heading and reports Codex-assisted code review/test/audit scripting in Reproducibility and Claim Rules. The final pipeline PDFs are integrated. If GPT assisted their artwork, both captions and the declaration must identify the tool, version, and use before release; all embedded residual and heatmap outputs must remain derived from the frozen data pipeline.

### Candidate-family accounting

The notation now distinguishes the realized family size $M=|\mathcal T|$ from its cap $M_{\max}=20$. This matches the implementation: the confidence allocation uses the number of proposal candidates actually retained in each cell, not an unexplained fixed value of 20. Table 1 reports design calculations for representative realized sizes $M\in\{1,5,20\}$, with $M=20$ the cap.

### Figure 4 terminology

Figure 4 has been regenerated from `target_only_asymmetric_nested5_cdf.csv`. Its axes now read “attainable rank value” and “empirical CDF,” matching the manuscript's validity-aware terminology; the lower-right insets and connector rays remain inside the panels and keep their tick labels on the right.

### Figure 1 visual hierarchy

The analytic feasibility figure has been redesigned around the study-design decision rather than decorative styling. Its formulas and crossing counts are unchanged. The frozen `n=3/4` region, `14/29/59` necessary counts, and two practical callouts occupy white-backed regions that no data curve crosses. A colorblind-safe palette is paired with solid, dashed, and dash-dot strokes plus circle, square, and triangle markers, so the three bounds remain distinct in grayscale. The legend is explicitly isolated from the horizontal alpha guides, preventing guide colors from being mislabeled as analytic curves. The final vector source and PDF are both retained, and four figure-specific regression checks now guard the formulas, quantities, assets, and collision/print controls.

### Automated claim audit

`scripts/audit_feasibility_first_core_claims.py` now checks the complete target-only corruption table, four-corruption aggregates, category heterogeneity, CDF gaps, matched-LOIO sensitivity, controlled clean-ranking coverage and means, local NN-alias equivalence, analytic and logged ranker storage, theory counts and confidence restatement, maximum certification counts under any nonempty disjoint role allocation, all primary strict-CRESS files, `0/960`, minimum UCBs, image-unit nonzero fractions, pooled-source results, and the fact that the category result remains zero after excluding `k=1`. It also validates all 13 CPU-manifest inputs plus the 48 primary strict outputs and empirical gate against their SHA-256 values, confirms the 1,500/1,200/600-cell artifact audits, and preserves the CPU manifest's recorded dirty-worktree warning rather than hiding it. The current full JSON report has been regenerated and passes.

The same script now has a dependency-free `--theory-only` mode. Its current report, `outputs/paper_tables/feasibility_first_theory_claim_audit.json`, passes and additionally verifies that nonempty reference/proposal roles cap the present certification pools at 12, 9, and 13 categories, all below the 14-category optimistic boundary.

`scripts/audit_feasibility_first_manuscript.py` separately checks the compiled section order, including the appendix, unique first-use abbreviation expansions, absence of repeated full forms after expansion, absence of pipeline placeholders, presence and inclusion of both final pipeline assets, official CAS class/bibliography settings, and absence of retired or overclaiming terms such as `0.463`, visible `SC3R`, `CalibSubspaceHead`, or a claim that the 960 configurations are independent. It also verifies that Figure 1 retains the audited formulas, key counts, vector source, collision guards, and distinct grayscale line styles. Its current JSON report passes.

`scripts/audit_feasibility_first_method_alignment.py` is a dependency-free static alignment audit between the compiled Method, the frozen implementation, and `submission_cpu_pipeline.final.json`. It checks DINOv2 preprocessing, top-fraction scoring, nested support sampling, corruption parameters, the asymmetric target-only construction, the $k=1$ fallback, normalization/routing order, four source-view modes, known-normal filtering, deterministic category split, disjoint reference/proposal/certification roles, source-reference rank map, candidate cap, category losses, $\delta/(2AM)$ allocation, Hoeffding and Clopper--Pearson formulas, zero fallback, frozen grid, and iid target-transfer scope. Its current report passes all 22 checks. Numerical outputs remain the responsibility of the separate core-claim audit.

`scripts/audit_feasibility_first_table_aggregations.py` is a separate dependency-free denominator audit. It verifies 240 gate configurations per source-to-target job and 960 overall; 75, 60, or 30 target-category/seed cells per configuration; and 18,000, 14,400, or 7,200 underlying cells per unit in the corresponding job. It also verifies that the image/category bookkeeping copies of direct pooled-source conformal are identical, averages only one copy per target cell, and reproduces every rounded FAR/power entry in Table 5. Its current report passes all 40 checks.

`scripts/audit_feasibility_first_claim_surface.py` closes the traceability loop from evidence to prose. It reads the four upstream audit reports and checks the rounded values and scope-bearing qualifiers that actually appear in the abstract, main text, and compiled tables. The current report passes all 77 checks. In particular, it guards the scope of the 0.341 headline, all rows of the category-count table, the complete 16-cell corruption table, the strict-CRESS and pooled-source summaries, the `k>1` sensitivity, controlled clean-ranking values, aggregation ablation, and the distinction between PCA128 ranker state and its historical calibration wrapper. Its emitted contribution-evidence matrix also maps each of the three Introduction contributions to the relevant Method/Results surfaces, upstream reports, and explicitly excluded claims. Its pass status establishes manuscript-to-artifact consistency, not the truth of untested population assumptions.

The manuscript audit now passes all 46 structural, semantic, figure-asset, and Figure 1 regression checks. It enforces the one-to-six keyword count, a sub-250-word approximate prose count for the abstract, three to five explicitly bulleted highlights of at most 85 characters, explicit portable PDF metadata, the exact compiled figure/table set, and a callout for every compiled item. It additionally fails if either final pipeline asset is missing, if a placeholder returns, if the category unit omits support construction, if independence is placed at the image rather than complete-category level for the category bound, if the pooled-image iid model is not labeled idealized, if the all-zero impossibility statement loses its deterministic distribution-free scope, if the confidence claim becomes grid-wide, if AI-assisted code/audit work loses its required disclosure, or if the declared preprocessing, score aggregation, corruption parameters, nested support sampling, and strict archive-label scope disappear. The semantic guards also require every core section to preserve the necessary-versus-sufficient distinction, source-versus-target transfer boundary, protocol-not-ranker positioning, noncausal dataset-specific shift scope, conformal-form rank qualification, and non-independent interpretation of the 960 configurations. This prevents later wording edits from silently weakening submission format, reproducibility, figure semantics, or claim boundaries.

The manuscript, theory, method-alignment, denominator, and claim-surface audits were rerun after the final Results wording pass and all report `pass`. The full empirical core audit was also rerun through the committed offline `uv` environment with NumPy and pandas and regenerated its passing JSON from the declared artifacts. A final clean-checkout release test remains necessary because the current checkout contains ongoing author work and has not yet been frozen as the review snapshot.

## Verified core numbers

| Claim | Verified value and scope |
| --- | --- |
| Target-only headline | FAR `0.341`, MVTec Gaussian noise, `k=4`, `alpha=.20`, pooled over images and five support-sampling seeds |
| MVTec four-corruption aggregate | FAR/detection `0.278/0.880` at `k=4`; `0.200/0.868` at `k=8` |
| VisA four-corruption aggregate | FAR/detection `0.142/0.595` at `k=4`; `0.094/0.555` at `k=8` |
| Optimistic DF counts | `14/29/59` at alpha `.20/.10/.05`; necessary and multiplicity-free, not sufficient |
| Frozen DF counts, M=1 | `22/46/94` |
| Hoeffding counts, M=1 | `60/240/958` |
| Strict category audit | every target cell receives `tau*=0`; all `960` configuration gates fail |
| Minimum category UCB | MVTec `.950`, VisA `1.000`, MVTec→VisA `.961`, MVTec→MPDD `.986` |
| Image-unit positive thresholds | `36.7%–60.3%`, idealized conditional iid source-image sensitivity only |
| Controlled clean coverage | MVTec `75` class-seed cells per shown $k$; VisA `60` per shown $k$ for NN, PCA64, and PCA128 |
| VisA PCA64 at $k=8$ | AUROC/AP `0.882/0.894`, re-aggregated from all 12 classes and 5 seeds |
| Category-specific ranker state | PCA64 `0.095 MiB`, PCA128 `0.189 MiB`, NN `2.005/6.000 MiB` from explicit fp32 counts |

## Current format status

- Elsevier CAS double-column class: `cas-dc` version 2.4.
- Official CAS bibliography style: `cas-model2-names` with numeric, sorted-and-compressed citations.
- Elsevier's [current LaTeX instructions](https://www.elsevier.com/en-gb/researcher/author/policies-and-guidelines/latex-instructions) require Editorial Manager source files to reside at one folder level. A fresh temporary flat-package test now compiles independently to the same 17-page PDF text, contains no subdirectories, includes both final pipeline PDFs, and includes both `references.bib` and the generated `main.bbl`. The permanent submission package remains intentionally deferred until the author-owned bibliography and declarations are final.
- PDF: A4, 17 pages, `Page 17 of 17` on the last page. The additional page results from replacing compact placeholders with publication-size pipeline artwork; no artificial downscaling is applied because the labels remain readable at the current size.
- Abstract: 243 approximate prose words by the manuscript audit; the count remains below 250.
- Keywords: six.
- Highlights: four explicit bullets, 71 to 82 characters each including the bullet marker, with nonessential abbreviations removed; the category-count bullet states both independence and common-population scope without using the `iid` acronym.
- PDF metadata: title, both authors, subject, six keywords, and the CAS double-column creator string are explicitly reset after front-matter generation to avoid the class's nonportable author separators.
- Undefined citations/references: none.
- Content overfull boxes: none after line-breaking cleanup. The remaining front-matter box is generated internally by the CAS class and does not visibly overflow the page.
- Final artwork: Figures 2 and 3 are integrated from `origin/fig`; no pipeline placeholder remains.

## Current blockers requiring author input

1. Confirm whether GPT or another generative tool contributed to Figures 2 or 3; if so, add the tool/version/use disclosure to both captions and the general declaration.
2. Add the scholarly MPDD dataset citation to `references.bib` and cite it at first dataset use; the user has reserved bibliography editing.
3. Add appropriate primary citations for the Clopper--Pearson interval, Hoeffding's inequality, the classical zero-failure/rule-of-three lineage, and Dunn et al.'s two-layer hierarchical conformal work; Proposition 3 and the category-unit discussion must not imply those primitives or hierarchical exchangeability are new. Recheck the July 2026 Salem et al. hierarchical group-conditional risk-control preprint and, if still public, distinguish its known hierarchy nodes from the new-category transfer estimand.
4. Apply `docs/references_bib_read_only_audit.md`: HeAD-CP acceptance is now verified on the official MAPR list but final proceedings metadata remain pending; fix the UniAD DOI field, DINOv2 venue/capitalization, the stray SubspaceAD block, and protected capitalization of method names.
5. Approve per-author CRediT roles. Suggested roles must not be inserted without both authors’ agreement.
6. Confirm the funding statement and replace the generic “advisor” acknowledgement with an approved name or remove it.
7. Confirm the competing-interest and generative-AI disclosures with both authors.
8. Replace the explicit author-confirmation note in the cover letter with the approved originality/exclusivity declaration.
9. Build a fresh flat package; the intermediate packaging test is explicitly marked `STALE_DO_NOT_SUBMIT`.
10. Commit and publish the final feasibility-first manuscript, aligned repository README, and regenerated artifacts as an immutable review snapshot, then execute every documented audit from a clean checkout.
11. Convert `highlights.txt` to the separate Word document requested by Elsevier and upload it as Highlights; use the text file as the audited source rather than the final upload format.

No additional GPU run is required by the current core claims. A new GPU run would be scientifically useful only if the study is expanded to genuinely category-rich source data, real operational shifts, or a new assumption-based certificate; rerunning the present three/four-category protocol cannot remove the category-count boundary.

## Honest readiness assessment

The manuscript is now materially more coherent and defensible than the earlier CRESS-first version, but acceptance cannot be guaranteed. The main remaining scientific risk is novelty perception: Proposition 3 uses an elementary Bernoulli counterexample, and the strict CRESS result is negative. The defense is the integrated contribution—category-budget calculus, estimand separation, shift audit, and a frozen boundary test—not a claim of a new generic concentration inequality or a successful universally transferable thresholding method. Final metadata, bibliography completion, AI-artwork disclosure confirmation, and independent human review remain necessary before submission.

## Key generated files

- `els-cas-templates-feasibility-first/main.pdf`
- `els-cas-templates-feasibility-first/cover_letter.md`
- `els-cas-templates-feasibility-first/highlights.txt`
- `scripts/audit_target_only_current_artifacts.py`
- `scripts/plot_target_only_uniformity_current.py`
- `outputs/paper_tables/target_only_asymmetric_nested5_cells.csv`
- `outputs/paper_tables/target_only_asymmetric_nested5_aggregate.csv`
- `outputs/paper_tables/target_only_asymmetric_nested5_cdf.csv`
- `outputs/paper_tables/feasibility_first_core_claim_audit.json`
- `outputs/paper_tables/feasibility_first_theory_claim_audit.json`
- `outputs/paper_tables/feasibility_first_method_alignment_audit.json`
- `outputs/paper_tables/feasibility_first_table_aggregation_audit.json`
- `outputs/paper_tables/feasibility_first_claim_surface_audit.json`
- `scripts/audit_feasibility_first_core_claims.py`
- `scripts/audit_feasibility_first_manuscript.py`
- `scripts/audit_feasibility_first_method_alignment.py`
- `scripts/audit_feasibility_first_table_aggregations.py`
- `scripts/audit_feasibility_first_claim_surface.py`
- `scripts/build_flat_elsevier_submission.py`

The GPU export retains the historical field name `image_p_loio_legacy`, but the regenerated paper-facing artifacts use `asymmetric` because that field implements the current Method: LOIO calibration scores with a full-support test score. The older `target_only_legacy_nested5_*` files are superseded and are not the declared manuscript artifacts.
