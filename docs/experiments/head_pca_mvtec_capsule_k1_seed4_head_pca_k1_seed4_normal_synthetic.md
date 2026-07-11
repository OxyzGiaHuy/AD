# Run head_pca_mvtec_capsule_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/head_pca_mvtec_capsule_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9606937181678282`
- `auroc`: `0.8496210610291185`
- `brier`: `0.23859019611244792`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3143734789707444`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0016596044103304546`
- `max_f1`: `0.9308755760368663`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6703092435144026`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/head_pca_mvtec_capsule_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
