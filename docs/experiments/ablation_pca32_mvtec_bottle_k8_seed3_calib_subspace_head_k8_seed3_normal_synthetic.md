# Run ablation_pca32_mvtec_bottle_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_bottle_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9813545753401336`
- `auroc`: `0.9515873015873015`
- `brier`: `0.11199739149597362`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1348658554713208`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.004535360194473381`
- `max_f1`: `0.9545454545454546`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.6832039889348301`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_bottle_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
