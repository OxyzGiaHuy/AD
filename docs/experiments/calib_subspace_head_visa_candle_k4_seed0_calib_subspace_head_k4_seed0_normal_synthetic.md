# Run calib_subspace_head_visa_candle_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/calib_subspace_head_visa_candle_k4_seed0.yaml`
- Dataset: `visa`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8641686136450037`
- `auroc`: `0.8804`
- `brier`: `0.27345897242763484`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.303202051622793`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.006146008288487792`
- `max_f1`: `0.8442211055276382`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.509014709608142`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/calib_subspace_head_visa_candle_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
