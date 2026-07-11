# Run calib_subspace_head_mvtec_wood_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/calib_subspace_head_mvtec_wood_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9878332299731146`
- `auroc`: `0.9657894736842105`
- `brier`: `0.13156505985706948`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1497920316797269`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0012894800003570846`
- `max_f1`: `0.9672131147540983`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.0002286052463107`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/calib_subspace_head_mvtec_wood_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
