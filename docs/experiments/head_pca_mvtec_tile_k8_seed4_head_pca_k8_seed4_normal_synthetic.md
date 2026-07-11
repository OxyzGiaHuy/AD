# Run head_pca_mvtec_tile_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/head_pca_mvtec_tile_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9903259770088614`
- `auroc`: `0.976911976911977`
- `brier`: `0.2607346610755875`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2742870276809758`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0015907113432374776`
- `max_f1`: `0.9704142011834319`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.7144390717375354`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_mvtec_tile_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
