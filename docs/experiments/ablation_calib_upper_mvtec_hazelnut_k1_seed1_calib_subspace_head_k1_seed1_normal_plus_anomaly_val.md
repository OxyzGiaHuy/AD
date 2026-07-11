# Run ablation_calib_upper_mvtec_hazelnut_k1_seed1_calib_subspace_head_k1_seed1_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_hazelnut_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9836052033185329`
- `auroc`: `0.9686507936507937`
- `brier`: `0.27144184089136225`
- `calibration_anomaly_val_count`: `7`
- `ece`: `0.31193663281144446`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0025435830782918095`
- `max_f1`: `0.944`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.8118630554424363`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_hazelnut_k1_seed1_calib_subspace_head_k1_seed1_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
