# Run ablation_pca32_mvtec_tile_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_tile_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9905911102488891`
- `auroc`: `0.9776334776334776`
- `brier`: `0.11175412609680098`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1361127331998184`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0017172858501091981`
- `max_f1`: `0.9647058823529412`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.6939298537956944`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_tile_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
