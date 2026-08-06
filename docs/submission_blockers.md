# Submission blockers requiring author confirmation

This checklist contains only facts that should not be inferred by an editing tool. The current scientific manuscript compiles, but it is not ready to upload until the critical items are closed.

## Critical author decisions

- [ ] Approve the final title. The semantic audit in `docs/feasibility_first_title_decision.md` recommends “Counting Categories, Not Images: Distribution-Free Feasibility Limits for Few-Shot Anomaly Threshold Certification” because the current question “How Many Categories Are Enough?” can be read as promising sufficiency, whereas 14/29/59 are necessary lower limits.
- [x] Final author names, order, affiliations, and corresponding-author email are present.
- [ ] Both authors approve per-author CRediT roles.
- [ ] Both authors confirm originality, exclusive consideration, and approval to submit; then replace the explicit confirmation note in `cover_letter.md`.
- [ ] Both authors confirm the competing-interest declaration.
- [ ] Both authors approve the generative-AI disclosure.
- [ ] Confirm the funding statement and grant numbers, or confirm that no external funding applies.
- [ ] Replace the generic advisor acknowledgement with an approved name, or remove it.

## Bibliography and data attribution

- [ ] Add the MPDD paper by Jezek et al. to `references.bib` and cite it at the first MPDD dataset description.
- [ ] Add primary references for the Clopper--Pearson interval and Hoeffding's inequality, plus an appropriate citation for the classical zero-failure/rule-of-three lineage. The paper already states that the Bernoulli counterexample is elementary and must not imply invention of these statistical primitives.
- [ ] Add Dunn, Wasserman, and Ramdas (2023) on distribution-free prediction sets for two-layer hierarchical models and insert the prepared Related Work comparison; this is the closest precedent for treating categories as exchangeable groups of repeated observations.
- [ ] Recheck and, if still public, cite Salem et al. (arXiv:2607.24562, July 2026) as a recent group-conditional risk-control guardrail; distinguish its known hierarchy nodes from CRESS's new-category transfer question.
- [ ] Recheck whether final MAPR 2026 proceedings metadata for HeAD-CP have appeared. The acceptance note is currently supported by the official MAPR accepted-paper list; until proceedings metadata exist, retain the arXiv record plus the verified acceptance note rather than inventing pages or a DOI.
- [ ] Remove the duplicated/raw UniAD DOI and URL formatting, correct the DINOv2 venue wording, and protect method-name capitalization where needed.
- [ ] Run the final DOI, year, venue, pagination/article-number, and preprint-status audit after the user finishes `references.bib`.
- [ ] Apply the read-only findings in `docs/references_bib_read_only_audit.md`, including removal of the stray malformed SubspaceAD block.
- [ ] Confirm the redistribution terms of every dataset; do not bundle raw dataset images in the release unless the license permits it.

## Figures and release package

- [x] Replace the target-side pipeline placeholder with `fig_target_pipeline.pdf` from `origin/fig:CRESS_ab.pdf`.
- [x] Replace the CRESS pipeline placeholder with `fig_cress_pipeline.pdf` from `origin/fig:CRESS_c.pdf`.
- [ ] In the target-side artwork, show the pixel anomaly map as an inherited optional output, but do not imply that pixel AUROC or localization state of the art is reported by this manuscript; the compiled evidence tables evaluate image-level ranking and alarm reliability.
- [ ] If GPT or another AI tool contributes to either final pipeline figure, disclose the specific tool, version, and use in that figure's caption and extend the general AI declaration. Elsevier's June 2026 policy permits AI-assisted explanatory workflows only with this transparency and author verification.
- [ ] Generate every residual map, anomaly map, heatmap, plot, and other data-derived panel directly from the frozen data/code path. Do not substitute a generative illustration for a research/data image; retain the underlying files and command provenance.
- [x] Check final figure fonts and layout at publication size; both figures remain legible and within the two-column page bounds.
- [x] Add both final pipeline assets to `FIGURES` in `scripts/build_flat_elsevier_submission.py`, remove the placeholder note, and verify them in a clean temporary flat build.
- [x] Align the local repository landing page with the feasibility-first title, claim scope, and paper-facing audit commands.
- [ ] Publish the aligned landing page in the final public snapshot and verify every documented audit from a clean checkout.
- [ ] Commit the feasibility-first manuscript and regenerated tables/figures.
- [ ] Create an immutable review snapshot and verify that both commit links in Code Availability are public.
- [ ] Test the release from a clean checkout and remove private absolute paths from user-facing instructions.
- [ ] Generate a fresh one-directory Editorial Manager package with `scripts/build_flat_elsevier_submission.py`; do not upload the intermediate `submission_flat/`, which is marked stale.
- [ ] Convert the audited `highlights.txt` content to a separate Word document for the final Elsevier upload; the current text file is the controlled source, not the final file format.

## Scientific checks already closed

- [x] Strict nested category and image-unit audits are present.
- [x] Category/image estimands are separated.
- [x] Category units explicitly include their support construction and held-out views; the exchangeable-target statement uses the same complete unit.
- [x] The pooled image-unit model is explicitly labeled an idealized iid sensitivity assumption because the archive is category-stratified and images share support-fitted scorers.
- [x] Distribution-free non-feasibility is restricted to the deterministic uniformly valid procedure class in Proposition 3.
- [x] Proposition 1 is scoped to one fixed target/seed/source-view/condition cell; no grid-wide 95% guarantee is claimed.
- [x] Corollary 1 requires a fresh independent target draw from the same category meta-population; generic exchangeability is not used to justify the Hoeffding transfer statement.
- [x] A dependency-free alignment audit checks the compiled CRESS flow, formulas, split/routing rules, family allocation, fail-closed selection, and frozen grid against the implementation and final CPU configuration.
- [x] A dependency-free aggregation audit distinguishes the 960 gate configurations from their target-category/seed cells, verifies all four strict-CRESS denominators, and prevents the pooled-source bookkeeping copies from being double weighted.
- [x] A dependency-free claim-surface audit traces the rounded values, scope qualifiers, and contribution-to-evidence links printed in the manuscript back to the empirical, theoretical, method-alignment, and aggregation reports; the current report passes all 77 checks.
- [x] DINOv2 preprocessing, exact top-1% aggregation, support nesting, corruption parameters, quantization, source routing, and partition rounding are declared in the compiled paper.
- [x] The strict 120-record label-stratified export is disclosed, and anomalous source rows are explicitly excluded before all CRESS stages.
- [x] `0.463` from the mixed legacy protocol is retired.
- [x] Current target-only results are regenerated from the latest nested five-seed artifacts.
- [x] The pooled CDF audit is descriptive; no invalid iid test is claimed.
- [x] Historical calibration/routing/FGSM/non-independent CRESS evidence is excluded from the compiled manuscript.
- [x] Storage excludes the unused legacy MLP.
- [x] The controlled clean-ranking table is re-aggregated from complete run-level records; the VisA PCA64 `k=8` value is corrected to `0.882/0.894` AUROC/AP.
- [x] AnomalyDINO rows are labeled as values reported by the cited paper, not as a repository-auditable reproduction after the original summary CSVs were removed.
- [x] The unsupported cached-feature latency sentence is removed; the paper limits its efficiency claim to explicitly accounted category-specific storage.
- [x] The aggregation ablation is compiled, its seven-category/three-seed subset is named, and the text does not claim full-dataset invariance to aggregation.
- [x] LaTeX compiles to a 16-page A4 two-column PDF with no undefined citation/reference or content overflow.
- [x] The manuscript uses the CAS template's `cas-model2-names` bibliography style rather than the generic `elsarticle-num` style.
- [x] A CPU audit verifies controlled clean ranking/storage, the complete target-only table, CDF claims, matched-LOIO sensitivity, theory counts, strict CRESS outputs, pooled baseline, and the `k>1` zero-threshold result.
- [x] The same audit verifies 13 manifest inputs, 48 primary strict artifacts, and the empirical gate against SHA-256 hashes; it explicitly retains the recorded post-checkpoint dirty-worktree warning.

## GPU status

No current blocker requires another GPU run. More computation on the same three/four certification categories cannot overcome the analytic category-count limit. New GPU work is justified only together with new independent categories, real-shift data, or a different assumption-backed certification design.
