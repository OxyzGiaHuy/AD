# Run calib_subspace_head_mvtec_tile_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/calib_subspace_head_mvtec_tile_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9946211188685307`
- `auroc`: `0.9862914862914863`
- `brier`: `0.2712609971568062`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2764609430590247`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0012876012672980626`
- `max_f1`: `0.9655172413793104`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.6130580303734026`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/calib_subspace_head_mvtec_tile_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
