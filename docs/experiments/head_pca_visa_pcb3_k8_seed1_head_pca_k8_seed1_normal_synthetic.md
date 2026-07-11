# Run head_pca_visa_pcb3_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb3_k8_seed1.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.7743062191388645`
- `auroc`: `0.7462376237623762`
- `brier`: `0.24562367680396666`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.006868945721963171`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0026659686767046722`
- `max_f1`: `0.7058823529411765`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6843906152967522`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_visa_pcb3_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
