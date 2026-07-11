# Run ablation_pca128_mvtec_cable_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_cable_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9410315842052555`
- `auroc`: `0.8976761619190404`
- `brier`: `0.2958639050230535`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3260731154680253`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0014239349588751793`
- `max_f1`: `0.8813559322033898`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.4006549966321782`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_cable_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
