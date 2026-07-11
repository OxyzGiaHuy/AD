# Run calib_subspace_head_mvtec_bottle_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/calib_subspace_head_mvtec_bottle_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9895316790070026`
- `auroc`: `0.9706349206349206`
- `brier`: `0.15158573172321343`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.17538525013769243`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0013155703803142869`
- `max_f1`: `0.9612403100775194`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.951520973506995`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/calib_subspace_head_mvtec_bottle_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
