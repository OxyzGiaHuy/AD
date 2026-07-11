# Run head_pca_visa_pcb4_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb4_k4_seed4.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.887982867006567`
- `auroc`: `0.916930693069307`
- `brier`: `0.2397085225572669`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.06529685573198316`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0026243584258342856`
- `max_f1`: `0.8796296296296297`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6725468006957345`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/head_pca_visa_pcb4_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
