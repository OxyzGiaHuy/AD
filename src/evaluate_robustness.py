from __future__ import annotations

import argparse
from pathlib import Path

from .robustness.attacks import parse_epsilon
from .utils.docs import append_markdown


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--attack", default="fgsm")
    parser.add_argument("--epsilon", default="8/255")
    parser.add_argument("--outputs-dir", default="outputs")
    parser.add_argument("--docs-dir", default="docs")
    args = parser.parse_args(argv)
    epsilon = parse_epsilon(args.epsilon)
    run_dir = Path(args.outputs_dir) / args.run_id
    if not run_dir.exists():
        raise FileNotFoundError(f"Run directory not found: {run_dir}")
    append_markdown(
        Path(args.docs_dir) / "experiment_findings.md",
        f"Robustness requested for {args.run_id}",
        [
            f"- Attack: `{args.attack}`",
            f"- Epsilon: `{epsilon}`",
            "- Status: full image-space FGSM requires a differentiable model.loss_on_images hook.",
        ],
    )
    print(f"Recorded robustness request for {args.run_id} with epsilon={epsilon}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

