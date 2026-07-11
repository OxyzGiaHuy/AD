# Run ablation_alpha_0p0_mvtec_metal_nut_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_metal_nut_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9895741836733822`
- `auroc`: `0.958455522971652`
- `brier`: `0.2469424222874107`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.4042480950770171`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.003220746536617694`
- `max_f1`: `0.9533678756476683`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6870052177137995`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_metal_nut_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
