# Mock reviews at the CPU-complete checkpoint

Date: 2026-07-22

Verdict at this checkpoint: **not ready to submit**. The method, audit code, and
claim boundaries are substantially stronger, but the displayed historical
numbers do not evaluate the new nested method. A submission before the frozen
GPU run would contain a method/evidence mismatch.

## Mock editor review — Neurocomputing

### Positive case

- The paper addresses reliability of a learning-system deployment rather than
  presenting only another anomaly-ranking model.
- The attainable-alpha obstruction is clear, and SC3R is a concrete response.
- The manuscript now distinguishes ranking, probability calibration, and
  operational false-alarm behavior.
- Two-column LaTeX, abstract length, keywords, highlights, numbered references,
  CRediT, declarations, and vector figures align with the current author guide.

### Desk-reject risks

1. The current Results tables are historical, whereas Method now specifies
   independent reference/proposal/certification partitions. This is a critical
   evidence mismatch until the nested run is complete.
2. The contribution could look diffuse because calibrators, corruption audits,
   FGSM, selective risk, and SC3R compete for attention. Final Results must lead
   with the strict SC3R gate and move noncentral diagnostics to supplementary
   material if length or focus becomes a problem.
3. Author metadata, biographies/photos, a reviewer-accessible immutable code
   snapshot, and final artifact identifiers remain absent.

### Editorial gate

Send for review only if category-level nested results, mandatory k=1/2,
condition-agnostic routing, a direct pooled-source baseline, and external MPDD
evidence (or a transparent negative result) are present and traceable.

## Mock reviewer A — conformal inference and statistics

### Strongest contribution

Proposition 1 exactly identifies the finite-grid floor without invoking
exchangeability. Proposition 2 correctly conditions on reference/proposal data
and uses a union bound over candidates. The target corollary explicitly adds a
stronger dominance or category-exchangeability assumption.

### Major concerns

1. With few certification classes, the class-level Hoeffding bound may be
   vacuous. The exact image-level Clopper--Pearson result targets the fixed
   source-image mixture and is not a substitute for a new-category statement.
   Every zero-threshold cell must remain in the result table.
2. LOIO calibration and full-support test scoring are asymmetric. The paper now
   calls LOIO approximate, but final wording must not let generic conformal
   validity language imply that Eq. (6) itself is finite-sample valid.
3. Source certification does not establish the target dominance condition.
   MVTec-to-VisA or MVTec-to-MPDD is empirical transfer evidence only.
4. Repeated images across corruption views and seeds invalidate image-iid
   inference. The artifact audit checks corruption identity; category-level
   analysis must remain primary.
5. Confirmatory intervals must use the single declared family. Pointwise
   intervals can appear only as sensitivity results.

### Statistical acceptance gate

- Exact R/P/C manifests and all candidate UCBs are released.
- Category and image units are both reported with distinct estimands; category
  is primary only for a new-category interpretation.
- Bonferroni family size and adjusted interval alpha are visible.
- Pooled-source and randomized conformal baselines use identical target images.
- Failed cells and heavy-corruption exceptions are not pooled away.

## Mock reviewer B — industrial anomaly detection

### Strongest contribution

The paper treats an operational issue that AUROC-centric few-shot AD papers
often omit: whether a threshold retains a useful false-alarm interpretation
under scarce normal support and corruption shift. Storage accounting and
separation from the inherited DINOv2 ranking mechanism are useful.

### Major concerns

1. Matched-condition routing assumes condition metadata and is not a realistic
   default. Condition-agnostic median pooling must be evaluated as the primary
   deployment-facing mode; matched routing is an oracle/metadata-assisted mode.
2. Results at k=4/8 alone are insufficient for a paper framed as few-shot.
   k=1 must be labeled patch-split rather than image-level LOIO, and k=2 must be
   included in the main evidence.
3. MVTec and VisA are closely related benchmark ecosystems. MVTec-to-MPDD is
   needed for stronger external validity; MPDD's six classes prevent pretending
   that within-MPDD nested certification has adequate category count.
4. Controlled memory-bank and subspace rows must remain distinct from official
   PatchCore/AnomalyDINO reproductions. The direct pooled-source conformal
   baseline should receive the full source pool to avoid a strawman comparison.
5. Synthetic corruptions do not establish robustness to real acquisition shift
   or adversarial attacks. The final conclusion must retain this boundary.

### AD acceptance gate

- Full class lists, exact dataset versions/licenses, image counts, support
  manifests, and sampling checksums are released.
- Same target images, prevalence, backbone features, k, seed, and corruption
  views are used across methods.
- Source-class/image-count, normalization, candidate-cap, and split-allocation
  ablations are reported as exploratory sensitivity analyses.
- Runtime includes source archive size, threshold certification time, and
  per-image p-value overhead on the declared server.

## Resolution status

| Concern | CPU resolution | Remaining evidence |
|---|---|---|
| Adaptive reuse in historical SC3R | Nested R/P/C code and Proposition 2 | GPU-exported nested results |
| Target overclaim | Conditional corollary and restrained prose | Empirical transfer only |
| Few-shot p-value floor | Proposition 1 and tests | None |
| Pooled-source strawman | Full-pool baseline implemented | Run on immutable artifacts |
| Dependence/multiplicity | Category unit, paired identities, Bonferroni family | Final CSV and failures |
| Condition knowledge | Blind/pooled and mismatch modes implemented | Run and compare |
| k=1/2 omission | Export/runbook and metadata rules implemented | GPU run |
| External validity | MPDD loader/protocol implemented | Download audit and GPU run |
| Reproducibility | One-command CPU pipeline and SHA-256 manifest | Clean committed GPU snapshot |
| Submission hygiene | Fail-closed package audit | Author/repository inputs |
