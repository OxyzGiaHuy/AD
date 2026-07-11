# Run ablation_pca128_mvtec_cable_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_cable_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9372120042706679`
- `auroc`: `0.8847451274362819`
- `brier`: `0.1887908507315773`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.20033060474360054`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0023644860337177914`
- `max_f1`: `0.8777777777777778`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.7801959483961921`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_cable_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
