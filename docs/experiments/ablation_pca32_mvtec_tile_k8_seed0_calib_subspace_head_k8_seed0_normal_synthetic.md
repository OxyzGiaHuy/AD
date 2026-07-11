# Run ablation_pca32_mvtec_tile_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_tile_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9923344257579729`
- `auroc`: `0.9823232323232324`
- `brier`: `0.07207405258511022`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.11844233499887663`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002754004067208013`
- `max_f1`: `0.9767441860465116`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.23502180706027795`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_tile_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
