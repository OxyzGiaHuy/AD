# Run ablation_alpha_1p0_mvtec_tile_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_tile_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8811397397103692`
- `auroc`: `0.7072510822510822`
- `brier`: `0.2013310605459313`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.004982624807928326`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0024295376979897166`
- `max_f1`: `0.8442211055276382`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5920607118058071`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_tile_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
