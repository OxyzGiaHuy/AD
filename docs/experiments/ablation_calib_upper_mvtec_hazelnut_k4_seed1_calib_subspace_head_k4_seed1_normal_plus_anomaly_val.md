# Run ablation_calib_upper_mvtec_hazelnut_k4_seed1_calib_subspace_head_k4_seed1_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_hazelnut_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9888812273525563`
- `auroc`: `0.9817460317460317`
- `brier`: `0.13777974839183638`
- `calibration_anomaly_val_count`: `7`
- `ece`: `0.20915829643462472`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0021413309156026656`
- `max_f1`: `0.9421487603305785`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.43807758436838923`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_hazelnut_k4_seed1_calib_subspace_head_k4_seed1_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
