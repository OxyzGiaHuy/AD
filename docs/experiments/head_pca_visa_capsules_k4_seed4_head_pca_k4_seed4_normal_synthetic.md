# Run head_pca_visa_capsules_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_capsules_k4_seed4.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.9725754120194864`
- `auroc`: `0.9518333333333333`
- `brier`: `0.22530155851176142`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.23802734278142457`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0033173091942444444`
- `max_f1`: `0.9253731343283582`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6436262254352789`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/head_pca_visa_capsules_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
