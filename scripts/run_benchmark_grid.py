from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def run_id_from_config(path: Path) -> str:
    import yaml

    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    name = data.get("experiment", {}).get("name", path.stem)
    variant = data.get("model", {}).get("variant", "model")
    k = data.get("dataset", {}).get("k_shots", [1])[0]
    seed = data.get("dataset", {}).get("seeds", [0])[0]
    mode = data.get("calibration", {}).get("modes", ["normal_synthetic"])[0]
    return f"{name}_{variant}_k{k}_seed{seed}_{mode}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-list", required=True)
    parser.add_argument("--python", default=sys.executable)
    parser.add_argument("--outputs-dir", default="outputs")
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--no-skip", action="store_true")
    args = parser.parse_args()
    configs = [Path(line.strip()) for line in Path(args.run_list).read_text(encoding="utf-8").splitlines() if line.strip()]
    if args.limit is not None:
        configs = configs[: args.limit]
    completed = 0
    skipped = 0
    for cfg in configs:
        run_id = run_id_from_config(cfg)
        metrics = Path(args.outputs_dir) / run_id / "metrics.json"
        if metrics.exists() and not args.no_skip:
            print(f"SKIP {cfg} -> {run_id}", flush=True)
            skipped += 1
            continue
        print(f"RUN {cfg}", flush=True)
        subprocess.run([args.python, "-m", "src.run_experiment", "--config", str(cfg)], check=True)
        completed += 1
    print(f"completed={completed} skipped={skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
