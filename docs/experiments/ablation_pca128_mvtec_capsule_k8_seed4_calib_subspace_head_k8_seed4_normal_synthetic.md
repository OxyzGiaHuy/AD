# Run ablation_pca128_mvtec_capsule_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_capsule_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9732157385018406`
- `auroc`: `0.895492620662146`
- `brier`: `0.09886634929471891`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.10621007087739234`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.001615622475969069`
- `max_f1`: `0.9406392694063926`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.4292889685288637`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_capsule_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
