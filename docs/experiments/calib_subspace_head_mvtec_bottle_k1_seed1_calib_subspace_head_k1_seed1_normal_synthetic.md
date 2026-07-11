# Run calib_subspace_head_mvtec_bottle_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/calib_subspace_head_mvtec_bottle_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9719084306496563`
- `auroc`: `0.9246031746031746`
- `brier`: `0.24083546926419105`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2408982292715326`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001317535156765616`
- `max_f1`: `0.9333333333333333`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `2.5141161598793356`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/calib_subspace_head_mvtec_bottle_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
