# Preflight summary — nc_gpu_20260722_e7f1759

Status: **PASS / FULL GPU JOBS NOT STARTED**

## Snapshot and paths

- Repository: `/home/crl/MoME/other/AD`
- Commit: `e7f175990b02aa3cbdb7c92250d57c0272abef9d`
- Local `HEAD` equals `origin/main`; preflight `git status --short` was empty.
- Output: `/home/crl/MoME/other/AD/outputs`
- Scratch: `/home/crl/MoME/other/AD/tmp/ad-neurocomputing`
- Scratch/output filesystem: ext4 `/home`, 1.4 TiB total, 279 GiB available before dataset preparation; 253 GiB available after preparation, with scratch using 26 GiB.
- GPU device: `cuda:0`
- MVTec root: `/home/crl/MoME/other/AD/tmp/ad-neurocomputing/extracted/mvtec`
- VisA root: `/home/crl/MoME/other/AD/tmp/ad-neurocomputing/extracted/visa_raw`
- MPDD root: `/home/crl/MoME/other/AD/tmp/ad-neurocomputing/extracted/mpdd_raw/MPDD`
- Loader mappings: `data/mvtec`, `data/visa`, and `data/mpdd` are explicit symlinks to the roots above.

## Passed gates

- Required Git, GPU, Python, disk, environment, and path probes were logged.
- CPU suite: 98 passed in 2.19 seconds, exit 0.
- Synthetic DINOv2 GPU smoke: patch tensor `(1, 1369, 384)`, finite, exit 0.
- Smoke output is explicitly not paper evidence.
- Full dataset audit: PASS for MVTec AD (5,354 records), VisA (10,821 records), and MPDD (1,346 records).
- Exact classes, split/labels, anomaly masks, root containment, train/evaluation disjointness, and nested support for `k={1,2,4,8}`, seeds `{0,1,2,3,4}` all passed.
- Archive, local license, and split checksums are recorded in `dataset_source_manifest.json` and `dataset_checksums.log`.

## Warnings

- `pip check` exited 1 because an unrelated installed ROS package `generate-parameter-library-py` lacks `typeguard`; the project CPU suite and CUDA smoke passed. The full freeze is logged.
- The local Torch Hub DINOv2 source snapshot has no Git metadata; a complete source-tree SHA-256 and checkpoint SHA-256 are recorded instead.
- Optional xFormers is absent; smoke used the standard attention path.
- The first MPDD assembly was rejected after checksum/CRC failure. Clean independent ranges were downloaded; the accepted archive matches the pinned SHA-256 exactly. Rejected intermediates remain only in ignored scratch for traceability and are not mapped into `data/mpdd`.

No full GPU export, paper analysis, historical-artifact promotion, frozen protocol change, or raw-data redistribution has occurred. Dataset downloads were explicitly authorized by the user and remain only in ignored local scratch.
