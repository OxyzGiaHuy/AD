# Run head_pca_mvtec_bottle_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/head_pca_mvtec_bottle_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9990155677655678`
- `auroc`: `0.9968253968253968`
- `brier`: `0.25578779800319057`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.29121483018599365`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0016946445656828135`
- `max_f1`: `0.984375`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.704657987345109`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/head_pca_mvtec_bottle_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
