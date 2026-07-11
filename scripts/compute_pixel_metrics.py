from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
import re
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.data.datasets import load_records
from src.evaluation.pixel_metrics import resize_score_map, summarize_pixel
from src.utils.io import write_json

_RECORD_CACHE = {}
_IMAGE_SIZE_CACHE = {}
_MASK_CACHE = {}


def read_table(path_without_suffix: Path):
    parquet = path_without_suffix.with_suffix(".parquet")
    csv_path = path_without_suffix.with_suffix(".csv")
    import pandas as pd
    if parquet.exists():
        return pd.read_parquet(parquet)
    if csv_path.exists():
        return pd.read_csv(csv_path)
    raise FileNotFoundError(path_without_suffix)


def parse_run(run_id: str) -> dict[str, str]:
    out = {"run_id": run_id, "dataset": "unknown", "class": "unknown", "variant": "unknown", "k_shot": "", "seed": ""}
    if "_mvtec_" in run_id:
        out["dataset"] = "mvtec"
    elif "_visa_" in run_id:
        out["dataset"] = "visa"
    m = re.search(r"_(mvtec|visa)_(.+?)_k(\d+)_seed(\d+)_", run_id)
    if m:
        out["dataset"] = m.group(1)
        out["class"] = m.group(2)
        out["k_shot"] = m.group(3)
        out["seed"] = m.group(4)
    for variant in ["calib_subspace_head", "head_pca", "patchcore", "anomalydino", "subspacead"]:
        if run_id.startswith(variant) or f"_{variant}_" in run_id:
            out["variant"] = variant
            break
    return out


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def metrics_for_run(run_dir: Path, roots: dict[str, str], max_side: int = 256) -> dict | None:
    info = parse_run(run_dir.name)
    if info["dataset"] not in roots:
        return None
    pred_path = run_dir / "predictions"
    score_path = run_dir / "anomaly_maps" / "patch_scores.npy"
    if not score_path.exists():
        return None
    df = read_table(pred_path)
    patch_scores = np.load(score_path)
    record_key = (info["dataset"], roots[info["dataset"]], info["class"])
    if record_key not in _RECORD_CACHE:
        records = load_records(info["dataset"], roots[info["dataset"]], [info["class"]])
        _RECORD_CACHE[record_key] = {r.path: r for r in records}
    rec_by_path = _RECORD_CACHE[record_key]
    masks = []
    maps = []
    skipped_anomaly_missing_mask = 0
    from PIL import Image
    for idx, row in df.reset_index(drop=True).iterrows():
        image_path = str(row["image_path"])
        rec = rec_by_path.get(image_path)
        if rec is None:
            continue
        if image_path not in _IMAGE_SIZE_CACHE:
            with Image.open(image_path) as image:
                _IMAGE_SIZE_CACHE[image_path] = image.size
        w, h = _IMAGE_SIZE_CACHE[image_path]
        scale = min(1.0, float(max_side) / max(h, w)) if max_side else 1.0
        out_h = max(1, int(round(h * scale)))
        out_w = max(1, int(round(w * scale)))
        mask_key = (image_path, rec.mask_path or "", out_h, out_w)
        if mask_key in _MASK_CACHE:
            mask = _MASK_CACHE[mask_key]
        elif rec.label == 1:
            if not rec.mask_path or not Path(rec.mask_path).exists():
                skipped_anomaly_missing_mask += 1
                continue
            with Image.open(rec.mask_path) as mask_image:
                mask = np.asarray(mask_image.convert("L").resize((out_w, out_h), resample=Image.Resampling.NEAREST)) > 0
            _MASK_CACHE[mask_key] = mask
        else:
            mask = np.zeros((out_h, out_w), dtype=bool)
            _MASK_CACHE[mask_key] = mask
        score = resize_score_map(patch_scores[int(idx)], (out_h, out_w))
        masks.append(mask)
        maps.append(score)
    summary = summarize_pixel(masks, maps)
    return {**info, **summary, "images_used": len(masks), "skipped_anomaly_missing_mask": skipped_anomaly_missing_mask}


def summarize(rows: list[dict]) -> list[dict]:
    from collections import defaultdict
    from statistics import mean, stdev
    groups = defaultdict(list)
    for row in rows:
        groups[(row["dataset"], row["variant"], row["k_shot"])].append(row)
    out = []
    for key, group in sorted(groups.items()):
        base = {"dataset": key[0], "variant": key[1], "k_shot": key[2], "n": len(group)}
        for metric in ["pixel_auroc", "pixel_ap", "max_pixel_f1", "pro"]:
            vals = [float(r[metric]) for r in group if r.get(metric) is not None and not np.isnan(float(r[metric]))]
            base[f"{metric}_mean"] = mean(vals) if vals else float("nan")
            base[f"{metric}_std"] = stdev(vals) if len(vals) > 1 else 0.0
        out.append(base)
    return out


def usable_row(row: dict) -> bool:
    try:
        if int(float(row.get("images_used", 0))) <= 0:
            return False
        value = float(row.get("pixel_auroc", "nan"))
        return not np.isnan(value)
    except (TypeError, ValueError):
        return False


def dedupe_rows(rows: list[dict]) -> list[dict]:
    deduped = {}
    for row in rows:
        if not usable_row(row):
            continue
        run_id = row.get("run_id")
        if run_id:
            deduped[run_id] = row
    return [deduped[key] for key in sorted(deduped)]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--outputs-dir", default="outputs")
    parser.add_argument("--pattern", default="*mvtec*normal_synthetic")
    parser.add_argument("--mvtec-root", default="data/mvtec")
    parser.add_argument("--visa-root", default="data/visa")
    parser.add_argument("--out-dir", default="outputs/paper_tables")
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--max-side", type=int, default=256)
    parser.add_argument("--main-only", action="store_true")
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--variants", nargs="*", default=None)
    args = parser.parse_args()
    run_dirs = [p for p in sorted(Path(args.outputs_dir).glob(args.pattern)) if (p / "predictions.parquet").exists() or (p / "predictions.csv").exists()]
    if args.main_only:
        run_dirs = [p for p in run_dirs if not p.name.startswith("ablation_") and not p.name.startswith("smoke_")]
    if args.variants:
        allowed = set(args.variants)
        run_dirs = [p for p in run_dirs if parse_run(p.name).get("variant") in allowed]
    out_dir = Path(args.out_dir)
    detail_path = out_dir / "pixel_metrics_detailed.csv"
    rows = []
    done = set()
    if args.resume and detail_path.exists() and detail_path.stat().st_size > 0:
        with detail_path.open(newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                rows.append(row)
                done.add(row.get("run_id"))
        rows = dedupe_rows(rows)
        done = {row.get("run_id") for row in rows}
        rows = dedupe_rows(rows)
        done = {row.get("run_id") for row in rows}
    run_dirs = [p for p in run_dirs if p.name not in done]
    if args.limit:
        run_dirs = run_dirs[: args.limit]
    roots = {"mvtec": args.mvtec_root, "visa": args.visa_root}
    for index, run_dir in enumerate(run_dirs, start=1):
        try:
            row = metrics_for_run(run_dir, roots, max_side=args.max_side)
            if row:
                rows.append(row)
                write_csv(detail_path, rows)
                if index % 25 == 0:
                    print(f"pixel_progress={index}/{len(run_dirs)} total={len(rows)} last={run_dir.name}", flush=True)
        except Exception as exc:
            print(f"WARN failed {run_dir}: {exc}", file=sys.stderr)
    rows = dedupe_rows(rows)
    write_csv(detail_path, rows)
    rows = dedupe_rows(rows)
    write_csv(detail_path, rows)
    summary = summarize(rows)
    write_csv(out_dir / "pixel_metrics_summary.csv", summary)
    print(f"runs={len(rows)}")
    print(out_dir / "pixel_metrics_summary.csv")
    return 0 if rows else 1


if __name__ == "__main__":
    raise SystemExit(main())
