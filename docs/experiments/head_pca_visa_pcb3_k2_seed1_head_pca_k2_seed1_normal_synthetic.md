# Run head_pca_visa_pcb3_k2_seed1_head_pca_k2_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb3_k2_seed1.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.7525487464795614`
- `auroc`: `0.7324752475247525`
- `brier`: `0.24642337963748387`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.009526299303443897`
- `k_shot`: `2`
- `latency_sec_per_image`: `0.004221647004805394`
- `max_f1`: `0.7074235807860262`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6859899651649015`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `2738`

## Notes

- Predictions written to outputs/head_pca_visa_pcb3_k2_seed1_head_pca_k2_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
