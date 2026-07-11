# Run head_pca_visa_pcb1_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb1_k4_seed0.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.877239340103737`
- `auroc`: `0.8857`
- `brier`: `0.24500225303072107`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.07507947191596029`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.006660112263634801`
- `max_f1`: `0.8387096774193549`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6831339940380502`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/head_pca_visa_pcb1_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
