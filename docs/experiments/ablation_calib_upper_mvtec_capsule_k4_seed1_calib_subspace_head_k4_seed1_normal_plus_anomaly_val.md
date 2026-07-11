# Run ablation_calib_upper_mvtec_capsule_k4_seed1_calib_subspace_head_k4_seed1_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_capsule_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9703377974948599`
- `auroc`: `0.8805445761967501`
- `brier`: `0.11551641119026494`
- `calibration_anomaly_val_count`: `10`
- `ece`: `0.12201506766628052`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0023320318337102406`
- `max_f1`: `0.9282296650717703`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.3700214233048766`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_capsule_k4_seed1_calib_subspace_head_k4_seed1_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
