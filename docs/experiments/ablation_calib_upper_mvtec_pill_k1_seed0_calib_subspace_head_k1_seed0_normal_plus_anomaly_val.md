# Run ablation_calib_upper_mvtec_pill_k1_seed0_calib_subspace_head_k1_seed0_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_pill_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9795793982845886`
- `auroc`: `0.9097516656571775`
- `brier`: `0.11844599849349514`
- `calibration_anomaly_val_count`: `14`
- `ece`: `0.1165347966103772`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002349349834463176`
- `max_f1`: `0.9433962264150944`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.38235485051818235`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_pill_k1_seed0_calib_subspace_head_k1_seed0_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
