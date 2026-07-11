# Run ablation_calib_upper_mvtec_tile_k8_seed0_calib_subspace_head_k8_seed0_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_tile_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9917102522351177`
- `auroc`: `0.9828548644338118`
- `brier`: `0.049322045450052095`
- `calibration_anomaly_val_count`: `8`
- `ece`: `0.0934376642278849`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002787603355875803`
- `max_f1`: `0.9806451612903225`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.18265943523048597`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_tile_k8_seed0_calib_subspace_head_k8_seed0_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
