# Run head_pca_mvtec_tile_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/head_pca_mvtec_tile_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9920414996777024`
- `auroc`: `0.9812409812409812`
- `brier`: `0.2532139820254523`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3750101496011784`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0016036303475117071`
- `max_f1`: `0.9710982658959537`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6995440643781717`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/head_pca_mvtec_tile_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
