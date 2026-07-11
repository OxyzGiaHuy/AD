# Run ablation_alpha_0p75_mvtec_toothbrush_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_toothbrush_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9615533792588008`
- `auroc`: `0.9027777777777778`
- `brier`: `0.19774602479935877`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.042383606944765354`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0037557391361111685`
- `max_f1`: `0.9032258064516129`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5838423055883342`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_toothbrush_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
