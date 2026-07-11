from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.run_benchmark_grid import run_id_from_config


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-list", required=True)
    parser.add_argument("--python", default=sys.executable)
    parser.add_argument("--outputs-dir", default="outputs")
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--no-skip", action="store_true")
    args = parser.parse_args()

    configs = [Path(line.strip()) for line in Path(args.run_list).read_text(encoding="utf-8").splitlines() if line.strip()]
    if args.limit is not None:
        configs = configs[: args.limit]

    tasks = []
    skipped = 0
    for cfg in configs:
        run_id = run_id_from_config(cfg)
        metrics = Path(args.outputs_dir) / run_id / "metrics.json"
        if metrics.exists() and not args.no_skip:
            skipped += 1
            continue
        tasks.append((cfg, run_id))

    total = len(tasks)
    print(f"parallel_grid_tasks={total} skipped={skipped}", flush=True)
    if not tasks:
        return 0

    def run_task(item):
        cfg, run_id = item
        proc = subprocess.run(
            [args.python, "-m", "src.run_experiment", "--config", str(cfg)],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if proc.returncode != 0:
            return cfg, run_id, proc.returncode, proc.stdout[-2000:], proc.stderr[-4000:]
        return cfg, run_id, 0, proc.stdout[-1000:], ""

    completed = 0
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        futures = [executor.submit(run_task, task) for task in tasks]
        for future in as_completed(futures):
            cfg, run_id, code, stdout, stderr = future.result()
            if code != 0:
                print(f"FAILED {cfg} -> {run_id} code={code}\nSTDOUT\n{stdout}\nSTDERR\n{stderr}", flush=True)
                return code
            completed += 1
            if completed % 50 == 0 or completed == total:
                print(f"parallel_grid_progress={completed}/{total} last={run_id}", flush=True)
    print(f"parallel_grid_completed={completed} skipped={skipped}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
