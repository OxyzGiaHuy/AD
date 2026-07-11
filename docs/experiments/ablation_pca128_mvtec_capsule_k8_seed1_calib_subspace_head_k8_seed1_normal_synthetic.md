# Run ablation_pca128_mvtec_capsule_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_capsule_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9905889984961505`
- `auroc`: `0.9525329078579976`
- `brier`: `0.11163007125425978`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.128305681099212`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0021271002902226014`
- `max_f1`: `0.9497716894977168`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.41146298300403034`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_capsule_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
