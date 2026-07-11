# Run ablation_calib_upper_mvtec_hazelnut_k1_seed0_calib_subspace_head_k1_seed0_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_hazelnut_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9757828309708644`
- `auroc`: `0.959920634920635`
- `brier`: `0.3156408307752939`
- `calibration_anomaly_val_count`: `7`
- `ece`: `0.3414934925662661`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002741713727851516`
- `max_f1`: `0.9230769230769231`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.9933142501255018`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_hazelnut_k1_seed0_calib_subspace_head_k1_seed0_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
