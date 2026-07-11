# Run head_pca_mvtec_tile_k2_seed2_head_pca_k2_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/head_pca_mvtec_tile_k2_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9892941160870627`
- `auroc`: `0.974025974025974`
- `brier`: `0.25386922662738726`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.30082409096579266`
- `k_shot`: `2`
- `latency_sec_per_image`: `0.001606865141254205`
- `max_f1`: `0.96`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.7008433631873365`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `2738`

## Notes

- Predictions written to outputs/head_pca_mvtec_tile_k2_seed2_head_pca_k2_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
