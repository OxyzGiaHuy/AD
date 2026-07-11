from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.calibration.offline_sage_gate import (
    RidgeECERegressor,
    SoftmaxLinearGate,
    hierarchical_shared_dynamic_choice,
    risk_aware_choice,
    standardize_train_test,
    topk_soft_choice,
)

CALIBRATION_EXPERTS = ["vector_platt", "shift_aware_vector_platt", "weighted_platt"]
VIEW_EXPERTS = ["vector_platt", "shift_aware_vector_platt", "weighted_platt", "anchored_structured_gate"]


def read_csv(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def load_cases(paths: list[Path], expert_names: list[str]) -> tuple[list[tuple], dict[tuple, dict[str, dict]]]:
    by_case: dict[tuple, dict[str, dict]] = defaultdict(dict)
    for path in paths:
        for row in read_csv(path):
            if row["method"] not in expert_names:
                continue
            key = (row["dataset"], row["class"], int(row["k_shot"]), int(row["seed"]), row["corruption"])
            by_case[key][row["method"]] = row
    keys = [key for key, methods in by_case.items() if all(name in methods for name in expert_names)]
    return sorted(keys), by_case


def one_hot(value: str, choices: list[str]) -> list[float]:
    return [1.0 if value == c else 0.0 for c in choices]


def build_matrices(keys: list[tuple], by_case: dict[tuple, dict[str, dict]], expert_names: list[str]) -> tuple[np.ndarray, np.ndarray, np.ndarray, list[str]]:
    corruptions = sorted({key[4] for key in keys})
    datasets = sorted({key[0] for key in keys})
    feature_names = [
        "bias_free_log_k",
        "seed_scaled",
        "n_eff_ratio",
        "domain_shift_strength",
        "domain_confidence",
        "pca_concentration",
        "log_n_eff",
    ] + [f"corr={c}" for c in corruptions] + [f"dataset={d}" for d in datasets]
    x_rows = []
    ece_rows = []
    vector = []
    for key in keys:
        dataset, _cls, k, seed, corruption = key
        base = by_case[key]["vector_platt"]
        n_eff = float(base["n_eff"])
        n_eff_ratio = float(base["n_eff_ratio"])
        domain_conf = float(base["domain_confidence"])
        pca_conc = float(base["pca_concentration"])
        x_rows.append(
            [
                np.log(float(k)),
                seed / 4.0,
                n_eff_ratio,
                2.0 * abs(domain_conf - 0.5),
                domain_conf,
                pca_conc,
                np.log(max(n_eff, 1e-6)),
            ]
            + one_hot(corruption, corruptions)
            + one_hot(dataset, datasets)
        )
        vals = [float(by_case[key][name]["ece"]) for name in expert_names]
        ece_rows.append(vals)
        vector.append(float(base["ece"]))
    return np.asarray(x_rows, dtype=np.float64), np.asarray(ece_rows, dtype=np.float64), np.asarray(vector, dtype=np.float64), feature_names


def summarize_choice(name: str, split: str, keys: list[tuple], expert_names: list[str], ece: np.ndarray, vector: np.ndarray, choice: np.ndarray) -> dict:
    chosen_ece = ece[np.arange(len(choice)), choice]
    usage = Counter(expert_names[int(i)] for i in choice)
    no_harm = int(np.sum(chosen_ece <= vector + 0.01))
    return {
        "gate": name,
        "dataset": "+".join(sorted({k[0] for k in keys})),
        "split": split,
        "expert_pool": ";".join(expert_names),
        "n_cases": len(keys),
        "mean_ece": float(np.mean(chosen_ece)),
        "mean_vector_ece": float(np.mean(vector)),
        "mean_delta_vs_vector": float(np.mean(chosen_ece - vector)),
        "worst_ece": float(np.max(chosen_ece)),
        "no_harm_count": no_harm,
        "no_harm_total": len(keys),
        "no_harm_rate": float(no_harm / max(len(keys), 1)),
        "usage": ";".join(f"{k}:{usage.get(k, 0)}" for k in expert_names),
    }


def evaluate_split(keys: list[tuple], by_case: dict[tuple, dict[str, dict]], expert_names: list[str], train_idx: np.ndarray, test_idx: np.ndarray, split_name: str) -> list[dict]:
    x, ece, vector, _ = build_matrices(keys, by_case, expert_names)
    x_train, x_test, _, _ = standardize_train_test(x[train_idx], x[test_idx])
    ece_train = ece[train_idx]
    ece_test = ece[test_idx]
    vector_test = vector[test_idx]
    test_keys = [keys[int(i)] for i in test_idx]
    anchor_idx = expert_names.index("vector_platt")
    oracle_choice = ece_test.argmin(axis=1)
    rows = [summarize_choice("oracle_case_best", split_name, test_keys, expert_names, ece_test, vector_test, oracle_choice)]

    y_best = ece_train.argmin(axis=1)
    clf = SoftmaxLinearGate(lr=0.04, steps=1800, l2=5e-3, seed=7).fit(x_train, y_best)
    pred_choice = clf.predict(x_test)
    rows.append(summarize_choice("class_heldout_logistic_top1", split_name, test_keys, expert_names, ece_test, vector_test, pred_choice))
    soft_ece = topk_soft_choice(clf.predict_proba(x_test), ece_test, k=min(2, len(expert_names)))
    rows.append(
        {
            **summarize_choice("class_heldout_logistic_top2_soft", split_name, test_keys, expert_names, ece_test, vector_test, pred_choice),
            "mean_ece": float(np.mean(soft_ece)),
            "mean_delta_vs_vector": float(np.mean(soft_ece - vector_test)),
            "worst_ece": float(np.max(soft_ece)),
            "no_harm_count": int(np.sum(soft_ece <= vector_test + 0.01)),
            "no_harm_rate": float(np.mean(soft_ece <= vector_test + 0.01)),
            "usage": "soft_top2",
        }
    )

    reg = RidgeECERegressor(l2=0.1).fit(x_train, ece_train)
    pred_ece = reg.predict(x_test)
    for margin in [0.0, 0.005, 0.01, 0.02]:
        choice = risk_aware_choice(pred_ece, anchor_idx, margin=margin)
        rows.append(summarize_choice(f"risk_aware_margin_{margin:g}", split_name, test_keys, expert_names, ece_test, vector_test, choice))

    dynamic_labels = (ece_train.min(axis=1) < ece_train[:, anchor_idx] - 0.005).astype(np.int64)
    if dynamic_labels.max() == dynamic_labels.min():
        dynamic_prob = np.full(len(test_idx), float(dynamic_labels[0]), dtype=np.float64)
    else:
        shared_gate = SoftmaxLinearGate(lr=0.04, steps=1200, l2=5e-3, seed=11).fit(x_train, dynamic_labels)
        dynamic_prob = shared_gate.predict_proba(x_test)[:, 1]
    dynamic_indices = [i for i, name in enumerate(expert_names) if name != "vector_platt"]
    if dynamic_indices:
        y_dyn = ece_train[:, dynamic_indices].argmin(axis=1)
        dyn_gate = SoftmaxLinearGate(lr=0.04, steps=1200, l2=5e-3, seed=13).fit(x_train, y_dyn)
        dyn_probs = dyn_gate.predict_proba(x_test)
    else:
        dyn_probs = np.zeros((len(test_idx), 0), dtype=np.float64)
    for threshold in [0.5, 0.6, 0.7]:
        choice = hierarchical_shared_dynamic_choice(dynamic_prob, dyn_probs, dynamic_indices, anchor_idx, threshold=threshold)
        rows.append(summarize_choice(f"sage_hier_shared_dynamic_t{threshold:g}", split_name, test_keys, expert_names, ece_test, vector_test, choice))
    return rows


def leave_one_class_out(keys: list[tuple], by_case: dict[tuple, dict[str, dict]], expert_names: list[str]) -> list[dict]:
    rows = []
    arr = np.arange(len(keys))
    for dataset in sorted({k[0] for k in keys}):
        classes = sorted({k[1] for k in keys if k[0] == dataset})
        for cls in classes:
            test_idx = np.asarray([i for i, k in enumerate(keys) if k[0] == dataset and k[1] == cls], dtype=np.int64)
            train_idx = np.asarray([i for i, k in enumerate(keys) if not (k[0] == dataset and k[1] == cls)], dtype=np.int64)
            rows.extend(evaluate_split(keys, by_case, expert_names, train_idx, test_idx, f"loco:{dataset}:{cls}"))
    return rows


def cross_dataset(keys: list[tuple], by_case: dict[tuple, dict[str, dict]], expert_names: list[str]) -> list[dict]:
    rows = []
    for train_dataset, test_dataset in [("visa", "mvtec"), ("mvtec", "visa")]:
        train_idx = np.asarray([i for i, k in enumerate(keys) if k[0] == train_dataset], dtype=np.int64)
        test_idx = np.asarray([i for i, k in enumerate(keys) if k[0] == test_dataset], dtype=np.int64)
        if len(train_idx) and len(test_idx):
            rows.extend(evaluate_split(keys, by_case, expert_names, train_idx, test_idx, f"cross:{train_dataset}_to_{test_dataset}"))
    return rows


def aggregate(rows: list[dict]) -> list[dict]:
    groups: dict[tuple, list[dict]] = defaultdict(list)
    for row in rows:
        split_group = row["split"].split(":")[0]
        if row["split"].startswith("cross:"):
            split_group = row["split"]
        groups[(row["expert_pool"], split_group, row["gate"])].append(row)
    out = []
    for (pool, split_group, gate), group in sorted(groups.items()):
        n = sum(int(r["n_cases"]) for r in group)
        mean_ece = sum(float(r["mean_ece"]) * int(r["n_cases"]) for r in group) / max(n, 1)
        mean_vec = sum(float(r["mean_vector_ece"]) * int(r["n_cases"]) for r in group) / max(n, 1)
        no = sum(int(r["no_harm_count"]) for r in group)
        total = sum(int(r["no_harm_total"]) for r in group)
        out.append(
            {
                "expert_pool": pool,
                "split_group": split_group,
                "gate": gate,
                "n_cases": n,
                "mean_ece": mean_ece,
                "mean_vector_ece": mean_vec,
                "mean_delta_vs_vector": mean_ece - mean_vec,
                "no_harm_count": no,
                "no_harm_total": total,
                "no_harm_rate": no / max(total, 1),
            }
        )
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--visa", default="outputs/paper_tables/gated_shift_aware_anchored_adaptive_visa_full_k4k8_s0s2_detailed.csv")
    parser.add_argument("--mvtec", default="outputs/paper_tables/gated_shift_aware_anchored_adaptive_mvtec_full_k4k8_s0s2_detailed.csv")
    parser.add_argument("--out-dir", default="outputs/paper_tables")
    parser.add_argument("--run-tag", default="sage_style_gate_offline")
    args = parser.parse_args()

    paths = [Path(args.visa), Path(args.mvtec)]
    all_rows = []
    for pool_name, expert_names in [("calibration_experts", CALIBRATION_EXPERTS), ("view_experts", VIEW_EXPERTS)]:
        keys, by_case = load_cases(paths, expert_names)
        rows = leave_one_class_out(keys, by_case, expert_names) + cross_dataset(keys, by_case, expert_names)
        for row in rows:
            row["pool_name"] = pool_name
        all_rows.extend(rows)
    summary = aggregate(all_rows)
    out_dir = Path(args.out_dir)
    write_csv(out_dir / f"{args.run_tag}_detailed.csv", all_rows)
    write_csv(out_dir / f"{args.run_tag}_summary.csv", summary)
    print(f"wrote {len(all_rows)} detailed rows and {len(summary)} summary rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
