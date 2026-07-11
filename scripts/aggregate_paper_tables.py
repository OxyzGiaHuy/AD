from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from statistics import mean, pstdev

METRICS = ["auroc", "ap", "max_f1", "ece", "brier", "nll", "latency_sec_per_image", "model_storage_mb", "calibration_anomaly_val_count"]


def parse_run_id(run_id: str) -> dict[str, str]:
    parts = run_id.split("_")
    info = {"run_id": run_id}
    k_idx = None
    for idx, part in enumerate(parts):
        if part.startswith("k") and part[1:].isdigit():
            info["k_shot"] = part[1:]
            k_idx = idx
        if part.startswith("seed"):
            info["seed"] = part.replace("seed", "")
    if run_id.endswith("_normal_plus_anomaly_val"):
        info["calibration_mode"] = "normal_plus_anomaly_val"
    elif run_id.endswith("_normal_synthetic"):
        info["calibration_mode"] = "normal_synthetic"
    else:
        info["calibration_mode"] = "unknown"
    if "mvtec" in parts:
        info["dataset"] = "mvtec"
    elif "visa" in parts:
        info["dataset"] = "visa"
    else:
        info["dataset"] = "unknown"

    variant_tokens: list[str] = []
    if k_idx is not None and k_idx >= 3 and parts[k_idx - 3 : k_idx] == ["calib", "subspace", "head"]:
        info["variant"] = "calib_subspace_head"
        variant_tokens = ["calib", "subspace", "head"]
    elif k_idx is not None and k_idx >= 2 and parts[k_idx - 2 : k_idx] == ["head", "pca"]:
        info["variant"] = "head_pca"
        variant_tokens = ["head", "pca"]
    elif k_idx is not None and k_idx >= 1 and parts[k_idx - 1] in {"patchcore", "anomalydino", "subspacead"}:
        info["variant"] = parts[k_idx - 1]
        variant_tokens = [parts[k_idx - 1]]
    elif "calib" in parts and "subspace" in parts:
        info["variant"] = "calib_subspace_head"
        variant_tokens = ["calib", "subspace", "head"]
    elif "patchcore" in parts:
        info["variant"] = "patchcore"
        variant_tokens = ["patchcore"]
    elif "anomalydino" in parts:
        info["variant"] = "anomalydino"
        variant_tokens = ["anomalydino"]
    elif "subspacead" in parts:
        info["variant"] = "subspacead"
        variant_tokens = ["subspacead"]
    elif "head" in parts and "pca" in parts:
        info["variant"] = "head_pca"
        variant_tokens = ["head", "pca"]
    else:
        info["variant"] = "unknown"

    if k_idx is not None and variant_tokens:
        info["experiment"] = "_".join(parts[: max(0, k_idx - len(variant_tokens))])
    else:
        info["experiment"] = run_id
    return info


def fmt(values: list[float]) -> str:
    values = [v for v in values if isinstance(v, (int, float)) and v == v]
    if not values:
        return ""
    return f"{mean(values):.4f}+-{pstdev(values):.4f}" if len(values) > 1 else f"{values[0]:.4f}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--outputs-dir", default="outputs")
    parser.add_argument("--pattern", default="*")
    parser.add_argument("--group-by", default="dataset,experiment,variant,k_shot,calibration_mode")
    parser.add_argument("--out", default=None)
    args = parser.parse_args()
    group_keys = [item.strip() for item in args.group_by.split(",") if item.strip()]
    groups: dict[tuple[str, ...], dict[str, list[float]]] = defaultdict(lambda: defaultdict(list))
    for metrics_path in sorted(Path(args.outputs_dir).glob(f"{args.pattern}/metrics.json")):
        data = json.loads(metrics_path.read_text(encoding="utf-8"))
        info = parse_run_id(metrics_path.parent.name)
        key = tuple(info.get(k, "") for k in group_keys)
        for metric in METRICS:
            value = data.get(metric)
            if isinstance(value, (int, float)):
                groups[key][metric].append(float(value))
    header = group_keys + METRICS
    lines = [",".join(header)]
    for key, values in sorted(groups.items()):
        lines.append(",".join(list(key) + [fmt(values[m]) for m in METRICS]))
    text = "\n".join(lines) + "\n"
    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
