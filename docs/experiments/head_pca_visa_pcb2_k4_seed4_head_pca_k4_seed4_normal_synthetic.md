# Run head_pca_visa_pcb2_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb2_k4_seed4.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.7140245910894876`
- `auroc`: `0.7336`
- `brier`: `0.24534151402667492`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.0022655373811721526`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.004674821998924017`
- `max_f1`: `0.7137254901960784`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6838262033005935`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/head_pca_visa_pcb2_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
