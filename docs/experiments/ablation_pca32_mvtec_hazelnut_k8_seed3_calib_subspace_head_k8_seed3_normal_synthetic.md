# Run ablation_pca32_mvtec_hazelnut_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_hazelnut_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9583841146338804`
- `auroc`: `0.9339285714285714`
- `brier`: `0.2834078637148526`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.30079238062555136`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0035874733870679683`
- `max_f1`: `0.9014084507042254`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.9820206056961756`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_hazelnut_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
