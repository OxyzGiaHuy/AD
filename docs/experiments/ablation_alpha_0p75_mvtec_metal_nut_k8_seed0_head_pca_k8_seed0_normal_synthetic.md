# Run ablation_alpha_0p75_mvtec_metal_nut_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_metal_nut_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9906643580266864`
- `auroc`: `0.9643206256109482`
- `brier`: `0.15547301919745318`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2454879377199256`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.004108921940559927`
- `max_f1`: `0.9735449735449735`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.49423769110690047`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_metal_nut_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
