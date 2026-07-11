# Run head_pca_visa_pcb3_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb3_k8_seed4.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.7514186081425717`
- `auroc`: `0.7410891089108911`
- `brier`: `0.24573018740932867`
- `calibration_anomaly_val_count`: `0`
- `ece`: `2.5550376123451013e-05`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0028032091775195517`
- `max_f1`: `0.7174887892376681`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6846043432359084`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_visa_pcb3_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
