from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

from src.data import evaluation_records, few_shot_support, load_records


PROJECT_ROOT = Path("/home/crl/MoME/other/AD")
OUTPUT = PROJECT_ROOT / "outputs/manifests/nc_gpu_20260722_e7f1759/dataset_audit_full.json"
EXPECTED_CLASSES = {
    "mvtec": [
        "bottle", "cable", "capsule", "carpet", "grid", "hazelnut",
        "leather", "metal_nut", "pill", "screw", "tile", "toothbrush",
        "transistor", "wood", "zipper",
    ],
    "visa": [
        "candle", "capsules", "cashew", "chewinggum", "fryum",
        "macaroni1", "macaroni2", "pcb1", "pcb2", "pcb3", "pcb4",
        "pipe_fryum",
    ],
    "mpdd": [
        "bracket_black", "bracket_brown", "bracket_white", "connector",
        "metal_plate", "tubes",
    ],
}
EXPECTED_TOTALS = {"mvtec": 5354, "visa": 10821, "mpdd": 1346}
KS = (1, 2, 4, 8)
SEEDS = range(5)


def inside(path: Path, root: Path) -> bool:
    try:
        path.resolve(strict=True).relative_to(root)
    except (FileNotFoundError, ValueError):
        return False
    return True


def audit_dataset(dataset: str) -> dict[str, object]:
    configured_root = PROJECT_ROOT / "data" / dataset
    resolved_root = configured_root.resolve(strict=True)
    expected_classes = EXPECTED_CLASSES[dataset]
    records = load_records(dataset, configured_root, "all")
    discovered_classes = sorted({record.category for record in records})
    by_class: dict[str, Counter[str]] = defaultdict(Counter)
    for record in records:
        key = f"{record.split}_{'anomaly' if record.label else 'normal'}"
        by_class[record.category][key] += 1
        by_class[record.category]["total"] += 1

    image_paths = [Path(record.path) for record in records]
    train_paths = {record.path for record in records if record.split == "train"}
    evaluation = evaluation_records(records)
    evaluation_paths = {record.path for record in evaluation}
    anomaly_records = [record for record in records if record.label == 1]
    missing_masks = [record.path for record in anomaly_records if not record.mask_path or not Path(record.mask_path).is_file()]
    outbound_images = [str(path) for path in image_paths if not inside(path, resolved_root)]
    outbound_masks = [
        record.mask_path for record in anomaly_records
        if record.mask_path and not inside(Path(record.mask_path), resolved_root)
    ]
    symlinks = [path for path in resolved_root.rglob("*") if path.is_symlink()]
    outbound_symlinks = [str(path) for path in symlinks if not inside(path, resolved_root)]

    checks: dict[str, bool] = {
        "classes_exact": discovered_classes == expected_classes,
        "total_exact": len(records) == EXPECTED_TOTALS[dataset],
        "all_images_exist": all(path.is_file() for path in image_paths),
        "all_images_inside_root": not outbound_images,
        "all_anomaly_masks_exist": not missing_masks,
        "all_masks_inside_root": not outbound_masks,
        "no_outbound_symlinks": not outbound_symlinks,
        "train_test_paths_disjoint": train_paths.isdisjoint(evaluation_paths),
        "train_only_normal": all(record.label == 0 for record in records if record.split == "train"),
        "evaluation_only_test": all(record.split == "test" for record in evaluation),
        "each_class_has_8_train_normal": all(
            by_class[category]["train_normal"] >= 8 for category in expected_classes
        ),
        "each_class_has_test_normal_and_anomaly": all(
            by_class[category]["test_normal"] > 0 and by_class[category]["test_anomaly"] > 0
            for category in expected_classes
        ),
    }

    support_audit: dict[str, object] = {}
    support_ok = True
    for seed in SEEDS:
        supports = {k: few_shot_support(records, k=k, seed=seed) for k in KS}
        supports_repeat = {k: few_shot_support(records, k=k, seed=seed) for k in KS}
        sets = {k: {record.path for record in supports[k]} for k in KS}
        seed_checks = {
            "deterministic": supports == supports_repeat,
            "exact_sizes": all(len(supports[k]) == k * len(expected_classes) for k in KS),
            "train_normal_only": all(
                record.split == "train" and record.label == 0
                for k in KS for record in supports[k]
            ),
            "support_evaluation_disjoint": all(sets[k].isdisjoint(evaluation_paths) for k in KS),
            "nested": sets[1] < sets[2] < sets[4] < sets[8],
        }
        support_ok &= all(seed_checks.values())
        support_audit[str(seed)] = {
            "checks": seed_checks,
            "paths": {str(k): sorted(sets[k]) for k in KS},
        }
    checks["few_shot_support_invariants"] = support_ok

    return {
        "configured_root": str(configured_root),
        "resolved_root": str(resolved_root),
        "expected_classes": expected_classes,
        "discovered_classes": discovered_classes,
        "total_records": len(records),
        "expected_total_records": EXPECTED_TOTALS[dataset],
        "counts": {category: dict(by_class[category]) for category in expected_classes},
        "aggregate_counts": dict(Counter(
            f"{record.split}_{'anomaly' if record.label else 'normal'}" for record in records
        )),
        "anomaly_records": len(anomaly_records),
        "missing_masks": missing_masks,
        "outbound_images": outbound_images,
        "outbound_masks": outbound_masks,
        "symlink_count_below_resolved_root": len(symlinks),
        "outbound_symlinks": outbound_symlinks,
        "checks": checks,
        "support_audit": support_audit,
        "status": "PASS" if all(checks.values()) else "FAIL",
    }


def main() -> int:
    report = {
        "run_tag": "nc_gpu_20260722_e7f1759",
        "git_commit": "e7f175990b02aa3cbdb7c92250d57c0272abef9d",
        "scope": "metadata_and_path_integrity_no_image_modification",
        "datasets": {dataset: audit_dataset(dataset) for dataset in EXPECTED_CLASSES},
    }
    report["status"] = "PASS" if all(
        item["status"] == "PASS" for item in report["datasets"].values()
    ) else "FAIL"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": report["status"],
        "output": str(OUTPUT),
        "datasets": {
            name: {
                "status": item["status"],
                "resolved_root": item["resolved_root"],
                "total_records": item["total_records"],
                "aggregate_counts": item["aggregate_counts"],
                "checks": item["checks"],
            }
            for name, item in report["datasets"].items()
        },
    }, indent=2, sort_keys=True))
    return 0 if report["status"] == "PASS" else 4


if __name__ == "__main__":
    raise SystemExit(main())
