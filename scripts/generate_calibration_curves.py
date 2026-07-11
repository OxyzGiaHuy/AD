from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path


def parse_run_name(name: str) -> dict[str, str | int]:
    parts = name.split("_")
    dataset = "visa" if "_visa_" in name else "mvtec" if "_mvtec_" in name else "unknown"
    variant = "unknown"
    for candidate in ["calib_subspace_head", "anomalydino", "patchcore", "subspacead", "head_pca"]:
        if name.startswith(candidate + "_") or f"_{candidate}_" in name:
            variant = candidate
            break
    k = -1
    seed = -1
    for part in parts:
        if part.startswith("k") and part[1:].isdigit():
            k = int(part[1:])
        if part.startswith("seed") and part[4:].isdigit():
            seed = int(part[4:])
    return {"dataset": dataset, "variant": variant, "k_shot": k, "seed": seed}


def weighted_mean(items: list[tuple[float | None, int]]) -> float | None:
    total = sum(count for value, count in items if value is not None and count > 0)
    if total == 0:
        return None
    return sum(float(value) * count for value, count in items if value is not None and count > 0) / total


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--outputs-dir", default="outputs")
    parser.add_argument("--out-dir", default="outputs/paper_tables")
    parser.add_argument("--pattern", default="*normal_synthetic")
    args = parser.parse_args()

    rows: list[dict] = []
    for run_dir in Path(args.outputs_dir).glob(args.pattern):
        bins_path = run_dir / "calibration_bins.json"
        if not bins_path.exists():
            continue
        meta = parse_run_name(run_dir.name)
        payload = json.loads(bins_path.read_text(encoding="utf-8"))
        for item in payload.get("bins", []):
            rows.append(
                {
                    **meta,
                    "run_id": run_dir.name,
                    "bin": int(item["bin"]),
                    "lo": float(item["lo"]),
                    "hi": float(item["hi"]),
                    "count": int(item["count"]),
                    "confidence": item.get("confidence"),
                    "accuracy": item.get("accuracy"),
                }
            )

    grouped: dict[tuple, list[dict]] = defaultdict(list)
    for row in rows:
        grouped[(row["dataset"], row["variant"], row["k_shot"], row["bin"])].append(row)

    summary = []
    for (dataset, variant, k_shot, bin_id), group in sorted(grouped.items()):
        count = sum(int(r["count"]) for r in group)
        summary.append(
            {
                "dataset": dataset,
                "variant": variant,
                "k_shot": k_shot,
                "bin": bin_id,
                "lo": group[0]["lo"],
                "hi": group[0]["hi"],
                "n_runs": len(group),
                "count": count,
                "confidence": weighted_mean([(r["confidence"], int(r["count"])) for r in group]),
                "accuracy": weighted_mean([(r["accuracy"], int(r["count"])) for r in group]),
            }
        )

    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    for path, data in [
        (out / "calibration_reliability_bins_detailed.csv", rows),
        (out / "calibration_reliability_bins_summary.csv", summary),
    ]:
        if not data:
            path.write_text("", encoding="utf-8")
            continue
        with path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(data[0].keys()))
            writer.writeheader()
            writer.writerows(data)
    (out / "calibration_reliability_bins_summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )
    print(f"runs={len({r['run_id'] for r in rows})}")
    print(out / "calibration_reliability_bins_summary.csv")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
