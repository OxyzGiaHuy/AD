# Run head_pca_visa_capsules_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_capsules_k8_seed0.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.9731300808649084`
- `auroc`: `0.9498333333333333`
- `brier`: `0.22399226252391383`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.20506921429187058`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.005249450076371431`
- `max_f1`: `0.9253731343283582`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6409738611934106`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_visa_capsules_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
