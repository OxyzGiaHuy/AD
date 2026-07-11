from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-list", required=True)
    parser.add_argument("--python", default=sys.executable)
    parser.add_argument("--workers", type=int, default=2)
    parser.add_argument("--variants", nargs="*", default=None)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--max-images", type=int, default=None)
    args = parser.parse_args()
    configs = [Path(x.strip()) for x in Path(args.run_list).read_text(encoding="utf-8").splitlines() if x.strip()]
    if args.variants:
        configs = [p for p in configs if any(p.name.startswith(v + "_") for v in args.variants)]
    if args.limit:
        configs = configs[: args.limit]
    print(f"corruption_grid_tasks={len(configs)}", flush=True)
    def run(cfg: Path):
        cmd = [args.python, "scripts/evaluate_corruptions_batch.py", "--config", str(cfg)]
        if args.max_images:
            cmd += ["--max-images", str(args.max_images)]
        proc = subprocess.run(cmd, cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return cfg, proc.returncode, proc.stdout[-2000:], proc.stderr[-4000:]
    done = 0
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as ex:
        futures = [ex.submit(run, cfg) for cfg in configs]
        for fut in as_completed(futures):
            cfg, code, out, err = fut.result()
            if code != 0:
                print(f"FAILED {cfg} code={code}\nSTDOUT\n{out}\nSTDERR\n{err}", flush=True)
                return code
            done += 1
            if done % 25 == 0 or done == len(configs):
                print(f"corruption_grid_progress={done}/{len(configs)} last={cfg}", flush=True)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
