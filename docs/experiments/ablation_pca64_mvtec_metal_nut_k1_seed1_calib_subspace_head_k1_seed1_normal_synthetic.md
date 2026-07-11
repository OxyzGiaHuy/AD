# Run ablation_pca64_mvtec_metal_nut_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_metal_nut_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9944208933801431`
- `auroc`: `0.9760508308895406`
- `brier`: `0.18990869968215557`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.19059756216795554`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0013985185681477837`
- `max_f1`: `0.9578947368421052`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.8096411228180567`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_metal_nut_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
