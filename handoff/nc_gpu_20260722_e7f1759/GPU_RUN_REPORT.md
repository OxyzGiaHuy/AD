# GPU Run Report — `nc_gpu_20260722_e7f1759`

## 1. Executive status

Scientific execution status: **complete**.

Submission-package status: **partial**. All frozen P0–P7 computations, artifact
audits, transfers, ablations, simultaneous comparisons, and the final CPU
pipeline completed. The separate manuscript/package gate returned exit code 1
for author/repository placeholders and manuscript packaging issues listed in
Section 10. No failed package check was hidden or changed by hand.

The frozen scientific protocol was not changed.

## 2. Commit, environment, GPU, and datasets

- Frozen run commit: `e7f175990b02aa3cbdb7c92250d57c0272abef9d`.
- First artifact checkpoint: `07d8031`.
- Complete handoff artifact commit: `8369ffe`.
- Repository: `/home/crl/MoME/other/AD`.
- Python: 3.10.20.
- PyTorch: 2.12.1+cu130.
- torchvision: 0.27.1+cu130.
- PyTorch CUDA: 13.0.
- cuDNN: 92000.
- NVIDIA driver: 580.126.09.
- GPU: NVIDIA GeForce RTX 5090, 32607 MiB, compute capability 12.0.
- DINOv2: `dinov2_vits14`, image size 518.
- DINOv2 source-tree SHA-256:
  `fd85b105a21d0b9fce4377f915a97a330661893f5dbb97846373bbe99520dd65`.
- DINOv2 weight SHA-256:
  `b938bf1bc15cd2ec0feacfe3a1bb553fe8ea9ca46a7e1d8d00217f29aef60cd9`.

Resolved dataset mappings:

- `data/mvtec` → `/home/crl/MoME/other/AD/tmp/ad-neurocomputing/extracted/mvtec`
- `data/visa` → `/home/crl/MoME/other/AD/tmp/ad-neurocomputing/extracted/visa_raw`
- `data/mpdd` → `/home/crl/MoME/other/AD/tmp/ad-neurocomputing/extracted/mpdd_raw/MPDD`

The full dataset audit passed for MVTec AD (5,354 records), VisA (10,821
records), and MPDD (1,346 records). Raw datasets are not included in this
handoff.

## 3. Commands and phase exit status

Exact commands, timestamps, stdout/stderr, and exit codes are under `logs/`.

| Phase | Result |
|---|---|
| Preflight and P0 lineage audit | Complete |
| P1 MVTec/VisA SC3R export | Complete; artifact audits pass |
| P2 matched LOIO export | MVTec 750/750 and VisA 600/600; exit 0 |
| P2 clustered diagnostics | `class seed` and `class` sensitivity complete for both datasets |
| P3 historical empirical reproduction | Complete; lineage-only |
| P4 strict nested SC3R | Complete |
| P5 routing modes | Complete |
| P6 final CPU pipeline | Complete; exit 0 |
| P7 MPDD export/audit/LOIO | Complete; audit pass |
| P7 MVTec-to-MPDD transfer | Complete; exit 0 |
| Submission package gate | Failed with documented non-scientific blockers |

Operational thread caps and CPU affinity were used to remove OpenBLAS
oversubscription. They changed scheduling only, not the frozen grid,
estimands, seeds, corruptions, thresholds, or algorithms.

## 4. Artifact audit results

- MVTec: pass; 1,500 view cells, 156,100 view rows, 300 statistic rows,
  1,125 support rows.
- VisA: pass; 1,200 view cells, 144,000 view rows, 240 statistic rows,
  900 support rows.
- MPDD: pass; 600 view cells, 45,800 view rows, 120 statistic rows,
  450 support rows.
- CPU pipeline manifest artifact audits: MVTec, VisA, and MPDD all `pass`.
- Final CPU pipeline: 192 declared runs and 585 output artifacts.

## 5. Empirical gate results

The zero-preserving empirical gate contains 960 cells:

- empirical pass: 0;
- empirical fail: 960;
- required minimum nonzero-threshold rate: 0.8.

This is a negative result and must be reported as such. It is an empirical
target gate, not a target-domain validity certificate. No pooled mean may be
used to hide zero thresholds or failed cells.

## 6. Category versus image certificate

Category-level Hoeffding certification and fixed-archive image-level
Clopper–Pearson certification target different estimands. Image-level results
must not be presented as substitutes for failed or underpowered new-category
certification. The 0/960 empirical gate outcome is retained.

## 7. Matched versus condition-agnostic boundary

`matched_condition` uses condition metadata and is the metadata-assisted
operational mode. `condition_agnostic` is the blind pooled deployment mode.
`mismatched_condition` remains a deterministic negative control. Claims must
be limited to the mode supported by its own per-cell results.

## 8. Few-shot caveat

The primary grid includes `k={1,2,4,8}` and seeds `{0,1,2,3,4}`. For `k=1`,
the metadata is `patch_split_conformal`; it is not image-level LOIO. Results
for `k=1,2` remain in the main artifacts and were not relegated or removed.

## 9. Transfer boundaries

- MVTec-to-VisA strict transfer completed.
- MVTec-to-MPDD strict transfer completed with 10,800 result rows, 71,958
  candidate rows, and 600 partition manifests.
- Within-MPDD is empirical replication only because MPDD has too few classes
  for the strong primary three-way nested category split.
- MPDD did not tune `rho`, PCA dimension, corruption severity, candidate cap,
  alpha, or delta.

## 10. Negative results, deviations, and unresolved blockers

Scientific negative result:

- all 960 empirical gate cells fail the declared operational gate.

Recorded environment warning:

- `pip check` reports an unrelated ROS package missing `typeguard`; 98 CPU
  tests and the synthetic DINOv2 CUDA smoke passed.
- xFormers is unavailable; the standard attention path was used.

Submission-package blockers from the final gate:

- placeholder author;
- placeholder repository;
- generic TODO;
- missing `author_biographies.md`;
- missing author passport-type photographs;
- duplicate PDF anchor warnings caused by empty author placeholders;
- the CPU manifest recorded a dirty worktree.

Personal author metadata was intentionally not invented. The CPU manifest was
not edited by hand to conceal its recorded Git state.

The manuscript was rebuilt successfully with Tectonic and `main.log` was
retained. Generated `main.abs` was moved to
`/tmp/ad_nc_gpu_20260722_e7f1759_generated/main.abs` and can be recovered from
there. The remaining empty-anchor warnings occur at the placeholder author
line and cannot be resolved without real author metadata.

## 11. Exact paths to copy

- CPU manifest:
  `outputs/submission_cpu/cpu_pipeline_manifest_nc_gpu_20260722_e7f1759.json`
- Empirical gate:
  `outputs/submission_cpu/nested_sc3r_nc_gpu_20260722_e7f1759_empirical_gate.json`
- Simultaneous comparisons:
  `outputs/submission_cpu/sc3r_confirmatory_simultaneous_nc_gpu_20260722_e7f1759.csv`
- Paired cells:
  `outputs/submission_cpu/nested_sc3r_nc_gpu_20260722_e7f1759_paired_cells.csv`
- Summary:
  `outputs/submission_cpu/nested_sc3r_nc_gpu_20260722_e7f1759_summary.csv`
- GPU/LOIO/transfer tables: `outputs/paper_tables/`
- Dataset/support/audit manifests:
  `outputs/manifests/nc_gpu_20260722_e7f1759/`
- Exact command logs: `logs/nc_gpu_20260722_e7f1759/`
- Final pipeline config: `configs/submission_cpu_pipeline.final.json`
- Package audit: `outputs/submission_audit_nc_gpu_20260722_e7f1759.json`
- Handoff checksum: `handoff/nc_gpu_20260722_e7f1759/SHA256SUMS`

The handoff uses relative symlinks for the large derived-artifact directories
to avoid duplicating approximately 6.5 GiB. Raw datasets, feature caches, and
temporary corrupted images are excluded.
