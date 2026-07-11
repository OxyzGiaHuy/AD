# Run ablation_alpha_0p75_mvtec_toothbrush_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_toothbrush_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9851801934127202`
- `auroc`: `0.9611111111111111`
- `brier`: `0.18712106206445855`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12828147269430618`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0035517941273394086`
- `max_f1`: `0.9354838709677419`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5593602426947388`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_toothbrush_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
