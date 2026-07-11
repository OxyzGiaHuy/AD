# Run ablation_alpha_1p0_mvtec_wood_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_wood_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9871817863898613`
- `auroc`: `0.9706140350877193`
- `brier`: `0.173669406070471`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.19804824379426011`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.003361466588287414`
- `max_f1`: `0.9917355371900827`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.529963401550367`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_wood_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
