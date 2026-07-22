from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence


_IMAGE_SUFFIXES = {".bmp", ".jpeg", ".jpg", ".png", ".tif", ".tiff", ".webp"}


@dataclass(frozen=True, slots=True)
class ImageRecord:
    """One benchmark image and its metadata.

    ``defect_type`` deliberately precedes ``mask_path`` to preserve the
    positional constructor used by the original evaluation scripts.
    """

    path: str
    label: int
    split: str
    category: str
    defect_type: str = "good"
    mask_path: str | None = None


def _normalise_classes(classes: str | Sequence[str], available: Iterable[str]) -> list[str]:
    discovered = sorted(set(available))
    if classes == "all" or (not isinstance(classes, str) and list(classes) == ["all"]):
        if not discovered:
            raise ValueError("No dataset classes were discovered.")
        return discovered
    selected = [classes] if isinstance(classes, str) else [str(item) for item in classes]
    missing = sorted(set(selected) - set(discovered))
    if missing:
        raise ValueError(f"Requested classes are absent from the dataset: {missing}")
    return selected


def _images(directory: Path) -> list[Path]:
    if not directory.is_dir():
        return []
    return sorted(path for path in directory.rglob("*") if path.is_file() and path.suffix.lower() in _IMAGE_SUFFIXES)


def _mask_for_mvtec(class_root: Path, defect: str, image: Path) -> str | None:
    mask_dir = class_root / "ground_truth" / defect
    candidates = [
        mask_dir / f"{image.stem}_mask{image.suffix}",
        mask_dir / f"{image.stem}_mask.png",
        mask_dir / image.name,
    ]
    for candidate in candidates:
        if candidate.is_file():
            return str(candidate.resolve())
    return None


def _scan_mvtec_like(root: Path, classes: str | Sequence[str]) -> list[ImageRecord]:
    available = [path.name for path in root.iterdir() if path.is_dir() and (path / "train").is_dir()]
    selected = _normalise_classes(classes, available)
    records: list[ImageRecord] = []
    for category in selected:
        class_root = root / category
        for image in _images(class_root / "train" / "good"):
            records.append(ImageRecord(str(image.resolve()), 0, "train", category))
        test_root = class_root / "test"
        if test_root.is_dir():
            for defect_dir in sorted(path for path in test_root.iterdir() if path.is_dir()):
                is_normal = defect_dir.name.lower() in {"good", "normal"}
                for image in _images(defect_dir):
                    records.append(
                        ImageRecord(
                            str(image.resolve()),
                            0 if is_normal else 1,
                            "test",
                            category,
                            "good" if is_normal else defect_dir.name,
                            None if is_normal else _mask_for_mvtec(class_root, defect_dir.name, image),
                        )
                    )
    return records


def _first_present(row: dict[str, str], names: Sequence[str]) -> str:
    lowered = {str(key).strip().lower(): (value or "").strip() for key, value in row.items()}
    for name in names:
        if lowered.get(name):
            return lowered[name]
    return ""


def _resolve_csv_path(root: Path, value: str) -> Path:
    value = value.replace("\\", "/")
    candidate = Path(value)
    if candidate.is_absolute():
        return candidate
    attempts = [root / candidate, root.parent / candidate]
    if value.startswith("../"):
        attempts.insert(0, root / value)
    for attempt in attempts:
        resolved = attempt.resolve()
        if resolved.exists():
            return resolved
    return attempts[0].resolve()


def _find_visa_csv(root: Path) -> Path | None:
    candidates = [root / "split_csv" / "1cls.csv", root / "1cls.csv", root.parent / "split_csv" / "1cls.csv"]
    return next((path for path in candidates if path.is_file()), None)


def _scan_visa_csv(root: Path, csv_path: Path, classes: str | Sequence[str]) -> list[ImageRecord]:
    with csv_path.open(newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))
    parsed: list[tuple[dict[str, str], str]] = []
    for row in rows:
        category = _first_present(row, ("object", "class", "category"))
        if category:
            parsed.append((row, category))
    selected = set(_normalise_classes(classes, (category for _, category in parsed)))
    records: list[ImageRecord] = []
    for row, category in parsed:
        if category not in selected:
            continue
        image_value = _first_present(row, ("image", "image_path", "img_path", "path"))
        if not image_value:
            raise ValueError(f"VisA CSV row has no image path: {row}")
        split_value = _first_present(row, ("split", "set", "phase")).lower()
        split = "train" if split_value.startswith("train") else "test"
        label_value = _first_present(row, ("label", "anomaly", "is_anomaly")).lower()
        is_normal = label_value in {"0", "false", "good", "normal", "negative"}
        label = 0 if is_normal else 1
        defect = "good" if label == 0 else _first_present(row, ("defect_type", "defect", "type")) or "bad"
        mask_value = _first_present(row, ("mask", "mask_path", "ground_truth"))
        mask_path = str(_resolve_csv_path(root, mask_value)) if label == 1 and mask_value else None
        image_path = _resolve_csv_path(root, image_value)
        if not image_path.is_file():
            raise FileNotFoundError(f"VisA image listed in {csv_path} does not exist: {image_path}")
        records.append(ImageRecord(str(image_path), label, split, category, defect, mask_path))
    return sorted(records, key=lambda rec: (rec.category, rec.split, rec.label, rec.defect_type, rec.path))


def synthetic_records(category: str = "synthetic", count: int = 12) -> list[ImageRecord]:
    """Create deterministic metadata-only records for smoke tests.

    ``count`` is the number of examples in each of the train-normal,
    test-normal, and test-anomaly partitions. The identity backbone hashes the
    paths, so no image files are needed.
    """

    if count < 1:
        raise ValueError("Synthetic count must be positive.")
    records = [ImageRecord(f"synthetic/{category}/train/good/{idx:04d}.png", 0, "train", category) for idx in range(count)]
    records.extend(ImageRecord(f"synthetic/{category}/test/good/{idx:04d}.png", 0, "test", category) for idx in range(count))
    records.extend(ImageRecord(f"synthetic/{category}/test/defect/{idx:04d}.png", 1, "test", category, "defect") for idx in range(count))
    return records


def load_records(
    dataset: str,
    root: str | Path | None,
    classes: str | Sequence[str] = "all",
    synthetic_count: int = 12,
) -> list[ImageRecord]:
    """Load benchmark metadata without sampling or changing labels."""

    dataset_key = dataset.lower()
    if dataset_key == "synthetic":
        if classes == "all" or (not isinstance(classes, str) and list(classes) == ["all"]):
            category = "synthetic"
        else:
            category = classes if isinstance(classes, str) else str(list(classes)[0])
        return synthetic_records(category, synthetic_count)
    if dataset_key not in {"mvtec", "visa", "mpdd"}:
        raise ValueError(f"Unsupported dataset: {dataset}")
    if root is None:
        raise ValueError(f"A root directory is required for {dataset_key}.")
    root_path = Path(root).expanduser().resolve()
    if not root_path.is_dir():
        raise FileNotFoundError(f"Dataset root does not exist: {root_path}")

    if dataset_key == "visa":
        csv_path = _find_visa_csv(root_path)
        if csv_path is not None:
            records = _scan_visa_csv(root_path, csv_path, classes)
        else:
            records = _scan_mvtec_like(root_path, classes)
    else:
        records = _scan_mvtec_like(root_path, classes)
    if not records:
        raise ValueError(f"No image records found under {root_path} for classes={classes!r}.")
    return records
