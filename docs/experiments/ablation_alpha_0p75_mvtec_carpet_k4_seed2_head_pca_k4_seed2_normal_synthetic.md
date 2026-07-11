# Run ablation_alpha_0p75_mvtec_carpet_k4_seed2_head_pca_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_carpet_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9981259370410642`
- `auroc`: `0.9939807383627608`
- `brier`: `0.1704798322767183`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.27813842281317097`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0025389298128011897`
- `max_f1`: `0.978021978021978`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5281435747000022`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_carpet_k4_seed2_head_pca_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
