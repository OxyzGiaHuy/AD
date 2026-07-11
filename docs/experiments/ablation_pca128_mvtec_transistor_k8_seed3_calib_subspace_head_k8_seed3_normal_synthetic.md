# Run ablation_pca128_mvtec_transistor_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_transistor_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8378242937863114`
- `auroc`: `0.8733333333333333`
- `brier`: `0.2688576855585243`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.31117614394053816`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0024448287114501`
- `max_f1`: `0.7804878048780488`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.1157244988800692`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_transistor_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
