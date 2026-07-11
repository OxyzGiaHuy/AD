# Run head_pca_visa_pcb1_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb1_k1_seed0.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.8323033651155015`
- `auroc`: `0.8529`
- `brier`: `0.24577086935762713`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.010526366382837271`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.004664607215672732`
- `max_f1`: `0.8195121951219512`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6846835166565381`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/head_pca_visa_pcb1_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
