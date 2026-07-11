from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--outputs-dir", default="outputs")
    parser.add_argument("--pattern", default="*")
    args = parser.parse_args()
    rows = []
    for metrics_path in sorted(Path(args.outputs_dir).glob(f"{args.pattern}/metrics.json")):
        data = json.loads(metrics_path.read_text(encoding="utf-8"))
        rows.append((metrics_path.parent.name, data))
    if not rows:
        print("No metrics found")
        return 1
    print("run_id,auroc,ap,max_f1,ece,brier,nll,latency_sec_per_image,model_storage_mb,support_patch_count")
    for run_id, data in rows:
        print(",".join([
            run_id,
            str(data.get("auroc")),
            str(data.get("ap")),
            str(data.get("max_f1")),
            str(data.get("ece")),
            str(data.get("brier")),
            str(data.get("nll")),
            str(data.get("latency_sec_per_image")),
            str(data.get("model_storage_mb")),
            str(data.get("support_patch_count")),
        ]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
