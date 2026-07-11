# Run ablation_pca64_mvtec_tile_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_tile_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9930653303096755`
- `auroc`: `0.9841269841269841`
- `brier`: `0.14942344407277688`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1720053279915681`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0026041532779096537`
- `max_f1`: `0.9824561403508771`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.6617811323062808`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_tile_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
