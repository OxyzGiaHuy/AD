# Run ablation_alpha_0p5_mvtec_metal_nut_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_metal_nut_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9788023028554`
- `auroc`: `0.9266862170087976`
- `brier`: `0.17845775274632522`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.22779687798541523`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0019547399295412977`
- `max_f1`: `0.9565217391304348`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5463883828589071`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_metal_nut_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
