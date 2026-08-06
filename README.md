# Distribution-Free Certification Limits for Few-Shot Anomaly Thresholds

Research code, frozen evaluation records, and LaTeX sources for the manuscript
**“How Many Categories Are Enough? Distribution-Free Certification Limits for
Few-Shot Anomaly Thresholds.”**

The study separates anomaly ranking from threshold reliability. It audits a
frozen DINOv2/PCA residual ranker, target-only leave-one-image-out rank values,
and source-assisted threshold certification under an explicit iid category-unit model.
Its central result is a feasibility boundary: with only three or four
certification categories, the frozen category-level protocol cannot certify a
positive threshold at the tested risk levels. Under an explicitly idealized
iid model, image-unit sensitivity analyses target a different source-mixture
estimand and are not interpreted as new-category certificates; the stratified
archive itself does not establish pooled-image independence.

The family-wise confidence statement applies within a fixed target, seed,
source-view mode, and condition cell, not simultaneously over the complete
experimental grid. The strict score export is capped by deterministic
label-stratified evaluation sampling; all anomalous source rows are discarded
before reference mapping, threshold proposal, or certification.

## Manuscript

The feasibility-first manuscript is in
`els-cas-templates-feasibility-first/`. It uses Elsevier's double-column CAS
class. The two pipeline figures remain intentional placeholders until the final
artwork is supplied; `submission_flat/` is stale and must not be uploaded.

Build the current manuscript with:

```bash
cd els-cas-templates-feasibility-first
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

## Reproduce the paper-facing audits

Run these commands from the repository root. The full core audit reads the
frozen run records and primary result artifacts, verifies their recorded
SHA-256 hashes, and regenerates the paper-facing consistency report.

```bash
UV_CACHE_DIR=/tmp/uv-cache-feasibility \
  uv run --offline --no-project --with numpy --with pandas \
  scripts/audit_feasibility_first_core_claims.py \
  --output outputs/paper_tables/feasibility_first_core_claim_audit.json

python3 scripts/audit_feasibility_first_manuscript.py \
  --root els-cas-templates-feasibility-first \
  --output outputs/paper_tables/feasibility_first_manuscript_audit.json

python3 scripts/audit_feasibility_first_method_alignment.py \
  --output outputs/paper_tables/feasibility_first_method_alignment_audit.json

python3 scripts/audit_feasibility_first_table_aggregations.py \
  --root . \
  --manuscript els-cas-templates-feasibility-first \
  --output outputs/paper_tables/feasibility_first_table_aggregation_audit.json

python3 scripts/audit_feasibility_first_claim_surface.py \
  --root . \
  --manuscript els-cas-templates-feasibility-first \
  --output outputs/paper_tables/feasibility_first_claim_surface_audit.json

python3 scripts/audit_feasibility_first_core_claims.py \
  --theory-only \
  --output outputs/paper_tables/feasibility_first_theory_claim_audit.json
```

The frozen records deliberately retain their declared protocol revisions,
source-tree and weight hashes, and recorded worktree state. A passing integrity
audit establishes consistency with those records; it does not turn the
conditional source-domain result into unconditional target-category control.

Detailed claim lineage and remaining author-confirmation items are documented
in:

- `docs/feasibility_first_submission_progress.md`
- `docs/submission_blockers.md`
- `docs/feasibility_first_mock_review.md`

## Experiment scaffold

The repository also retains the experiment CLIs used during development:

```bash
python -m src.run_experiment --config configs/experiments/headpca_mvtec.yaml
python -m src.extract_features --dataset mvtec --root /path/to/mvtec --k-shot 4
python -m src.evaluate_robustness --run-id <run_id> --attack fgsm --epsilon 8/255
```

These development commands cover a broader historical scaffold than the
evidence compiled in the feasibility-first manuscript. Only results included in
the frozen paper-facing audit are used as manuscript evidence.

## Dataset setup

Large datasets can be stored outside the repository and linked into `data/`:

```bash
python scripts/download_datasets.py --dataset visa --download-root /tmp/AD-data

# MVTec requires accepting its official terms and supplying the download URL.
python scripts/download_datasets.py --dataset mvtec \
  --mvtec-url "<official-mvtec-url>" --download-root /tmp/AD-data
```

Do not redistribute raw dataset images without confirming their licenses.

## Tests

```bash
python -m pytest -q
# If unrelated globally installed pytest plugins interfere:
scripts/run_tests.sh
```

## Outputs and provenance

Experiment runs may write `metrics.json`, prediction tables, anomaly maps, and
run notes under `docs/experiments/`. The manuscript audit consumes only the
declared frozen inputs. Historical exploratory outputs are retained for
traceability but are not automatically scientific evidence for the paper.
