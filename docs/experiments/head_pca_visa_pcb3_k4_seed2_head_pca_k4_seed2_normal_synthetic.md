# Run head_pca_visa_pcb3_k4_seed2_head_pca_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb3_k4_seed2.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.6740978044115952`
- `auroc`: `0.6214851485148515`
- `brier`: `0.24787119370179342`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.004437028768643825`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.006830446922512196`
- `max_f1`: `0.6757679180887372`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6888879405192678`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/head_pca_visa_pcb3_k4_seed2_head_pca_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
