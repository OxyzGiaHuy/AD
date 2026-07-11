# Run head_pca_visa_macaroni2_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_macaroni2_k8_seed1.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.8285544454051174`
- `auroc`: `0.7894`
- `brier`: `0.24136779505684391`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.056556482464075054`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.005193740762770176`
- `max_f1`: `0.7258064516129032`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6758637147418434`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_visa_macaroni2_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
