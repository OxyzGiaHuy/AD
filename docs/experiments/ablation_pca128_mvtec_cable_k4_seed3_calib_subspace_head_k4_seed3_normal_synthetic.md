# Run ablation_pca128_mvtec_cable_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_cable_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9351077000454929`
- `auroc`: `0.8787481259370314`
- `brier`: `0.3417419341665108`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3523625271519026`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0021443551033735273`
- `max_f1`: `0.8666666666666667`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.8572662356772627`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_cable_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
