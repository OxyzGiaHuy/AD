# Run head_pca_mvtec_tile_k2_seed1_head_pca_k2_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/head_pca_mvtec_tile_k2_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9913061718158387`
- `auroc`: `0.9787157287157288`
- `brier`: `0.27619597284073044`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.44699996658879465`
- `k_shot`: `2`
- `latency_sec_per_image`: `0.001596867528736082`
- `max_f1`: `0.9585798816568047`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.7455961275206109`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `2738`

## Notes

- Predictions written to outputs/head_pca_mvtec_tile_k2_seed1_head_pca_k2_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
