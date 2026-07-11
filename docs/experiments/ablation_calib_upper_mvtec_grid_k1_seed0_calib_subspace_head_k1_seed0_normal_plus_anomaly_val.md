# Run ablation_calib_upper_mvtec_grid_k1_seed0_calib_subspace_head_k1_seed0_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_grid_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9824712575335445`
- `auroc`: `0.9578754578754579`
- `brier`: `0.19292589469383256`
- `calibration_anomaly_val_count`: `5`
- `ece`: `0.21517822166828263`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002613320436379681`
- `max_f1`: `0.9369369369369369`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.6883981885753555`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_grid_k1_seed0_calib_subspace_head_k1_seed0_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
