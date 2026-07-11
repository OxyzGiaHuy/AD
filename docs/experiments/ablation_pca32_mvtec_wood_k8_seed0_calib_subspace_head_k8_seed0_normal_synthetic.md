# Run ablation_pca32_mvtec_wood_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_wood_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.98349883498292`
- `auroc`: `0.9508771929824561`
- `brier`: `0.1450818759655013`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.16432931538246856`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0022905376280033135`
- `max_f1`: `0.9411764705882353`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.8945589231253653`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_wood_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
