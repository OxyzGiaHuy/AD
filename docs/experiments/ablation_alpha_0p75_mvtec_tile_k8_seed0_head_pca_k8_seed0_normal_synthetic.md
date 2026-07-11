# Run ablation_alpha_0p75_mvtec_tile_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_tile_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9943254668801103`
- `auroc`: `0.987012987012987`
- `brier`: `0.17937467515473893`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3433471133566311`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0034544865131123452`
- `max_f1`: `0.9767441860465116`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5447559856413898`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_tile_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
