# Run ablation_alpha_0p5_mvtec_metal_nut_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_metal_nut_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9876357747352584`
- `auroc`: `0.9501466275659824`
- `brier`: `0.18856395364068435`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2389109616694243`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002059924262373344`
- `max_f1`: `0.9578947368421052`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5680287553946463`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_metal_nut_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
