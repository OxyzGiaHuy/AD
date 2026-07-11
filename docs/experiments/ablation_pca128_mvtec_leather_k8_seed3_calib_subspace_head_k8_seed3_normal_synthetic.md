# Run ablation_pca128_mvtec_leather_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_leather_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `1.0`
- `auroc`: `1.0`
- `brier`: `0.06399369035395808`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.08962816642897746`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002086655011460666`
- `max_f1`: `1.0`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.21460187289844207`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_leather_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
