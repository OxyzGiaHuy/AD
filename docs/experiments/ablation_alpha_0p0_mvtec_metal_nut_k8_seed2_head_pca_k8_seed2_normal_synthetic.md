# Run ablation_alpha_0p0_mvtec_metal_nut_k8_seed2_head_pca_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_metal_nut_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9950370483013878`
- `auroc`: `0.978494623655914`
- `brier`: `0.2518216400611525`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.4134552206682123`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.005944286303027816`
- `max_f1`: `0.9633507853403142`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6967536450390402`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_metal_nut_k8_seed2_head_pca_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
