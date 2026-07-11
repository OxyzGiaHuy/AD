# Run head_pca_mvtec_toothbrush_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/head_pca_mvtec_toothbrush_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.991118862718325`
- `auroc`: `0.9777777777777777`
- `brier`: `0.23580452292832885`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3709183753955932`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0016214103837098395`
- `max_f1`: `0.967741935483871`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6647205351021767`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_mvtec_toothbrush_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
