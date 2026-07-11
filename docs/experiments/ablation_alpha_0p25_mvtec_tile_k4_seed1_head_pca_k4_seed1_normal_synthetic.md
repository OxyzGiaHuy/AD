# Run ablation_alpha_0p25_mvtec_tile_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_tile_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9915576066081667`
- `auroc`: `0.9783549783549783`
- `brier`: `0.223909276732206`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.24110910372856334`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0026125695683762557`
- `max_f1`: `0.9700598802395209`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6408593721795037`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_tile_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
