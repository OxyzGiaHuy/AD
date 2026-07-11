# Run ablation_pca32_mvtec_carpet_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_carpet_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9991314288990252`
- `auroc`: `0.9971910112359551`
- `brier`: `0.08304186138883701`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.09631879949289515`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0027299245548808677`
- `max_f1`: `0.9834254143646409`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.33524018824886953`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_carpet_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
