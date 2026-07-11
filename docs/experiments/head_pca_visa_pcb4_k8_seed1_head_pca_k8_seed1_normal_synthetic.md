# Run head_pca_visa_pcb4_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb4_k8_seed1.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.8063149119242989`
- `auroc`: `0.8035643564356436`
- `brier`: `0.24434360138869698`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.006240134363743786`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0035902623050100176`
- `max_f1`: `0.7654320987654321`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6818294110064033`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_visa_pcb4_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
