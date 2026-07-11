# Run ablation_calib_upper_mvtec_screw_k8_seed3_calib_subspace_head_k8_seed3_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_screw_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8922120646600652`
- `auroc`: `0.7976513098464318`
- `brier`: `0.15781273733982604`
- `calibration_anomaly_val_count`: `11`
- `ece`: `0.14656317069026445`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.00201124820433207`
- `max_f1`: `0.8859649122807017`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.5883734792365728`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_screw_k8_seed3_calib_subspace_head_k8_seed3_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
