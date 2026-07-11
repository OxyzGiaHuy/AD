# Run ablation_pca128_mvtec_hazelnut_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_hazelnut_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9931941716737015`
- `auroc`: `0.9882142857142857`
- `brier`: `0.2763446676348225`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3035458845171062`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.001886892200193622`
- `max_f1`: `0.9655172413793104`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.333748880780734`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_hazelnut_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
