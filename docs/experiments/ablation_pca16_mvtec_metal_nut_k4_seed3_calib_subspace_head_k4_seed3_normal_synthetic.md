# Run ablation_pca16_mvtec_metal_nut_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_metal_nut_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9527833111730547`
- `auroc`: `0.855327468230694`
- `brier`: `0.14005369281072408`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1361239029013593`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0013868624263483544`
- `max_f1`: `0.9381443298969072`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.4827708203329729`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_metal_nut_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
