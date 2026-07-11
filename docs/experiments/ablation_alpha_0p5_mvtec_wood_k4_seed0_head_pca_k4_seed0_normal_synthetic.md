# Run ablation_alpha_0p5_mvtec_wood_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_wood_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9976016584329718`
- `auroc`: `0.9921052631578947`
- `brier`: `0.18980866670061214`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.20407686505136619`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.00309947361768801`
- `max_f1`: `0.9752066115702479`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5695994744852695`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_wood_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
