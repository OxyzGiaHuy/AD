# Run head_pca_visa_macaroni2_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_macaroni2_k8_seed0.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.8169420511895231`
- `auroc`: `0.7865`
- `brier`: `0.24150856758490646`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.0935438276827335`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.004260101672261953`
- `max_f1`: `0.7251908396946565`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6761387630137705`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_visa_macaroni2_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
