# Run ablation_pca128_mvtec_cable_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_cable_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9413520619616903`
- `auroc`: `0.8858695652173914`
- `brier`: `0.22917639854968105`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.23654663215391342`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0023354660967985787`
- `max_f1`: `0.8850574712643678`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.9942155446381152`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_cable_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
