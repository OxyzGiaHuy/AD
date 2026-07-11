# Run ablation_pca64_mvtec_hazelnut_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_hazelnut_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.987077719953576`
- `auroc`: `0.9764285714285714`
- `brier`: `0.29788522819876534`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3138187424025753`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0020887145095250825`
- `max_f1`: `0.9481481481481482`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.6615539664269416`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_hazelnut_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
