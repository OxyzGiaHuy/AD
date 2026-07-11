from __future__ import annotations

import argparse
import csv
from pathlib import Path


def read_csv(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fieldnames = list(rows[0].keys())
    for row in rows[1:]:
        for key in row:
            if key not in fieldnames:
                fieldnames.append(key)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def image_suffix(path: str, cls: str) -> str:
    parts = Path(path).parts
    if cls in parts:
        idx = parts.index(cls)
        return "/".join(parts[idx:])
    return "/".join(parts[-3:])


def key(row: dict) -> tuple[str, str, str, str, str, str]:
    return (row["dataset"], row["class"], str(row["k_shot"]), str(row["seed"]), row["corruption"], image_suffix(row["image_path"], row["class"]))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--predictions", required=True)
    parser.add_argument("--conformal", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    preds = read_csv(Path(args.predictions))
    conf = read_csv(Path(args.conformal))
    conf_by_key = {key(r): r for r in conf}
    merged = []
    missing = 0
    for row in preds:
        item = dict(row)
        c = conf_by_key.get(key(row))
        if c is None:
            missing += 1
        else:
            for col in ["image_p_loio", "image_p_weighted", "conformal_prob_loio", "conformal_prob_weighted", "patch_rejection_rate_loio", "patch_rejection_rate_weighted", "n_eff_patch", "n_eff_image", "coverage_gap_proxy", "domain_confidence_conformal"]:
                if col in c:
                    item[col] = c[col]
        merged.append(item)
    write_csv(Path(args.out), merged)
    print(f"merged={len(merged)} missing_conformal={missing}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
