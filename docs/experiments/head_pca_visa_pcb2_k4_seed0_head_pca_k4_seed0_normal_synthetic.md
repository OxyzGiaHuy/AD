# Run head_pca_visa_pcb2_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb2_k4_seed0.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.7739135229424048`
- `auroc`: `0.7564`
- `brier`: `0.2435537588399505`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.04614864870905877`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0025616525020450355`
- `max_f1`: `0.7205882352941176`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6802406879999083`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/head_pca_visa_pcb2_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
