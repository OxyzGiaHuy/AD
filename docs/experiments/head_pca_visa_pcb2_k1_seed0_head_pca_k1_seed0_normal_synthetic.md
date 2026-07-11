# Run head_pca_visa_pcb2_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb2_k1_seed0.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.6625069665299113`
- `auroc`: `0.6465`
- `brier`: `0.2470306763331434`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.008916675895452501`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0029683391842991115`
- `max_f1`: `0.696969696969697`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6872051253764957`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/head_pca_visa_pcb2_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
