# Run ablation_calib_upper_mvtec_hazelnut_k8_seed2_calib_subspace_head_k8_seed2_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_hazelnut_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9967654589737608`
- `auroc`: `0.9948412698412699`
- `brier`: `0.05004027964135719`
- `calibration_anomaly_val_count`: `7`
- `ece`: `0.11824121101967339`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0020696976882161448`
- `max_f1`: `0.9763779527559056`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.18280343576757527`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_hazelnut_k8_seed2_calib_subspace_head_k8_seed2_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
