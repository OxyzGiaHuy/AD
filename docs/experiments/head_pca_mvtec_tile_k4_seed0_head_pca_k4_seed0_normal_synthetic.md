# Run head_pca_mvtec_tile_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/head_pca_mvtec_tile_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9930653303096755`
- `auroc`: `0.9841269841269841`
- `brier`: `0.26770451405396845`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.43552476371455395`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0015975416789197514`
- `max_f1`: `0.9824561403508771`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.7283795405348025`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/head_pca_mvtec_tile_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
