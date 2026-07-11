# Run ablation_calib_upper_mvtec_wood_k8_seed2_calib_subspace_head_k8_seed2_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_wood_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9743056054468526`
- `auroc`: `0.9337231968810916`
- `brier`: `0.09638932622899851`
- `calibration_anomaly_val_count`: `6`
- `ece`: `0.09775908452088702`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0033621166462767613`
- `max_f1`: `0.9310344827586207`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.3319003844205261`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_wood_k8_seed2_calib_subspace_head_k8_seed2_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
