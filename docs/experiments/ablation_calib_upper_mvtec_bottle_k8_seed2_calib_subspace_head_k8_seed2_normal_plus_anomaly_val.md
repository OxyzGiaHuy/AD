# Run ablation_calib_upper_mvtec_bottle_k8_seed2_calib_subspace_head_k8_seed2_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_bottle_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9889412230740847`
- `auroc`: `0.9736842105263158`
- `brier`: `0.04669157293113643`
- `calibration_anomaly_val_count`: `6`
- `ece`: `0.07084172431911745`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0025613522036122037`
- `max_f1`: `0.9743589743589743`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.1790151696259681`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_bottle_k8_seed2_calib_subspace_head_k8_seed2_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
