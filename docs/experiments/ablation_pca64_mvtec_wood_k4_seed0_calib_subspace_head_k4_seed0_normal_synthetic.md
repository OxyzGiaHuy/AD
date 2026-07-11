# Run ablation_pca64_mvtec_wood_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_wood_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.978614829115624`
- `auroc`: `0.9394736842105263`
- `brier`: `0.1592184767036893`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.18106084062328826`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0014631774370806128`
- `max_f1`: `0.9375`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.2389881745845126`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_wood_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
