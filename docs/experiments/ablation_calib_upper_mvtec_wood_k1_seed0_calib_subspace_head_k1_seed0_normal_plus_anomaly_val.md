# Run ablation_calib_upper_mvtec_wood_k1_seed0_calib_subspace_head_k1_seed0_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_wood_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9785869476956992`
- `auroc`: `0.9463937621832359`
- `brier`: `0.1491045351842165`
- `calibration_anomaly_val_count`: `6`
- `ece`: `0.17325173583749223`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0029266725919426303`
- `max_f1`: `0.9454545454545454`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.4896156866769839`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_wood_k1_seed0_calib_subspace_head_k1_seed0_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
