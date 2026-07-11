# Run ablation_calib_upper_mvtec_pill_k4_seed3_calib_subspace_head_k4_seed3_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_pill_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9882480803622787`
- `auroc`: `0.9476075105996365`
- `brier`: `0.07540457954160083`
- `calibration_anomaly_val_count`: `14`
- `ece`: `0.071680701197752`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0025095034122856615`
- `max_f1`: `0.9538461538461539`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.24758044878273344`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_pill_k4_seed3_calib_subspace_head_k4_seed3_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
