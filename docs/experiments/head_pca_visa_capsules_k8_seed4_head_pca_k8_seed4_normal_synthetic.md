# Run head_pca_visa_capsules_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_capsules_k8_seed4.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.9770433151127078`
- `auroc`: `0.9595`
- `brier`: `0.22148818632752204`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.18949102889746425`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.00508904445450753`
- `max_f1`: `0.9261083743842364`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6359310815082615`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_visa_capsules_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
