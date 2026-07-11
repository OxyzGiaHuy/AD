# Run head_pca_visa_pcb4_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb4_k1_seed0.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.6263904136244363`
- `auroc`: `0.6697029702970297`
- `brier`: `0.2479287688681221`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.003842084858547923`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.00576579501268579`
- `max_f1`: `0.704`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.689004146523332`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/head_pca_visa_pcb4_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
