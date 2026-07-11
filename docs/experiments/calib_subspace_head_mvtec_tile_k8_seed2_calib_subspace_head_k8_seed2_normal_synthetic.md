# Run calib_subspace_head_mvtec_tile_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/calib_subspace_head_mvtec_tile_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9889391911580325`
- `auroc`: `0.974025974025974`
- `brier`: `0.10998877834448882`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1309488591793766`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0012930375961666433`
- `max_f1`: `0.9651162790697675`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.7590529275501238`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/calib_subspace_head_mvtec_tile_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
