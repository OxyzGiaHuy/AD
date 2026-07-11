# Run ablation_alpha_0p5_mvtec_tile_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_tile_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9943645562723886`
- `auroc`: `0.987012987012987`
- `brier`: `0.19723708751153254`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3616152869330513`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.003397368754331882`
- `max_f1`: `0.9824561403508771`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5851380108043869`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_tile_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
