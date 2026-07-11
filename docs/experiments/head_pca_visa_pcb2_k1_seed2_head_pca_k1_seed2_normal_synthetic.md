# Run head_pca_visa_pcb2_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb2_k1_seed2.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.64054729281161`
- `auroc`: `0.6397`
- `brier`: `0.24758486090686638`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.0016945958137511985`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.003780035302042961`
- `max_f1`: `0.6884057971014492`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6883147115400295`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/head_pca_visa_pcb2_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
