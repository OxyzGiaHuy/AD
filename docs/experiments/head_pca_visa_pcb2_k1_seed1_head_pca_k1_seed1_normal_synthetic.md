# Run head_pca_visa_pcb2_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb2_k1_seed1.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.5998179724758816`
- `auroc`: `0.5682`
- `brier`: `0.24921863624469842`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.00608219817280764`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0037974879145622254`
- `max_f1`: `0.6666666666666666`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6915834376125826`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/head_pca_visa_pcb2_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
