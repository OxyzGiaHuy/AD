# Run ablation_alpha_0p75_mvtec_cable_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_cable_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9474365424823862`
- `auroc`: `0.8984257871064468`
- `brier`: `0.23305006909491596`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.06977317452430724`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002917499244213104`
- `max_f1`: `0.8620689655172413`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6576905917061922`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_cable_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
