from __future__ import annotations

import os
from pathlib import Path


PROJECT_ROOT = Path("/home/crl/MoME/other/AD")
EXPECTED = {
    "mvtec": (
        "bottle/train/good",
        [
            "bottle", "cable", "capsule", "carpet", "grid", "hazelnut",
            "leather", "metal_nut", "pill", "screw", "tile", "toothbrush",
            "transistor", "wood", "zipper",
        ],
    ),
    "visa": (
        "split_csv/1cls.csv",
        [
            "candle", "capsules", "cashew", "chewinggum", "fryum",
            "macaroni1", "macaroni2", "pcb1", "pcb2", "pcb3", "pcb4",
            "pipe_fryum",
        ],
    ),
    "mpdd": (
        "bracket_black/train/good",
        [
            "bracket_black", "bracket_brown", "bracket_white", "connector",
            "metal_plate", "tubes",
        ],
    ),
}


def main() -> int:
    print("audit_scope=metadata_only")
    print("raw_data_downloaded=False")
    print("raw_data_modified=False")
    print("raw_data_redistributed=False")
    missing = []
    for dataset, (signature, classes) in EXPECTED.items():
        root = PROJECT_ROOT / "data" / dataset
        print(f"{dataset}.configured_root={root}")
        print(f"{dataset}.expected_classes={','.join(classes)}")
        print(f"{dataset}.expected_signature={signature}")
        print(f"{dataset}.root_exists={root.is_dir()}")
        print(f"{dataset}.signature_exists={(root / signature).exists()}")
        if not root.is_dir() or not (root / signature).exists():
            missing.append(dataset)
            print(f"{dataset}.audit_status=BLOCKED_MISSING_ROOT")
            print(f"{dataset}.counts_split_masks=NOT_RUN")
            print(f"{dataset}.support_evaluation_overlap=NOT_RUN")
            print(f"{dataset}.local_license_verification=NOT_RUN")
    print("missing_datasets=" + ",".join(missing))
    print("overall_dataset_audit=" + ("PASS" if not missing else "BLOCKED"))
    return 0 if not missing else 3


if __name__ == "__main__":
    raise SystemExit(main())
