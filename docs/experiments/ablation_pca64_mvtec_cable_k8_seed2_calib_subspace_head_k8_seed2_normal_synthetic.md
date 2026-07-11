# Run ablation_pca64_mvtec_cable_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_cable_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9546808065217498`
- `auroc`: `0.9070464767616192`
- `brier`: `0.21783974653591387`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2278293558458487`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0018596572677294413`
- `max_f1`: `0.8953488372093024`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.7176193471872678`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_cable_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
