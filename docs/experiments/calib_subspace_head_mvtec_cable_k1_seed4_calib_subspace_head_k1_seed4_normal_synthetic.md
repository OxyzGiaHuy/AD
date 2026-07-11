# Run calib_subspace_head_mvtec_cable_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/calib_subspace_head_mvtec_cable_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.931379596429638`
- `auroc`: `0.8680659670164917`
- `brier`: `0.3866147005819812`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.38663912415504464`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0012929318100214004`
- `max_f1`: `0.847457627118644`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `5.138967889609638`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/calib_subspace_head_mvtec_cable_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
