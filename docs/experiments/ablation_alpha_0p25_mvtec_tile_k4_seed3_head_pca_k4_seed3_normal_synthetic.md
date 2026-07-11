# Run ablation_alpha_0p25_mvtec_tile_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_tile_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9949779660024834`
- `auroc`: `0.9884559884559885`
- `brier`: `0.22055400973488368`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.25772497236219233`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0028222393499225634`
- `max_f1`: `0.9882352941176471`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6340940010615788`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_tile_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
