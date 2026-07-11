# Run ablation_calib_upper_mvtec_cable_k4_seed4_calib_subspace_head_k4_seed4_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_cable_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9456757974320713`
- `auroc`: `0.8953053593685085`
- `brier`: `0.28186150435652024`
- `calibration_anomaly_val_count`: `9`
- `ece`: `0.3097546903799612`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0025238184958485`
- `max_f1`: `0.8903225806451613`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.7986821313333907`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_cable_k4_seed4_calib_subspace_head_k4_seed4_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
