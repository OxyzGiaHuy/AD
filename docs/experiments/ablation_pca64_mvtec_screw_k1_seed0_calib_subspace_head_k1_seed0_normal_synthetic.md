# Run ablation_pca64_mvtec_screw_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_screw_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7991189282506898`
- `auroc`: `0.6171346587415454`
- `brier`: `0.25438708460842496`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2552190363407135`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001365794416051358`
- `max_f1`: `0.8764044943820225`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `2.869377836653162`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_screw_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
