# Run ablation_calib_upper_mvtec_capsule_k1_seed1_calib_subspace_head_k1_seed1_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_capsule_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.826889311339547`
- `auroc`: `0.6152832674571805`
- `brier`: `0.15200743940207892`
- `calibration_anomaly_val_count`: `10`
- `ece`: `0.1531551629304886`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0027574592224154314`
- `max_f1`: `0.92018779342723`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.8647439306216002`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_capsule_k1_seed1_calib_subspace_head_k1_seed1_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
