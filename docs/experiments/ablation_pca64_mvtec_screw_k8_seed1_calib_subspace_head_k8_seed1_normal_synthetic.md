# Run ablation_pca64_mvtec_screw_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_screw_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9048292220013348`
- `auroc`: `0.7981143676982988`
- `brier`: `0.16724842337886814`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1440816024783999`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0021940258098766207`
- `max_f1`: `0.875968992248062`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.5523967480214053`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_screw_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
