# Run ablation_pca64_mvtec_hazelnut_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_hazelnut_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9952928635184961`
- `auroc`: `0.9917857142857143`
- `brier`: `0.2912248692903188`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.31617569598284634`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002229490063407204`
- `max_f1`: `0.9722222222222222`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.6134187552440198`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_hazelnut_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
