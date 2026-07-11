from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
import re


def parse_run_id(name: str) -> dict:
    info={"run_id":name,"dataset":"unknown","variant":"unknown","k_shot":"","seed":""}
    if "_mvtec_" in name: info["dataset"]="mvtec"
    elif "_visa_" in name: info["dataset"]="visa"
    for v in ["calib_subspace_head","head_pca","patchcore","anomalydino","subspacead"]:
        if name.startswith(v) or f"_{v}_" in name: info["variant"]=v; break
    m=re.search(r"_k(\d+)_seed(\d+)",name)
    if m: info["k_shot"]=m.group(1); info["seed"]=m.group(2)
    return info


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("w",newline="",encoding="utf-8") as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0].keys()))
        writer.writeheader(); writer.writerows(rows)


def main()->int:
    parser=argparse.ArgumentParser()
    parser.add_argument("--outputs-dir",default="outputs")
    parser.add_argument("--pattern",default="*normal_synthetic")
    parser.add_argument("--out-dir",default="outputs/paper_tables")
    args=parser.parse_args()
    rows=[]
    for metrics_path in sorted(Path(args.outputs_dir).glob(f"{args.pattern}/metrics.json")):
        data=json.loads(metrics_path.read_text(encoding="utf-8"))
        info=parse_run_id(metrics_path.parent.name)
        rows.append({**info,"latency_sec_per_image_cached_features":data.get("latency_sec_per_image"),"model_storage_mb":data.get("model_storage_mb"),"support_patch_count":data.get("support_patch_count"),"peak_memory_mb":data.get("peak_memory_mb")})
    write_csv(Path(args.out_dir)/"runtime_audit_summary.csv", rows)
    print(f"runs={len(rows)}")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
