# Run calib_subspace_head_mvtec_tile_k2_seed1_calib_subspace_head_k2_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/calib_subspace_head_mvtec_tile_k2_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9913061718158387`
- `auroc`: `0.9787157287157288`
- `brier`: `0.17911327987630296`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1955644394008395`
- `k_shot`: `2`
- `latency_sec_per_image`: `0.0013156794489194185`
- `max_f1`: `0.9585798816568047`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.8748293931298342`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `2738`

## Notes

- Predictions written to outputs/calib_subspace_head_mvtec_tile_k2_seed1_calib_subspace_head_k2_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
