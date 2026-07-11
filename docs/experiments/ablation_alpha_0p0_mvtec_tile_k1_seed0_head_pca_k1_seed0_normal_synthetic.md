# Run ablation_alpha_0p0_mvtec_tile_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_tile_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9934380409059012`
- `auroc`: `0.9848484848484849`
- `brier`: `0.24813421167630817`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.41721503627605927`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0021366892525782953`
- `max_f1`: `0.9767441860465116`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6893936187616897`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_tile_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
