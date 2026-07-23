# Dataset audit preflight

- Initial status: **BLOCKED — missing all three dataset roots**.
- Current status: **RESOLVED / FULL AUDIT PASS** after explicit user authorization to search for and download all three datasets.
- Raw data was downloaded and extracted only into ignored local scratch; it was not modified or redistributed.

## Frozen expected layouts

- MVTec AD: 15 classes; `<root>/<class>/{train/good,test/*,ground_truth/*}`.
- VisA: 12 classes; `<root>/split_csv/1cls.csv` plus every referenced image and mask.
- MPDD: `bracket_black`, `bracket_brown`, `bracket_white`, `connector`, `metal_plate`, `tubes` in an MVTec-like layout.

## Completed checks

- Exact loader totals: MVTec 5,354; VisA 10,821; MPDD 1,346.
- Every class has at least eight train-normal images, no train anomaly label, and both normal/anomaly labels in test.
- Every anomaly record has an existing mask under its resolved dataset root.
- All image/mask paths are contained in the intended root; no outbound symlink was found; train and evaluation paths are disjoint.
- Deterministic nested support and support/evaluation disjointness passed for every dataset, seed `{0,1,2,3,4}`, and `k={1,2,4,8}`.
- Archive, split, license, source revision, and download provenance are recorded in `dataset_source_manifest.json` and `dataset_checksums.log`.

Machine-readable per-class counts, checks, and exact support paths are in `dataset_audit_full.json`. Full jobs have not been started pending the requested preflight report checkpoint.
