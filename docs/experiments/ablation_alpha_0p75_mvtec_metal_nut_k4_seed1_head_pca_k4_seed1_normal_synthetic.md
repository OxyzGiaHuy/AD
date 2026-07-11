# Run ablation_alpha_0p75_mvtec_metal_nut_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_metal_nut_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9825602667770579`
- `auroc`: `0.9310850439882697`
- `brier`: `0.17109940362276047`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2640380372171816`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0027071363738049633`
- `max_f1`: `0.956989247311828`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.529572612633171`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_metal_nut_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
