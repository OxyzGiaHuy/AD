# Run head_pca_visa_pipe_fryum_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pipe_fryum_k8_seed3.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.9847852287364839`
- `auroc`: `0.9684`
- `brier`: `0.23605981205226173`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3740183846155802`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0032551340013742447`
- `max_f1`: `0.9365853658536586`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6651846768546694`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_visa_pipe_fryum_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
