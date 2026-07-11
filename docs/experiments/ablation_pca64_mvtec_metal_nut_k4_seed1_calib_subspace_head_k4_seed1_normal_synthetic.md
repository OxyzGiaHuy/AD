# Run ablation_pca64_mvtec_metal_nut_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_metal_nut_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9880319525775595`
- `auroc`: `0.9525904203323559`
- `brier`: `0.14855354630372083`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.16482984812363333`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0014112765698329262`
- `max_f1`: `0.9518716577540107`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.0231844869510762`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_metal_nut_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
