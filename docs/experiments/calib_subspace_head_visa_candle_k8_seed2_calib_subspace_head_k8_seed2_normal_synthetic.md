# Run calib_subspace_head_visa_candle_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/calib_subspace_head_visa_candle_k8_seed2.yaml`
- Dataset: `visa`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8609578310050968`
- `auroc`: `0.886`
- `brier`: `0.19114179190715233`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.20871884806314484`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0092640327103436`
- `max_f1`: `0.8411214953271028`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.1133510763940386`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/calib_subspace_head_visa_candle_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
