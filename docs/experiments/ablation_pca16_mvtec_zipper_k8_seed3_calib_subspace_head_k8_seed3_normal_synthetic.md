# Run ablation_pca16_mvtec_zipper_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_zipper_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9810933539211368`
- `auroc`: `0.9340861344537815`
- `brier`: `0.0850721416131165`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.09383444683179139`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0017019234573012157`
- `max_f1`: `0.9477911646586346`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.42608416476325356`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_zipper_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
