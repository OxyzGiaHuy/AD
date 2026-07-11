# Run head_pca_visa_pcb1_k2_seed1_head_pca_k2_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb1_k2_seed1.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.6778495607709908`
- `auroc`: `0.6823`
- `brier`: `0.24622019818790497`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.020267324298620208`
- `k_shot`: `2`
- `latency_sec_per_image`: `0.0030231237038969992`
- `max_f1`: `0.7045454545454546`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6855813766829345`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `2738`

## Notes

- Predictions written to outputs/head_pca_visa_pcb1_k2_seed1_head_pca_k2_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
