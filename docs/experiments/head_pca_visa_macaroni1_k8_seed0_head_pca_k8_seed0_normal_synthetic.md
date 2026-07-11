# Run head_pca_visa_macaroni1_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_macaroni1_k8_seed0.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.8805632365789429`
- `auroc`: `0.8604`
- `brier`: `0.2354884763843556`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.16322596967220304`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.005932820485904813`
- `max_f1`: `0.7965367965367965`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6640692688852051`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_visa_macaroni1_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
