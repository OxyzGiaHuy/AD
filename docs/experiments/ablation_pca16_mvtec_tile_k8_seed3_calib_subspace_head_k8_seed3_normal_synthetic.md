# Run ablation_pca16_mvtec_tile_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_tile_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9924291753669582`
- `auroc`: `0.9819624819624819`
- `brier`: `0.15638637707745928`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.18710517892852807`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0015183225369606263`
- `max_f1`: `0.9704142011834319`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.4530294922512041`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_tile_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
