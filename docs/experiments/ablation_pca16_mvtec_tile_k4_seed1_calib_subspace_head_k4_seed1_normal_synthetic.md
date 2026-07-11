# Run ablation_pca16_mvtec_tile_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_tile_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9912274891194047`
- `auroc`: `0.9790764790764791`
- `brier`: `0.20100489108009462`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2004266017013126`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002681087798033005`
- `max_f1`: `0.9642857142857143`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.6064444167226211`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_tile_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
