# Run calib_subspace_head_mvtec_tile_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/calib_subspace_head_mvtec_tile_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9916416013011432`
- `auroc`: `0.9801587301587301`
- `brier`: `0.1358353321024944`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.15330137203359956`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0013032952148435463`
- `max_f1`: `0.9655172413793104`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.5605862855060126`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/calib_subspace_head_mvtec_tile_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
