# Run ablation_pca32_mvtec_cable_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_cable_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9209968998382528`
- `auroc`: `0.8562593703148426`
- `brier`: `0.35247876080491786`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.33958793044090274`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001581043762465318`
- `max_f1`: `0.8415300546448088`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `1.2112411567788823`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_cable_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
