# Run head_pca_visa_fryum_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_fryum_k8_seed0.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.9858529400646792`
- `auroc`: `0.9672`
- `brier`: `0.2297943191421886`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.20455519715944925`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002876384370028973`
- `max_f1`: `0.9430051813471503`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6526663099895765`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_visa_fryum_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
