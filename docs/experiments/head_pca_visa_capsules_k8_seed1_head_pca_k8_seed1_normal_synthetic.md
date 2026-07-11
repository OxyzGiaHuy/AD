# Run head_pca_visa_capsules_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_capsules_k8_seed1.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.9756667968398731`
- `auroc`: `0.956`
- `brier`: `0.22884560181180463`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.21114266216754915`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0045458241133019325`
- `max_f1`: `0.9186602870813397`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6507622247704241`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_visa_capsules_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
