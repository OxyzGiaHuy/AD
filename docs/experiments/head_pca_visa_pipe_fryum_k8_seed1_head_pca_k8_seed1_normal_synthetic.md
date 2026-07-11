# Run head_pca_visa_pipe_fryum_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pipe_fryum_k8_seed1.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.9481135681708178`
- `auroc`: `0.906`
- `brier`: `0.23518721898064787`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.26938118795553845`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002995820827782154`
- `max_f1`: `0.8959276018099548`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6634770572973762`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_visa_pipe_fryum_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
