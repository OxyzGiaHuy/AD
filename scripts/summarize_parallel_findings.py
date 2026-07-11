from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path

import pandas as pd


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def read_official_subspacead(root: Path) -> pd.DataFrame:
    frames = []
    for path in sorted(root.glob("**/benchmark_results.csv")):
        df = pd.read_csv(path)
        df["source_path"] = str(path)
        frames.append(df)
    if not frames:
        return pd.DataFrame()
    return pd.concat(frames, ignore_index=True)


def official_rows(df: pd.DataFrame) -> list[dict]:
    if df.empty:
        return []
    rows = []
    for _, row in df.iterrows():
        category = str(row.get("Category", row.get("categories", row.get("category", ""))))
        rows.append(
            {
                "source": "official_subspacead",
                "dataset": "mvtec_ad",
                "category": category,
                "i_auroc": float(row.get("Image AUROC", row.get("I-AUROC", math.nan))),
                "i_aupr": float(row.get("Image AUPR", row.get("I-AUPR", math.nan))),
                "pixel_auroc": float(row.get("Pixel AUROC", row.get("P-AUROC", math.nan))),
                "au_pro": float(row.get("AU-PRO", math.nan)),
                "source_path": row.get("source_path", ""),
            }
        )
    return rows


def ablation_claim_rows(path: Path) -> list[dict]:
    if not path.exists() or path.stat().st_size == 0:
        return []
    df = pd.read_csv(path)
    rows: list[dict] = []

    pca = df[df["ablation"].eq("pca_components")].copy()
    if not pca.empty:
        for k, g in pca.groupby("k_shot"):
            best = g.sort_values("auroc_mean", ascending=False).iloc[0]
            smallest = g.sort_values("model_storage_mb_mean", ascending=True).iloc[0]
            rows.append(
                {
                    "finding": "pca_accuracy_storage_tradeoff",
                    "k_shot": int(k),
                    "best_setting": f"pca={best['value']}",
                    "best_auroc": float(best["auroc_mean"]),
                    "best_ece": float(best["ece_mean"]),
                    "best_storage_mb": float(best["model_storage_mb_mean"]),
                    "smallest_setting": f"pca={smallest['value']}",
                    "smallest_auroc": float(smallest["auroc_mean"]),
                    "smallest_storage_mb": float(smallest["model_storage_mb_mean"]),
                    "paper_note": "PCA128 improves ranking while staying below 0.6 MB; useful as accuracy-storage ablation, not a novelty claim by itself.",
                }
            )

    alpha = df[df["ablation"].eq("alpha_decoupling")].copy()
    if not alpha.empty:
        for k, g in alpha.groupby("k_shot"):
            best_rank = g.sort_values("auroc_mean", ascending=False).iloc[0]
            best_cal = g.sort_values("ece_mean", ascending=True).iloc[0]
            rows.append(
                {
                    "finding": "alpha_decoupling_tradeoff",
                    "k_shot": int(k),
                    "best_setting": f"alpha={best_rank['value']}",
                    "best_auroc": float(best_rank["auroc_mean"]),
                    "best_ece": float(best_rank["ece_mean"]),
                    "best_storage_mb": float(best_rank["model_storage_mb_mean"]),
                    "smallest_setting": f"best_ece_alpha={best_cal['value']}",
                    "smallest_auroc": float(best_cal["auroc_mean"]),
                    "smallest_storage_mb": float(best_cal["model_storage_mb_mean"]),
                    "paper_note": "Directly mixing head score can improve ECE but hurts AUROC when head dominates; supports decoupled ranking/calibration.",
                }
            )

    calib = df[df["ablation"].eq("calibration_mode")].copy()
    if not calib.empty:
        for k, g in calib.groupby("k_shot"):
            best_cal = g.sort_values("ece_mean", ascending=True).iloc[0]
            rows.append(
                {
                    "finding": "upper_bound_calibration",
                    "k_shot": int(k),
                    "best_setting": str(best_cal["value"]),
                    "best_auroc": float(best_cal["auroc_mean"]),
                    "best_ece": float(best_cal["ece_mean"]),
                    "best_storage_mb": float(best_cal["model_storage_mb_mean"]),
                    "smallest_setting": "",
                    "smallest_auroc": math.nan,
                    "smallest_storage_mb": math.nan,
                    "paper_note": "Small anomaly validation improves calibration; report only as upper-bound, not main protocol.",
                }
            )
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--official-root", default="outputs/official_subspacead_small_threeclass")
    parser.add_argument("--tables-dir", default="outputs/paper_tables")
    args = parser.parse_args()

    tables_dir = Path(args.tables_dir)
    official = read_official_subspacead(Path(args.official_root))
    official_out = official_rows(official)
    write_csv(tables_dir / "official_subspacead_representative.csv", official_out)

    claim_rows = ablation_claim_rows(tables_dir / "mvtec_ablation_summary.csv")
    write_csv(tables_dir / "parallel_findings_for_claims.csv", claim_rows)

    print(tables_dir / "official_subspacead_representative.csv")
    print(tables_dir / "parallel_findings_for_claims.csv")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
