# Run head_pca_visa_pipe_fryum_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pipe_fryum_k8_seed4.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.9794578408688853`
- `auroc`: `0.9584`
- `brier`: `0.2321459286846472`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.21815875689188632`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.008381675779819488`
- `max_f1`: `0.9313725490196079`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6573872894964992`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_visa_pipe_fryum_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
