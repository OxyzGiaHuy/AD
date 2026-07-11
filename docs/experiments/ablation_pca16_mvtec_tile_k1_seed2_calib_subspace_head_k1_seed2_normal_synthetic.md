# Run ablation_pca16_mvtec_tile_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_tile_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9899664285167569`
- `auroc`: `0.9751082251082251`
- `brier`: `0.27712090919895893`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2793647590865437`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0013829638433252645`
- `max_f1`: `0.9534883720930233`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `3.4871577928000606`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_tile_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
