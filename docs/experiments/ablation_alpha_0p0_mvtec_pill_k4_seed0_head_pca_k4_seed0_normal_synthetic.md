# Run ablation_alpha_0p0_mvtec_pill_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_pill_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9907719851443024`
- `auroc`: `0.9549918166939444`
- `brier`: `0.23983094122134013`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3462704393321168`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.004425954464042258`
- `max_f1`: `0.9608540925266904`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6727908639458131`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_pill_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
