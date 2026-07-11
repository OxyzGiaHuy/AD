# Run ablation_pca32_mvtec_tile_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_tile_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9901344772238373`
- `auroc`: `0.9761904761904762`
- `brier`: `0.1870939531371081`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.20929853429094475`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0025578707647629273`
- `max_f1`: `0.96`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `1.3810541702375525`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_tile_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
