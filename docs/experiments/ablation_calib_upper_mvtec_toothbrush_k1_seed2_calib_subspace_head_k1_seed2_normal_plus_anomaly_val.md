# Run ablation_calib_upper_mvtec_toothbrush_k1_seed2_calib_subspace_head_k1_seed2_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_toothbrush_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9616236350365823`
- `auroc`: `0.9197530864197531`
- `brier`: `0.17985303832808316`
- `calibration_anomaly_val_count`: `3`
- `ece`: `0.20559107569547797`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.004404810519936757`
- `max_f1`: `0.9285714285714286`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.6167536659689821`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_toothbrush_k1_seed2_calib_subspace_head_k1_seed2_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
