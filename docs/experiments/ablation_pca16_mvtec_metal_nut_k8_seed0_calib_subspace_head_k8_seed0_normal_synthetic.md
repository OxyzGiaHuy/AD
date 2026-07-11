# Run ablation_pca16_mvtec_metal_nut_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_metal_nut_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9225968335539347`
- `auroc`: `0.7756598240469208`
- `brier`: `0.12540728045521735`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.13261334730831664`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.001347941289777341`
- `max_f1`: `0.9246231155778895`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.7254698743793855`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_metal_nut_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
