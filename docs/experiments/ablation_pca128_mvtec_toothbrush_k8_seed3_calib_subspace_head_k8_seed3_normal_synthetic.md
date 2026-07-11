# Run ablation_pca128_mvtec_toothbrush_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_toothbrush_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.978199771943662`
- `auroc`: `0.95`
- `brier`: `0.12345980304997382`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1410435776093177`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.003223927070697149`
- `max_f1`: `0.967741935483871`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.9610322828973794`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_toothbrush_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
