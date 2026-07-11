# Run ablation_calib_upper_mvtec_leather_k1_seed1_calib_subspace_head_k1_seed1_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_leather_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `1.0`
- `auroc`: `1.0`
- `brier`: `0.021468219832236946`
- `calibration_anomaly_val_count`: `9`
- `ece`: `0.06699601700124536`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002428318948849388`
- `max_f1`: `1.0`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.08400860836373687`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_leather_k1_seed1_calib_subspace_head_k1_seed1_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
