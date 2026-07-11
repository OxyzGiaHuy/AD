# Run head_pca_visa_macaroni1_k1_seed3_head_pca_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_macaroni1_k1_seed3.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.7560233641115316`
- `auroc`: `0.7938`
- `brier`: `0.24502894331198782`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.0066032199561595895`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0052172960713505745`
- `max_f1`: `0.757201646090535`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6832003255234094`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/head_pca_visa_macaroni1_k1_seed3_head_pca_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
