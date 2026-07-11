# Run ablation_alpha_0p5_mvtec_metal_nut_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_metal_nut_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9930019581792259`
- `auroc`: `0.9731182795698925`
- `brier`: `0.18388105401683544`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.36144078296163806`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0023282183253246803`
- `max_f1`: `0.9787234042553191`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5583582526362069`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_metal_nut_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
