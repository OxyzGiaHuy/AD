from __future__ import annotations

import argparse
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.evaluation.pixel_metrics import normalize_map, resize_score_map
from src.utils.io import ensure_dir, write_json


def read_table(path_without_suffix: Path):
    parquet = path_without_suffix.with_suffix(".parquet")
    csv = path_without_suffix.with_suffix(".csv")
    if parquet.exists():
        import pandas as pd
        return pd.read_parquet(parquet)
    if csv.exists():
        import pandas as pd
        return pd.read_csv(csv)
    raise FileNotFoundError(f"Missing predictions table at {path_without_suffix}.[parquet|csv]")


def colormap_jet(x: np.ndarray) -> np.ndarray:
    x = np.clip(x, 0.0, 1.0)
    r = np.clip(1.5 - np.abs(4.0 * x - 3.0), 0.0, 1.0)
    g = np.clip(1.5 - np.abs(4.0 * x - 2.0), 0.0, 1.0)
    b = np.clip(1.5 - np.abs(4.0 * x - 1.0), 0.0, 1.0)
    return np.stack([r, g, b], axis=-1)


def save_overlay(image_path: str, score_map: np.ndarray, out_prefix: Path, mask_path: str | None = None) -> None:
    from PIL import Image

    image = Image.open(image_path).convert("RGB")
    w, h = image.size
    norm = normalize_map(resize_score_map(score_map, (h, w)))
    heat = np.uint8(colormap_jet(norm) * 255)
    base = np.asarray(image, dtype=np.float32)
    overlay = np.uint8(np.clip(0.55 * base + 0.45 * heat, 0, 255))
    out_prefix.parent.mkdir(parents=True, exist_ok=True)
    image.save(out_prefix.with_name(out_prefix.name + "_original.png"))
    Image.fromarray(heat).save(out_prefix.with_name(out_prefix.name + "_heatmap.png"))
    Image.fromarray(overlay).save(out_prefix.with_name(out_prefix.name + "_overlay.png"))
    if mask_path and isinstance(mask_path, str) and mask_path and Path(mask_path).exists():
        mask = Image.open(mask_path).convert("L").resize((w, h), resample=Image.Resampling.NEAREST)
        Image.fromarray(np.asarray(mask)).save(out_prefix.with_name(out_prefix.name + "_gt_mask.png"))


def choose_indices(df, max_per_kind: int) -> list[int]:
    rows = []
    labels = df["label"].to_numpy() if "label" in df else np.zeros(len(df), dtype=int)
    scores = df["raw_score"].to_numpy() if "raw_score" in df else np.arange(len(df))
    entropy = df["entropy"].to_numpy() if "entropy" in df else scores
    for label, name in [(1, "anomaly"), (0, "normal")]:
        idx = np.where(labels == label)[0]
        if len(idx):
            rows.extend(idx[np.argsort(-scores[idx])[:max_per_kind]].tolist())
            rows.extend(idx[np.argsort(-entropy[idx])[:max_per_kind]].tolist())
    seen = []
    for idx in rows:
        if idx not in seen:
            seen.append(idx)
    return seen[: max_per_kind * 4]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", required=True)
    parser.add_argument("--out-dir", default="outputs/figures")
    parser.add_argument("--max-per-kind", type=int, default=2)
    args = parser.parse_args()
    run_dir = Path(args.run_dir)
    df = read_table(run_dir / "predictions")
    patch_scores = np.load(run_dir / "anomaly_maps" / "patch_scores.npy")
    out_dir = ensure_dir(Path(args.out_dir) / run_dir.name)
    selected = choose_indices(df, args.max_per_kind)
    manifest = []
    for rank, idx in enumerate(selected):
        row = df.iloc[int(idx)].to_dict()
        image_path = str(row["image_path"])
        mask_path = row.get("mask_path") or row.get("gt_mask") or None
        prefix = out_dir / f"{rank:02d}_idx{idx}_label{int(row.get('label', 0))}"
        save_overlay(image_path, patch_scores[int(idx)], prefix, mask_path=mask_path)
        manifest.append({"index": int(idx), "image_path": image_path, "label": int(row.get("label", 0)), "raw_score": float(row.get("raw_score", 0.0)), "entropy": float(row.get("entropy", 0.0))})
    write_json(out_dir / "manifest.json", {"run_dir": str(run_dir), "count": len(manifest), "samples": manifest})
    print(out_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
