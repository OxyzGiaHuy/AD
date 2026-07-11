# Run head_pca_visa_capsules_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_capsules_k1_seed0.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.9628313485407953`
- `auroc`: `0.9296666666666666`
- `brier`: `0.2316984629331061`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.25346290823072193`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0031376540544442834`
- `max_f1`: `0.900990099009901`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6564451556086692`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/head_pca_visa_capsules_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
