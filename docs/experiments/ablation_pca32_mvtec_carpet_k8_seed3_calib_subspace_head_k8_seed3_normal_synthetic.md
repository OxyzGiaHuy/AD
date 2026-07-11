# Run ablation_pca32_mvtec_carpet_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_carpet_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9962841285955003`
- `auroc`: `0.9883627608346709`
- `brier`: `0.10902343528026616`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12498633296061783`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0018560496660379262`
- `max_f1`: `0.978021978021978`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.48242145833127076`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_carpet_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
