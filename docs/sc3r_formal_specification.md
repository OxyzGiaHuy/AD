# SC3R formal specification and claim boundary

Status: design frozen for CPU implementation; numerical evaluation requires the
missing per-image artifacts or a GPU rerun.

## 1. Objects and sampling levels

For target category `t`, support seed `s`, and condition `d`, let
`A_{t,s}` be the detector fitted only to the `k` target-normal support images.
Its image score is the top-`rho` mean of patchwise PCA residuals. The normalized
score is

`z_{c,s,d}(x) = (A_{c,s}(x) - median(R_{c,s})) / max(MAD(R_{c,s}), eps)`,

where `R_{c,s}` contains LOIO support residuals of category `c`. This
normalization is a comparability device, not a proof that categories have the
same distribution.

The hierarchy that must remain visible in all analysis is:

`dataset -> category -> support seed -> base image -> corruption view`.

Corrupted copies of one base image are not independent observations. Multiple
images sharing a source reference pool are also not marginally independent.

## 2. Target-only resolution proposition

**Proposition 1 (attainable-alpha floor).** Let `r_1,...,r_k` be any finite
calibration scores and define

`p(x) = (1 + sum_i 1{r_i >= s(x)}) / (k+1)`.

Then `p(x)` belongs to `{1/(k+1),...,1}`. Consequently the alarm rule
`1{p(x) <= alpha}` is identically zero for every `alpha < 1/(k+1)`.

**Proof.** The exceedance count is an integer in `{0,...,k}`. Substitution into
the numerator gives an integer in `{1,...,k+1}`. Its minimum is therefore
`1/(k+1)`, so no p-value can satisfy a smaller threshold. This is algebraic and
does not require exchangeability. QED.

This proposition explains the operating-point obstruction. It is not by itself
a major algorithmic novelty.

## 3. Why the historical threshold is empirical

The historical code holds each source class out, scores it against all other
source classes, pools the resulting p-values, and selects the largest observed
threshold with pooled empirical FAR at most `alpha`. The same rows are used to
choose and assess the threshold, while folds share overlapping reference pools.
Therefore its reported source FAR is a training diagnostic, not an independent
confidence statement. A pointwise binomial interval added after selection does
not repair adaptive reuse or shared-reference dependence.

## 4. Nested source design

For each target category, exclude the target first and partition the remaining
source categories before looking at certification outcomes:

1. **Reference classes R:** define the source conformal reference pool.
2. **Proposal classes P:** propose a finite candidate set of thresholds.
3. **Certification classes C:** evaluate candidates; never tune normalization,
   candidate count, threshold, condition mode, or fallback using these outcomes.

The candidate set may depend on R and P. If it contains `M` positive thresholds,
certification uses error budget `delta/M` for each candidate (union bound).
Threshold zero is a deterministic no-alarm fallback and needs no estimated
bound because conformal p-values are strictly positive.

To avoid leakage, target anomalies and target normal test images are absent from
all three source stages. The class partition, seeds, candidate cap, `alpha`, and
`delta` must be saved in a manifest before the GPU evaluation.

## 5. Certification units and bounds

For a fixed candidate `tau`, define alarm loss `L_i(tau)=1{p_i <= tau}`. Let
`A` be the number of reported alpha levels. The family error `delta` is divided
over `A` levels, two unit definitions, and `M` candidates.

For independent bounded class units, Hoeffding gives

`E[L(tau)] <= mean(L_i(tau)) + sqrt(log(2*A*M/delta)/(2n))`.

For independent Bernoulli image alarms, the implementation instead uses the
sharper one-sided Clopper--Pearson upper limit at tail probability
`delta/(2*A*M)`. A union bound makes both units, all levels, and all candidates
simultaneous within one target cell with probability at least `1-delta`.

### Category feasibility consequence

Because the empirical class loss is nonnegative, a positive candidate can pass
the Hoeffding gate only if

`n >= log(2*A*M/delta) / (2*alpha^2)`.

This is a necessary, not sufficient, condition. With the frozen `A=3` and
`delta=0.05`, even the most favorable `M=1` case requires at least 60, 240, and
958 independent certification categories for `alpha=0.20`, `0.10`, and `0.05`.
The three or four certification categories available in the frozen MVTec/VisA
splits therefore make every positive category-certified threshold infeasible
under the declared Hoeffding rule before target outcomes are inspected.

Two analyses are required:

- **Image-level fixed-archive analysis:** each distinct base normal image is a
  unit. It estimates average source-mixture image risk, conditional on the fixed
  reference/proposal stages. It is not a new-category guarantee and must not
  duplicate different corruptions of the same image as independent units.
- **Category-level new-category stress test:** each category contributes its mean
  loss in `[0,1]`. This targets a new source-domain category/seed draw under an
  independence/exchangeability assumption across clusters. With few categories
  its bound may be too wide to certify a useful threshold; that outcome must be
  reported.

If cross-seed cells reuse the same images, category—not category/seed—is the
more conservative unit. Both should be reported as a sensitivity analysis. No
choice of unit may be made after seeing which gives the desired conclusion.

## 6. Source and target claims

**Source-domain statement (conditional).** If certification units are
independent draws from the declared population, the simultaneous
Clopper--Pearson/Hoeffding rules bound the selected threshold's fixed-archive
image risk or new-category mean risk, respectively, at confidence `1-delta`.

**Target-transfer statement (stronger assumption required).** The source result
does not imply a bound for a fixed unrelated target category. A target bound
requires an explicit condition such as stochastic dominance

`P_target(p <= tau) <= R_source(tau)`

at the selected threshold, or exchangeability of the target category with the
certification-category meta-distribution. Robust normalization and matched
condition routing make this assumption plausible enough to test; they do not
prove it. MVTec-to-VisA results are empirical stress tests of transfer, not a
distribution-free guarantee.

## 7. Adversarial review record

**Author case.** Nested source certification turns abundant normal archives into
operating points below the target-only resolution floor without target anomaly
labels.

**Reviewer case.** A useful source bound may disappear at the category level;
matched-condition routing assumes condition metadata; target transfer remains
unproved; using pooled images would overstate effective sample size.

**Resolution.** Report the historical empirical SC3R result separately from the
nested certification experiment. Pre-specify both estimands, never relabel an
image-mixture certificate as a new-category certificate, include
clean/pooled/mismatched/blind modes, and call target behavior empirical unless
the transfer assumption is stated.

## 8. Implementation-to-paper rule

The new certification code may be merged and tested on synthetic data now. No
paper table or numeric claim changes until the exact GPU run produces per-image
CSV, class-partition manifest, candidate table, certification bounds, and a
machine-readable environment record. If the nested gate fails, the paper must
retain SC3R as an empirically validated routing method rather than relabeling the
old analysis as a guarantee.
