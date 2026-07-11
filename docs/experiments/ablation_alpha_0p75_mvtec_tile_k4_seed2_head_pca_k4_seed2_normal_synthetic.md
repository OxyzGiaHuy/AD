# Run ablation_alpha_0p75_mvtec_tile_k4_seed2_head_pca_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_tile_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9889304023285784`
- `auroc`: `0.9736652236652237`
- `brier`: `0.1903645254313647`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.24558743859967616`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0019506265719731648`
- `max_f1`: `0.9655172413793104`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.568063604070696`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_tile_k4_seed2_head_pca_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
