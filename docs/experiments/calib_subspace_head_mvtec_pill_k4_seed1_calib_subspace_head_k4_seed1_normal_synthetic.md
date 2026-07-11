# Run calib_subspace_head_mvtec_pill_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/calib_subspace_head_mvtec_pill_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.98423140948906`
- `auroc`: `0.9236224768139661`
- `brier`: `0.11652830779947297`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1238140428486185`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0012965408337865761`
- `max_f1`: `0.9444444444444444`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.6656127217175007`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/calib_subspace_head_mvtec_pill_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
