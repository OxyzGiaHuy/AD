# Run ablation_alpha_0p25_mvtec_grid_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_grid_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9387167478326993`
- `auroc`: `0.8454469507101086`
- `brier`: `0.2282975224791104`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.27427278650112646`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0021278850065592006`
- `max_f1`: `0.8870967741935484`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6496022173080098`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_grid_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
