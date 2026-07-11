from __future__ import annotations

import argparse
import csv
from pathlib import Path
import re
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def read_table(path_without_suffix: Path):
    import pandas as pd
    if path_without_suffix.with_suffix(".parquet").exists():
        return pd.read_parquet(path_without_suffix.with_suffix(".parquet"))
    return pd.read_csv(path_without_suffix.with_suffix(".csv"))


def parse_run_id(name: str) -> dict:
    info={"run_id":name,"dataset":"unknown","variant":"unknown","k_shot":"","seed":"","condition":"clean"}
    if "_mvtec_" in name: info["dataset"]="mvtec"
    elif "_visa_" in name: info["dataset"]="visa"
    for v in ["calib_subspace_head","head_pca","patchcore","anomalydino","subspacead"]:
        if name.startswith(v) or f"_{v}_" in name: info["variant"]=v; break
    m=re.search(r"_k(\d+)_seed(\d+)",name)
    if m: info["k_shot"]=m.group(1); info["seed"]=m.group(2)
    if "_fgsm_" in name: info["condition"]="fgsm"
    elif "_corruption_" in name: info["condition"]=name.split("_corruption_")[-1]
    return info


def entropy_auc(labels: np.ndarray, entropy: np.ndarray) -> float:
    from src.evaluation.metrics import roc_auc_score_np
    if len(np.unique(labels))<2: return float("nan")
    return roc_auc_score_np(labels.astype(int), entropy.astype(float))


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True,exist_ok=True)
    if not rows: path.write_text("",encoding="utf-8"); return
    with path.open("w",newline="",encoding="utf-8") as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0].keys()))
        writer.writeheader(); writer.writerows(rows)


def main()->int:
    parser=argparse.ArgumentParser()
    parser.add_argument("--outputs-dir", default="outputs")
    parser.add_argument("--robustness-dir", default="outputs/robustness")
    parser.add_argument("--out-dir", default="outputs/paper_tables")
    parser.add_argument("--pattern", default="*")
    args=parser.parse_args()
    run_dirs=[p for root in [Path(args.outputs_dir),Path(args.robustness_dir)] for p in root.glob(args.pattern) if (p/"predictions.parquet").exists() or (p/"predictions.csv").exists()]
    rows=[]
    for run_dir in sorted(run_dirs):
        try: df=read_table(run_dir/"predictions")
        except Exception: continue
        if "entropy" not in df or "label" not in df: continue
        info=parse_run_id(run_dir.name)
        labels=df["label"].to_numpy().astype(int); ent=df["entropy"].to_numpy().astype(float)
        rows.append({**info,"n":len(df),"entropy_normal_mean":float(np.mean(ent[labels==0])) if np.any(labels==0) else float("nan"),"entropy_anomaly_mean":float(np.mean(ent[labels==1])) if np.any(labels==1) else float("nan"),"entropy_label_auroc":entropy_auc(labels,ent)})
    write_csv(Path(args.out_dir)/"uncertainty_separation_detailed.csv", rows)
    print(f"runs={len(rows)}")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
