# Run ablation_calib_upper_mvtec_zipper_k8_seed1_calib_subspace_head_k8_seed1_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_zipper_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9844070153440645`
- `auroc`: `0.9487847222222222`
- `brier`: `0.08610742678764631`
- `calibration_anomaly_val_count`: `11`
- `ece`: `0.09339475237232238`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0017941424090947423`
- `max_f1`: `0.9427312775330396`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.2989967587722844`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_zipper_k8_seed1_calib_subspace_head_k8_seed1_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
