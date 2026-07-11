# Run ablation_pca128_mvtec_carpet_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_carpet_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9974843245059981`
- `auroc`: `0.9919743178170144`
- `brier`: `0.06973011222770893`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.09207596613937974`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0037605447264818046`
- `max_f1`: `0.978021978021978`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.3997714798296909`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_carpet_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
