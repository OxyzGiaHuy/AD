# Run ablation_alpha_0p0_mvtec_bottle_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_bottle_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9953837495276107`
- `auroc`: `0.9865079365079366`
- `brier`: `0.259510083075639`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3050263638956001`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0021641765642597013`
- `max_f1`: `0.984375`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.7120065237115223`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_bottle_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
