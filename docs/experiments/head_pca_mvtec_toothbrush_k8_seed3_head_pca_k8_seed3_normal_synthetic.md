# Run head_pca_mvtec_toothbrush_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/head_pca_mvtec_toothbrush_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9862487192389863`
- `auroc`: `0.9666666666666667`
- `brier`: `0.23826484289709443`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.35144429263614474`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0016202372277066821`
- `max_f1`: `0.967741935483871`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6696434577004601`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_mvtec_toothbrush_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
