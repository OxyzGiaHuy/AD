# Run ablation_alpha_1p0_mvtec_tile_k1_seed3_head_pca_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_tile_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9382807442928222`
- `auroc`: `0.8297258297258298`
- `brier`: `0.20046710865243664`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.009132636917961965`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0017778163409640647`
- `max_f1`: `0.8502994011976048`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5900489018633962`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_tile_k1_seed3_head_pca_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
