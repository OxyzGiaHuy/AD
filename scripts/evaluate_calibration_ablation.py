from __future__ import annotations

import argparse
import csv
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.calibration.platt import PlattScaler, VectorPlattScaler, entropy_binary
from src.config import load_config
from src.data.datasets import load_records
from src.data.sampling import evaluation_records, few_shot_support
from src.evaluation.metrics import summarize_binary
from src.models.baselines import build_model
from src.run_experiment import encode_with_cache, load_feature_cache_if_present
from src.utils.io import ensure_dir


class IsotonicCalibrator:
    def __init__(self):
        self.x_: np.ndarray | None = None
        self.y_: np.ndarray | None = None

    def fit(self, scores: np.ndarray, labels: np.ndarray) -> "IsotonicCalibrator":
        order = np.argsort(scores)
        x = np.asarray(scores, dtype=np.float64)[order]
        y = np.asarray(labels, dtype=np.float64)[order]
        weights = np.ones_like(y)
        vals = y.copy()
        starts = list(range(len(vals)))
        ends = list(range(len(vals)))
        w = weights.copy().tolist()
        v = vals.copy().tolist()
        i = 0
        while i < len(v) - 1:
            if v[i] <= v[i + 1]:
                i += 1
                continue
            total_w = w[i] + w[i + 1]
            total_v = (v[i] * w[i] + v[i + 1] * w[i + 1]) / total_w
            v[i] = total_v
            w[i] = total_w
            ends[i] = ends[i + 1]
            del v[i + 1], w[i + 1], starts[i + 1], ends[i + 1]
            if i:
                i -= 1
        fitted = np.empty_like(y)
        for value, start, end in zip(v, starts, ends):
            fitted[start : end + 1] = value
        self.x_ = x
        self.y_ = np.clip(fitted, 0.0, 1.0)
        return self

    def predict_proba(self, scores: np.ndarray) -> np.ndarray:
        if self.x_ is None or self.y_ is None:
            raise RuntimeError("fit first")
        return np.interp(scores.astype(np.float64), self.x_, self.y_, left=self.y_[0], right=self.y_[-1]).astype(np.float32)


def config_run_id(config: dict, k: int, seed: int) -> str:
    return f"{config.get('experiment', {}).get('name', 'experiment')}_calibration_ablation_k{k}_seed{seed}"


def get_features(config: dict, records, support, eval_records, k: int, seed: int):
    from src.backbones.dinov2 import build_backbone

    dataset_cfg = config.get("dataset", {})
    backbone_cfg = config.get("backbone", {})
    experiment_cfg = config.get("experiment", {})
    backbone_name = backbone_cfg.get("name", "dinov2_vits14")
    image_size = int(dataset_cfg.get("image_size", backbone_cfg.get("image_size", 518)))
    cache_dir = backbone_cfg.get("cache_dir", "outputs/feature_cache")
    dataset_name = dataset_cfg.get("name", "dataset")
    support_cache_name = f"{dataset_name}_support_{backbone_name}_k{k}_seed{seed}"
    eval_cache_name = f"{dataset_name}_eval_{backbone_name}"
    eval_cache_seed = 0 if backbone_name.startswith("dinov2") else seed
    support_batch = load_feature_cache_if_present(support, cache_dir, support_cache_name, seed, backbone_name, image_size)
    eval_batch = load_feature_cache_if_present(eval_records, cache_dir, eval_cache_name, seed, backbone_name, image_size, cache_seed=eval_cache_seed)
    if support_batch is None or eval_batch is None:
        backbone = build_backbone(backbone_name, device=experiment_cfg.get("device", "cuda"), image_size=image_size, batch_size=int(backbone_cfg.get("batch_size", 8)))
        if support_batch is None:
            support_batch = encode_with_cache(backbone, support, cache_dir, support_cache_name, seed, backbone_name, image_size)
        if eval_batch is None:
            eval_batch = encode_with_cache(backbone, eval_records, cache_dir, eval_cache_name, seed, backbone_name, image_size, cache_seed=eval_cache_seed)
    return support_batch.patch_features, eval_batch.patch_features


def evaluate_one(config: dict, k: int, seed: int) -> list[dict]:
    dataset_cfg = config.get("dataset", {})
    model_cfg = dict(config.get("model", {}))
    model_cfg["variant"] = "calib_subspace_head"
    model_cfg.setdefault("device", config.get("experiment", {}).get("device", "cuda"))
    records = load_records(dataset_cfg.get("name", "mvtec"), dataset_cfg.get("root"), dataset_cfg.get("classes", "all"))
    support = few_shot_support(records, k=k, seed=seed)
    eval_recs = evaluation_records(records)
    support_features, eval_features = get_features(config, records, support, eval_recs, k, seed)
    model = build_model("calib_subspace_head", support_features, model_cfg, seed=seed)
    support_scores, _ = model.score_images(support_features)
    raw_scores, _ = model.score_images(eval_features)
    labels = np.asarray([r.label for r in eval_recs], dtype=np.int64)
    synth_scores = support_scores + max(float(np.std(support_scores)), 1e-3) + 1e-3
    scalar_x = np.concatenate([support_scores, synth_scores])
    scalar_y = np.concatenate([np.zeros_like(support_scores), np.ones_like(synth_scores)])
    vector_support = model.calibration_features(support_features)
    vector_synth = model.synthetic_calibration_features(support_features, seed=seed, ratio=float(model_cfg.get("synthetic_anomaly_ratio", 1.0)))
    vector_x = np.concatenate([vector_support, vector_synth], axis=0)
    vector_y = np.concatenate([np.zeros(len(vector_support), dtype=np.float32), np.ones(len(vector_synth), dtype=np.float32)])
    eval_vec = model.calibration_features(eval_features)
    methods = {
        "raw_sigmoid": 1.0 / (1.0 + np.exp(-np.clip(raw_scores, -40, 40))),
        "scalar_platt": PlattScaler().fit(scalar_x, scalar_y).predict_proba(raw_scores),
        "isotonic": IsotonicCalibrator().fit(scalar_x, scalar_y).predict_proba(raw_scores),
        "vector_platt": VectorPlattScaler().fit(vector_x, vector_y, positive_indices=(0,)).predict_proba(eval_vec),
    }
    rows = []
    for method, probs in methods.items():
        metrics = summarize_binary(labels, raw_scores, probs, bins=int(config.get("calibration", {}).get("bins", 15)))
        rows.append({
            "dataset": dataset_cfg.get("name", "mvtec"),
            "class": dataset_cfg.get("classes", ["unknown"])[0],
            "k_shot": k,
            "seed": seed,
            "method": method,
            "entropy_mean": float(entropy_binary(probs).mean()),
            **metrics,
        })
    return rows


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader(); writer.writerows(rows)


def summarize(rows: list[dict]) -> list[dict]:
    from collections import defaultdict
    from statistics import mean, stdev
    groups = defaultdict(list)
    for row in rows:
        groups[(row["dataset"], row["method"], row["k_shot"])].append(row)
    out=[]
    for (dataset, method, k), group in sorted(groups.items()):
        base={"dataset":dataset,"method":method,"k_shot":k,"n":len(group)}
        for metric in ["auroc","ap","max_f1","ece","brier","nll","entropy_mean"]:
            vals=[float(r[metric]) for r in group if not np.isnan(float(r[metric]))]
            base[f"{metric}_mean"]=mean(vals) if vals else float("nan")
            base[f"{metric}_std"]=stdev(vals) if len(vals)>1 else 0.0
        out.append(base)
    return out


def main() -> int:
    parser=argparse.ArgumentParser()
    parser.add_argument("--run-list", required=True)
    parser.add_argument("--out-dir", default="outputs/paper_tables")
    parser.add_argument("--limit", type=int, default=None)
    args=parser.parse_args()
    configs=[Path(x.strip()) for x in Path(args.run_list).read_text(encoding="utf-8").splitlines() if x.strip()]
    configs=[p for p in configs if "calib_subspace_head" in p.name and ("_k1_" in p.name or "_k4_" in p.name or "_k8_" in p.name)]
    if args.limit:
        configs=configs[:args.limit]
    rows=[]
    for cfg_path in configs:
        cfg=load_config(cfg_path)
        for k in cfg.get("dataset",{}).get("k_shots",[1]):
            for seed in cfg.get("dataset",{}).get("seeds",[0]):
                rows.extend(evaluate_one(cfg,int(k),int(seed)))
    out=Path(args.out_dir)
    write_csv(out/"calibration_ablation_detailed.csv", rows)
    write_csv(out/"calibration_ablation_summary.csv", summarize(rows))
    print(f"runs={len(rows)}")
    print(out/"calibration_ablation_summary.csv")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
