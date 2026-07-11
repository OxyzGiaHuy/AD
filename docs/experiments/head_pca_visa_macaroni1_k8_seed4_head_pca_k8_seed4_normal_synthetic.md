# Run head_pca_visa_macaroni1_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_macaroni1_k8_seed4.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.878965754425351`
- `auroc`: `0.85655`
- `brier`: `0.23560115726507952`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2346054074168205`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.00830492059700191`
- `max_f1`: `0.7679324894514767`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6642480575210626`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_visa_macaroni1_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
