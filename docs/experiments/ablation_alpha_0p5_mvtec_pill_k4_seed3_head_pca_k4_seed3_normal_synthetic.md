# Run ablation_alpha_0p5_mvtec_pill_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_pill_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9874088183621105`
- `auroc`: `0.9372613202400436`
- `brier`: `0.1715595312080942`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.30693070260350575`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0018779323129596824`
- `max_f1`: `0.952054794520548`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5325645514436806`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_pill_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
