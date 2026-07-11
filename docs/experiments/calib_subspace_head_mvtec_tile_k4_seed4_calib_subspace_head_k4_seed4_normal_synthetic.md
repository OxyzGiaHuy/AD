# Run calib_subspace_head_mvtec_tile_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/calib_subspace_head_mvtec_tile_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9931776691519542`
- `auroc`: `0.9841269841269841`
- `brier`: `0.08356553518157972`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.11408137734660992`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0013268883220660381`
- `max_f1`: `0.9824561403508771`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.39046553776050746`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/calib_subspace_head_mvtec_tile_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
