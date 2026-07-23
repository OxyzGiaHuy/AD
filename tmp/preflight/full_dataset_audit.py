from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import csv
import hashlib
import json
from pathlib import Path

from scripts.generate_benchmark_grid import MVTEC_CLASSES, VISA_CLASSES
from src.data.datasets import load_records
from src.data.sampling import evaluation_records, few_shot_support


EXPECTED_CLASSES = {
    "mvtec": MVTEC_CLASSES,
    "visa": VISA_CLASSES,
    "mpdd": [
        "bracket_black", "bracket_brown", "bracket_white", "connector",
        "metal_plate", "tubes",
    ],
}
LICENSES = {
    "mvtec": ("license.txt", "Attribution-NonCommercial-ShareAlike 4.0"),
    "visa": ("LICENSE-DATASET", "Attribution 4.0"),
    "mpdd": ("LICENSE", "Attribution-NonCommercial-ShareAlike 4.0"),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(8 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def contained(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root)
        return True
    except ValueError:
        return False


def audit_dataset(dataset: str, project_root: Path, out_dir: Path) -> dict:
    configured_root = project_root / "data" / dataset
    resolved_root = configured_root.resolve(strict=True)
    classes = EXPECTED_CLASSES[dataset]
    records = load_records(dataset, configured_root, classes)
    available = sorted(path.name for path in resolved_root.iterdir() if path.is_dir() and (path / "train").is_dir())
    failures: list[str] = []
    if available != sorted(classes):
        failures.append(f"class mismatch: {available}")

    path_counts = Counter(record.path for record in records)
    duplicate_paths = sorted(path for path, count in path_counts.items() if count != 1)
    if duplicate_paths:
        failures.append(f"duplicate record paths: {len(duplicate_paths)}")

    train = [record for record in records if record.split == "train"]
    evaluation = evaluation_records(records)
    if any(record.label != 0 for record in train):
        failures.append("train contains anomaly label")
    path_overlap = sorted(set(record.path for record in train) & set(record.path for record in evaluation))
    if path_overlap:
        failures.append(f"train/test path overlap: {len(path_overlap)}")

    per_class = {}
    for category in classes:
        category_train = [record for record in train if record.category == category]
        category_test = [record for record in evaluation if record.category == category]
        labels = sorted(set(record.label for record in category_test))
        if len(category_train) < 8:
            failures.append(f"{category}: fewer than eight train-normal images")
        if labels != [0, 1]:
            failures.append(f"{category}: test labels are {labels}")
        per_class[category] = {
            "train_normal": len(category_train),
            "test_normal": sum(record.label == 0 for record in category_test),
            "test_anomaly": sum(record.label == 1 for record in category_test),
        }

    missing_images = []
    outside_images = []
    missing_masks = []
    outside_masks = []
    rows = []
    image_hash_splits: dict[str, set[str]] = defaultdict(set)
    for record in records:
        image = Path(record.path)
        if not image.is_file():
            missing_images.append(record.path)
            continue
        if not contained(image, resolved_root):
            outside_images.append(record.path)
        image_hash = sha256(image)
        image_hash_splits[image_hash].add(record.split)
        mask_hash = ""
        if record.label == 1:
            if not record.mask_path or not Path(record.mask_path).is_file():
                missing_masks.append(record.path)
            else:
                mask = Path(record.mask_path)
                if not contained(mask, resolved_root):
                    outside_masks.append(record.mask_path)
                mask_hash = sha256(mask)
        rows.append({
            "dataset": dataset,
            "category": record.category,
            "split": record.split,
            "label": record.label,
            "defect_type": record.defect_type,
            "image_path": record.path,
            "image_bytes": image.stat().st_size,
            "image_sha256": image_hash,
            "mask_path": record.mask_path or "",
            "mask_sha256": mask_hash,
        })
    content_overlap = sorted(digest for digest, splits in image_hash_splits.items() if splits == {"train", "test"})
    for name, values in (
        ("missing images", missing_images),
        ("images outside root", outside_images),
        ("missing anomaly masks", missing_masks),
        ("masks outside root", outside_masks),
        ("train/test content overlap", content_overlap),
    ):
        if values:
            failures.append(f"{name}: {len(values)}")

    support_checks = 0
    support_eval_overlap = []
    nested_failures = []
    evaluation_paths = set(record.path for record in evaluation)
    for seed in range(5):
        supports = {k: set(record.path for record in few_shot_support(records, k, seed)) for k in (1, 2, 4, 8)}
        support_checks += len(supports)
        for lower, upper in ((1, 2), (2, 4), (4, 8)):
            if not supports[lower] <= supports[upper]:
                nested_failures.append((seed, lower, upper))
        for k, paths in supports.items():
            overlap = paths & evaluation_paths
            if overlap:
                support_eval_overlap.extend((seed, k, path) for path in sorted(overlap))
    if nested_failures:
        failures.append(f"nested support failures: {len(nested_failures)}")
    if support_eval_overlap:
        failures.append(f"support/evaluation overlap: {len(support_eval_overlap)}")

    license_name, license_marker = LICENSES[dataset]
    license_path = resolved_root / license_name
    license_ok = license_path.is_file() and license_marker in license_path.read_text(encoding="utf-8", errors="replace")
    if not license_ok:
        failures.append(f"license marker missing: {license_name}")

    csv_path = out_dir / f"dataset_files_{dataset}.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    counts = Counter((r.category, r.split, r.label, bool(r.mask_path)) for r in records)
    return {
        "dataset": dataset,
        "status": "PASS" if not failures else "FAIL",
        "configured_root": str(configured_root),
        "resolved_root": str(resolved_root),
        "class_count": len(classes),
        "record_count": len(records),
        "available_classes": available,
        "per_class": per_class,
        "counts": [
            {"category": key[0], "split": key[1], "label": key[2], "has_mask": key[3], "count": value}
            for key, value in sorted(counts.items())
        ],
        "missing_anomaly_masks": len(missing_masks),
        "train_test_path_overlap": len(path_overlap),
        "train_test_content_overlap": len(content_overlap),
        "support_evaluation_overlap": len(support_eval_overlap),
        "nested_support_checks": support_checks,
        "nested_support_failures": len(nested_failures),
        "license_path": str(license_path),
        "license_sha256": sha256(license_path) if license_path.is_file() else None,
        "license_marker_ok": license_ok,
        "file_manifest": str(csv_path),
        "file_manifest_sha256": sha256(csv_path),
        "failures": failures,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", type=Path, default=Path.cwd())
    parser.add_argument("--datasets", nargs="+", choices=sorted(EXPECTED_CLASSES), required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    audits = [audit_dataset(dataset, args.project_root.resolve(), args.out_dir) for dataset in args.datasets]
    payload = {"overall_status": "PASS" if all(item["status"] == "PASS" for item in audits) else "FAIL", "datasets": audits}
    args.out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    return 0 if payload["overall_status"] == "PASS" else 4


if __name__ == "__main__":
    raise SystemExit(main())
