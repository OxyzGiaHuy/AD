from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageOps


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.config import load_config
from src.data.datasets import ImageRecord, load_records
from src.data.sampling import evaluation_records, few_shot_support
from src.evaluation.pixel_metrics import as_score_grid


def _read_predictions(run_dir: Path):
    import pandas as pd

    parquet = run_dir / "predictions.parquet"
    csv = run_dir / "predictions.csv"
    if parquet.is_file():
        return pd.read_parquet(parquet)
    if csv.is_file():
        return pd.read_csv(csv)
    raise FileNotFoundError(f"Missing {parquet} and {csv}")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _sequential_colour(x: np.ndarray) -> np.ndarray:
    """A fixed, monotone-lightness, viridis-style map with no extra dependency."""

    stops = np.asarray([0.0, 0.25, 0.50, 0.75, 1.0], dtype=np.float32)
    colours = np.asarray(
        [
            [68, 1, 84],
            [59, 82, 139],
            [33, 145, 140],
            [94, 201, 98],
            [253, 231, 37],
        ],
        dtype=np.float32,
    )
    flat = np.clip(np.asarray(x, dtype=np.float32), 0.0, 1.0).reshape(-1)
    rgb = np.empty((len(flat), 3), dtype=np.float32)
    for channel in range(3):
        rgb[:, channel] = np.interp(flat, stops, colours[:, channel])
    return np.uint8(np.clip(rgb.reshape((*x.shape, 3)), 0, 255))


def _visual_normalize(score_grid: np.ndarray, percentile: float = 99.0) -> tuple[np.ndarray, float, float]:
    grid = np.asarray(score_grid, dtype=np.float32)
    lo = float(np.nanmin(grid))
    hi = float(np.nanpercentile(grid, percentile))
    norm = np.clip((grid - lo) / (hi - lo + 1e-8), 0.0, 1.0)
    return norm.astype(np.float32), lo, hi


def _fit_on_white(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    contained = ImageOps.contain(image.convert("RGB"), size, Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", size, "white")
    offset = ((size[0] - contained.width) // 2, (size[1] - contained.height) // 2)
    canvas.paste(contained, offset)
    return canvas


def _save_support_montage(paths: list[Path], output: Path) -> None:
    tile_size = (320, 320)
    gap = 18
    canvas = Image.new("RGB", (tile_size[0] * len(paths) + gap * (len(paths) - 1), tile_size[1]), "white")
    for index, path in enumerate(paths):
        with Image.open(path) as image:
            tile = _fit_on_white(image, tile_size)
        canvas.paste(tile, (index * (tile_size[0] + gap), 0))
    canvas.save(output)


def _select_test_index(
    dataframe,
    eval_records: list[ImageRecord],
    defect_type: str,
    explicit_image: str | None,
) -> tuple[int, ImageRecord, str]:
    if len(dataframe) != len(eval_records):
        raise ValueError(f"Prediction/record length mismatch: {len(dataframe)} versus {len(eval_records)}")

    record_by_path = {str(Path(record.path).resolve()): record for record in eval_records}
    matched_records: list[ImageRecord] = []
    for path in dataframe["image_path"].astype(str):
        key = str(Path(path).resolve())
        if key not in record_by_path:
            raise ValueError(f"Prediction path is absent from the dataset scan: {path}")
        matched_records.append(record_by_path[key])

    if explicit_image:
        requested = str(Path(explicit_image).expanduser().resolve())
        candidates = [index for index, record in enumerate(matched_records) if str(Path(record.path).resolve()) == requested]
        if not candidates:
            raise ValueError(f"Requested test image is not in this run: {requested}")
        index = candidates[0]
        record = matched_records[index]
        if record.label != 1:
            raise ValueError("The explicit pipeline test image must be anomalous for the localization illustration.")
        return index, record, "explicit anomalous image path"

    candidates = [
        index
        for index, record in enumerate(matched_records)
        if record.label == 1 and record.defect_type.lower() == defect_type.lower()
    ]
    if not candidates:
        available = sorted({record.defect_type for record in matched_records if record.label == 1})
        raise ValueError(f"No capsule anomaly of type {defect_type!r}; available defect types: {available}")

    ordered = sorted(candidates, key=lambda index: (float(dataframe.iloc[index]["raw_score"]), matched_records[index].path))
    index = ordered[(len(ordered) - 1) // 2]
    return index, matched_records[index], f"lower median raw score within predeclared defect type {defect_type!r}"


def _copy_with_entry(source: Path, destination: Path, role: str) -> dict[str, object]:
    shutil.copy2(source, destination)
    return {
        "role": role,
        "source_path": str(source.resolve()),
        "output_path": str(destination.resolve()),
        "sha256": _sha256(destination),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Export auditable capsule assets for pipeline panels a and b.")
    parser.add_argument("--config", required=True)
    parser.add_argument("--run-dir", required=True)
    parser.add_argument("--out-dir", default="outputs/pipeline_visuals/capsule_k4_seed0")
    parser.add_argument("--defect-type", default="crack")
    parser.add_argument("--test-image", default=None, help="Optional exact anomalous image path; overrides median selection.")
    args = parser.parse_args()

    config_path = Path(args.config).resolve()
    run_dir = Path(args.run_dir).resolve()
    out_dir = Path(args.out_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    config = load_config(config_path)
    dataset = config.get("dataset", {})
    backbone = config.get("backbone", {})
    model = config.get("model", {})
    classes = dataset.get("classes", [])
    if dataset.get("name") != "mvtec" or classes not in (["capsule"], "capsule"):
        raise ValueError("This exporter is deliberately restricted to the MVTec capsule configuration.")
    if backbone.get("name") != "dinov2_vits14" or int(dataset.get("image_size", 0)) != 518:
        raise ValueError("Expected frozen DINOv2 ViT-S/14 at image_size=518.")
    if model.get("variant") != "calib_subspace_head" or int(model.get("pca_components", 0)) != 64:
        raise ValueError("Expected the paper's PCA64/calib_subspace_head configuration.")

    k_values = list(dataset.get("k_shots", []))
    seeds = list(dataset.get("seeds", []))
    if k_values != [4] or seeds != [0]:
        raise ValueError(f"Expected k_shots=[4] and seeds=[0], got {k_values} and {seeds}.")

    records = load_records(dataset["name"], dataset["root"], classes)
    support = few_shot_support(records, k=4, seed=0)
    evaluation = evaluation_records(records)
    dataframe = _read_predictions(run_dir)
    patch_scores = np.load(run_dir / "anomaly_maps" / "patch_scores.npy")
    if len(patch_scores) != len(dataframe):
        raise ValueError(f"Patch-score/prediction mismatch: {len(patch_scores)} versus {len(dataframe)}")

    selected_index, test_record, selection_rule = _select_test_index(
        dataframe,
        evaluation,
        defect_type=args.defect_type,
        explicit_image=args.test_image,
    )
    if not test_record.mask_path or not Path(test_record.mask_path).is_file():
        raise FileNotFoundError(f"Missing MVTec ground-truth mask for {test_record.path}")

    assets: list[dict[str, object]] = []
    support_outputs: list[Path] = []
    for index, record in enumerate(support):
        destination = out_dir / f"support_{index + 1:02d}.png"
        assets.append(_copy_with_entry(Path(record.path), destination, f"normal support {index + 1} of 4"))
        support_outputs.append(destination)
    montage = out_dir / "support_montage_k4.png"
    _save_support_montage(support_outputs, montage)
    assets.append({"role": "four-support montage", "output_path": str(montage), "sha256": _sha256(montage)})

    test_output = out_dir / "test_capsule_anomaly.png"
    assets.append(_copy_with_entry(Path(test_record.path), test_output, "test anomaly input x"))
    mask_output = out_dir / "gt_mask_evaluation_only.png"
    assets.append(_copy_with_entry(Path(test_record.mask_path), mask_output, "ground truth, evaluation only"))

    score_grid = as_score_grid(patch_scores[selected_index])
    if score_grid.shape != (37, 37):
        raise ValueError(f"Expected a 37x37 DINOv2 patch grid, got {score_grid.shape}")
    residual_npy = out_dir / "patch_residual_raw_37x37.npy"
    np.save(residual_npy, score_grid.astype(np.float32))
    assets.append({"role": "raw PCA patch residual tensor", "output_path": str(residual_npy), "sha256": _sha256(residual_npy)})

    normalized, display_lo, display_hi = _visual_normalize(score_grid, percentile=99.0)
    coarse_rgb = _sequential_colour(normalized)
    coarse = Image.fromarray(coarse_rgb).resize((444, 444), resample=Image.Resampling.NEAREST)
    coarse_output = out_dir / "patch_residual_map_nearest.png"
    coarse.save(coarse_output)
    assets.append({"role": "coarse 37x37 residual map for panels a/b", "output_path": str(coarse_output), "sha256": _sha256(coarse_output)})

    with Image.open(test_record.path) as original:
        original_rgb = original.convert("RGB")
    pixel_norm = Image.fromarray(np.uint8(normalized * 255), mode="L").resize(original_rgb.size, resample=Image.Resampling.BILINEAR)
    pixel_rgb = _sequential_colour(np.asarray(pixel_norm, dtype=np.float32) / 255.0)
    heatmap_output = out_dir / "pixel_anomaly_heatmap_bilinear.png"
    Image.fromarray(pixel_rgb).save(heatmap_output)
    assets.append({"role": "bilinearly upsampled pixel anomaly heatmap", "output_path": str(heatmap_output), "sha256": _sha256(heatmap_output)})

    base = np.asarray(original_rgb, dtype=np.float32)
    overlay = np.uint8(np.clip(0.55 * base + 0.45 * pixel_rgb, 0, 255))
    overlay_output = out_dir / "test_heatmap_overlay.png"
    Image.fromarray(overlay).save(overlay_output)
    assets.append({"role": "display-only heatmap overlay", "output_path": str(overlay_output), "sha256": _sha256(overlay_output)})

    row = dataframe.iloc[selected_index]
    manifest = {
        "purpose": "Pipeline panels a and b only; no LOIO or CRESS outputs",
        "config_path": str(config_path),
        "config_sha256": _sha256(config_path),
        "run_dir": str(run_dir),
        "dataset": "MVTec AD",
        "category": "capsule",
        "k": 4,
        "seed": 0,
        "backbone": "frozen DINOv2 ViT-S/14",
        "input_size": 518,
        "pca_components": 64,
        "patch_grid": [37, 37],
        "raw_image_score_definition": "maximum PCA residual across patch tokens",
        "selected_prediction_index": int(selected_index),
        "selected_defect_type": test_record.defect_type,
        "selected_raw_score": float(row["raw_score"]),
        "selection_rule": selection_rule,
        "display_normalization_only": {
            "rule": "per-image clipping from the minimum to the 99th percentile, followed by a fixed sequential colour map",
            "lower": display_lo,
            "upper": display_hi,
            "warning": "This normalization and the overlay are for visualization only and are not used for scores, thresholds, or reported metrics.",
        },
        "ground_truth_warning": "The ground-truth mask is evaluation-only and must never be drawn as an input to DINOv2, PCA fitting, scoring, or calibration.",
        "assets": assets,
    }
    manifest_path = out_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True), encoding="utf-8")
    print(manifest_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
