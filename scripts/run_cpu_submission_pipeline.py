"""Fail-closed, one-command CPU analysis for GPU-exported SC3R artifacts.

The GPU server creates immutable score/support CSVs. This script audits those
files, runs every explicitly listed nested analysis, and writes a checksum
manifest. It never extracts features or edits manuscript numbers.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
from pathlib import Path
import subprocess
import sys

import pandas as pd
import numpy as np
import sklearn

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.audit_sc3r_artifacts import audit_frames
from scripts.evaluate_nested_sc3r import evaluate_nested, normalize_support_scores
from scripts.hierarchical_bootstrap_comparison import compare
from scripts.summarize_nested_sc3r import (
    aggregate_cells,
    build_empirical_gate_report,
    build_latex_tables,
    paired_cell_audit,
)


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _resolve(config_path: Path, value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else (config_path.parent / path).resolve()


def _git_state() -> dict[str, object]:
    def run(*args: str) -> str:
        result = subprocess.run(
            ["git", *args], cwd=ROOT, check=True, capture_output=True, text=True
        )
        return result.stdout.strip()

    try:
        return {"commit": run("rev-parse", "HEAD"), "dirty": bool(run("status", "--porcelain"))}
    except (FileNotFoundError, subprocess.CalledProcessError):
        return {"commit": None, "dirty": None}


def _load_artifact_set(config_path: Path, name: str, spec: dict, grid: dict) -> tuple[dict, dict[str, Path]]:
    required = ["views", "support_stats", "support_manifest", "support_residuals"]
    missing = [key for key in required if not spec.get(key)]
    if missing:
        raise ValueError(f"artifact set {name!r} is missing {missing}")
    paths = {key: _resolve(config_path, spec[key]) for key in required}
    absent = [str(path) for path in paths.values() if not path.is_file()]
    if absent:
        raise FileNotFoundError(f"artifact set {name!r} has missing files: {absent}")
    views = pd.read_csv(paths["views"])
    stats = pd.read_csv(paths["support_stats"])
    support = pd.read_csv(paths["support_manifest"])
    audit = audit_frames(
        views, stats, support,
        grid.get("k_shots"), grid.get("seeds"), grid.get("corruptions"),
    )
    if audit["status"] != "pass":
        raise RuntimeError(f"artifact audit failed for {name}: {audit['issues']}")
    return {
        "views": views,
        "stats": stats,
        "support": support,
        "residuals": pd.read_csv(paths["support_residuals"]),
        "audit": audit,
    }, paths


def run_pipeline(config_path: Path) -> Path:
    config_path = config_path.resolve()
    config = json.loads(config_path.read_text(encoding="utf-8"))
    required_top = {"run_tag", "out_dir", "grid", "artifact_sets", "jobs", "analyses"}
    missing_top = sorted(required_top - set(config))
    if missing_top:
        raise ValueError(f"pipeline config is missing {missing_top}")
    out_dir = _resolve(config_path, config["out_dir"])
    out_dir.mkdir(parents=True, exist_ok=True)

    loaded: dict[str, dict] = {}
    input_paths: dict[str, Path] = {"pipeline_config": config_path}
    for name, spec in sorted(config["artifact_sets"].items()):
        loaded[name], paths = _load_artifact_set(config_path, name, spec, config["grid"])
        input_paths.update({f"{name}:{key}": path for key, path in paths.items()})

    outputs: list[Path] = []
    run_records: list[dict] = []
    confirmatory_results: list[pd.DataFrame] = []
    alphas = [float(value) for value in config.get("alphas", [0.05, 0.10, 0.20])]
    delta = float(config.get("delta", 0.05))
    max_candidates = int(config.get("max_candidates", 20))
    for job in config["jobs"]:
        job_id = str(job["id"])
        names = list(job["artifact_sets"])
        unknown = sorted(set(names) - set(loaded))
        if unknown:
            raise ValueError(f"job {job_id!r} references unknown artifact sets {unknown}")
        views = pd.concat([loaded[name]["views"] for name in names], ignore_index=True)
        stats = pd.concat([loaded[name]["stats"] for name in names], ignore_index=True)
        residuals = pd.concat([loaded[name]["residuals"] for name in names], ignore_index=True)
        frame = views.merge(
            stats, on=["dataset", "class", "k_shot", "seed"],
            how="left", validate="many_to_one",
        )
        modes = job.get("source_modes", ["matched_condition"])
        for analysis in config["analyses"]:
            analysis_id = str(analysis["id"])
            normalization = str(analysis.get("normalization", "median_mad"))
            analysis_max_candidates = int(analysis.get("max_candidates", max_candidates))
            allocation = tuple(
                float(value) for value in analysis.get("partition_allocation", [0.5, 0.25, 0.25])
            )
            analysis_frame = frame.copy()
            analysis_frame["support_normalized_score"] = normalize_support_scores(
                analysis_frame, normalization
            )
            for mode in modes:
                tag = f"{config['run_tag']}__{job_id}__{analysis_id}__{mode}"
                results, candidates, partitions = evaluate_nested(
                    analysis_frame, alphas, delta, analysis_max_candidates, mode,
                    job.get("source_dataset"), job.get("target_dataset"), residuals,
                    analysis.get("source_class_limit"),
                    analysis.get("source_images_per_class"), normalization, allocation,
                )
                if results.empty or candidates.empty or not partitions:
                    raise RuntimeError(f"analysis {tag} produced incomplete outputs")
                results.insert(0, "analysis_id", analysis_id)
                results.insert(0, "job_id", job_id)
                result_path = out_dir / f"nested_sc3r_{tag}_detailed.csv"
                candidate_path = out_dir / f"nested_sc3r_{tag}_candidates.csv"
                partition_path = out_dir / f"nested_sc3r_{tag}_partitions.json"
                results.to_csv(result_path, index=False)
                candidates.to_csv(candidate_path, index=False)
                partition_path.write_text(
                    json.dumps(partitions, indent=2, sort_keys=True) + "\n", encoding="utf-8"
                )
                outputs.extend([result_path, candidate_path, partition_path])
                run_records.append({
                    "tag": tag, "job": job_id, "analysis": analysis_id,
                    "source_mode": mode, "normalization": normalization,
                    "source_class_limit": analysis.get("source_class_limit"),
                    "source_images_per_class": analysis.get("source_images_per_class"),
                    "max_candidates": analysis_max_candidates,
                    "partition_allocation": list(allocation),
                    "n_result_rows": len(results), "n_candidate_rows": len(candidates),
                    "methods": sorted(results.method.unique().tolist()),
                })
                if bool(analysis.get("confirmatory", False)):
                    confirmatory_results.append(results)

    if not confirmatory_results:
        raise ValueError("At least one analysis must set confirmatory=true")
    all_methods = pd.concat(confirmatory_results, ignore_index=True)
    all_methods_path = out_dir / f"sc3r_confirmatory_all_methods_{config['run_tag']}.csv"
    all_methods.to_csv(all_methods_path, index=False)
    simultaneous = compare(
        all_methods, "target_only", ["nested_sc3r", "pooled_source_conformal"],
        ["false_alarm_rate", "power", "alarm_precision"],
        int(config.get("bootstrap_iterations", 20000)),
        int(config.get("bootstrap_seed", 0)),
        float(config.get("family_alpha", 0.05)), "bonferroni",
    )
    if simultaneous.empty:
        raise RuntimeError("Confirmatory comparison produced no paired cells")
    simultaneous_path = out_dir / f"sc3r_confirmatory_simultaneous_{config['run_tag']}.csv"
    simultaneous.to_csv(simultaneous_path, index=False)
    outputs.extend([all_methods_path, simultaneous_path])
    paired_cells = paired_cell_audit(all_methods)
    summary = aggregate_cells(paired_cells)
    gate = build_empirical_gate_report(summary, simultaneous)
    paired_path = out_dir / f"nested_sc3r_{config['run_tag']}_paired_cells.csv"
    summary_path = out_dir / f"nested_sc3r_{config['run_tag']}_summary.csv"
    gate_path = out_dir / f"nested_sc3r_{config['run_tag']}_empirical_gate.json"
    paired_cells.to_csv(paired_path, index=False)
    summary.to_csv(summary_path, index=False)
    gate_path.write_text(
        json.dumps(gate, indent=2, sort_keys=True, allow_nan=False) + "\n", encoding="utf-8"
    )
    outputs.extend([paired_path, summary_path, gate_path])
    table_paths = []
    for name, content in build_latex_tables(summary).items():
        table_path = out_dir / name
        table_path.write_text(content, encoding="utf-8")
        table_paths.append(table_path)
    outputs.extend(table_paths)

    manifest = {
        "run_tag": config["run_tag"],
        "config": str(config_path),
        "environment": {
            "python": sys.version,
            "platform": platform.platform(),
            "numpy": np.__version__,
            "pandas": pd.__version__,
            "scikit_learn": sklearn.__version__,
            "git": _git_state(),
        },
        "inputs": {name: {"path": str(path), "sha256": _sha256(path)} for name, path in sorted(input_paths.items())},
        "artifact_audits": {name: loaded[name]["audit"] for name in sorted(loaded)},
        "runs": run_records,
        "confirmatory_family": {
            "baseline": "target_only",
            "candidates": ["nested_sc3r", "pooled_source_conformal"],
            "metrics": ["false_alarm_rate", "power", "alarm_precision"],
            "family_alpha": float(config.get("family_alpha", 0.05)),
            "multiplicity": "bonferroni",
            "family_size": int(simultaneous.family_size.iloc[0]),
        },
        "empirical_target_gate": {
            "claim_boundary": gate["claim_boundary"],
            "minimum_nonzero_threshold_rate": gate["minimum_nonzero_threshold_rate"],
            "n_gate_cells": gate["n_gate_cells"],
            "n_empirical_pass": gate["n_empirical_pass"],
            "n_empirical_fail": gate["n_empirical_fail"],
        },
        "outputs": {path.name: {"path": str(path), "sha256": _sha256(path)} for path in outputs},
    }
    manifest_path = out_dir / f"cpu_pipeline_manifest_{config['run_tag']}.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return manifest_path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()
    manifest = run_pipeline(Path(args.config))
    print(f"CPU submission pipeline completed: {manifest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
