# Run head_pca_visa_capsules_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_capsules_k8_seed3.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.9738882673180995`
- `auroc`: `0.952`
- `brier`: `0.225728642588665`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.33801005277782675`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.008968668908346444`
- `max_f1`: `0.9134615384615384`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6444582011261111`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_visa_capsules_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
