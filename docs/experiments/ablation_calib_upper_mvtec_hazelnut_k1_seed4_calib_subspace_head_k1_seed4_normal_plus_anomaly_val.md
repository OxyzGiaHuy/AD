# Run ablation_calib_upper_mvtec_hazelnut_k1_seed4_calib_subspace_head_k1_seed4_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_hazelnut_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.981347974563023`
- `auroc`: `0.9753968253968254`
- `brier`: `0.29730299858001186`
- `calibration_anomaly_val_count`: `7`
- `ece`: `0.3297695546474272`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0022163155841306574`
- `max_f1`: `0.9538461538461539`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.8980331781009087`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_hazelnut_k1_seed4_calib_subspace_head_k1_seed4_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
