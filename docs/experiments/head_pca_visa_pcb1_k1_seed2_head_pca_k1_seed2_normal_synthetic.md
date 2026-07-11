# Run head_pca_visa_pcb1_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb1_k1_seed2.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.8660788025361641`
- `auroc`: `0.8662`
- `brier`: `0.24541265968881765`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.006922379732131945`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.005491221696138382`
- `max_f1`: `0.8058252427184466`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6839691386700355`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/head_pca_visa_pcb1_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
