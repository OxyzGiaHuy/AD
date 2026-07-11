# Run head_pca_visa_pcb2_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb2_k8_seed1.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.7457167854302809`
- `auroc`: `0.751`
- `brier`: `0.24365533111294504`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.031027272790670392`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.005703634340316057`
- `max_f1`: `0.752`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6804471290715154`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_visa_pcb2_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
