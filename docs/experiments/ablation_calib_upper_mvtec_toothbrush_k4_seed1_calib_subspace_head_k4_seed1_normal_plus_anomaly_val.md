# Run ablation_calib_upper_mvtec_toothbrush_k4_seed1_calib_subspace_head_k4_seed1_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_toothbrush_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9907448107448107`
- `auroc`: `0.9783950617283951`
- `brier`: `0.08027846599467085`
- `calibration_anomaly_val_count`: `3`
- `ece`: `0.1131000803449215`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0026625157453310797`
- `max_f1`: `0.9473684210526315`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.32349044716041925`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_toothbrush_k4_seed1_calib_subspace_head_k4_seed1_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
