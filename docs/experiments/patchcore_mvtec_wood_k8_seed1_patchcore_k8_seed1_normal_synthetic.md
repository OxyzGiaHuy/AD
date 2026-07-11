# Run patchcore_mvtec_wood_k8_seed1_patchcore_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_wood_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.9862861229216617`
- `auroc`: `0.962280701754386`
- `brier`: `0.7447161555394494`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7457872171108199`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012211450151627577`
- `max_f1`: `0.9752066115702479`
- `model_storage_mb`: `6.0`
- `nll`: `3.5513775476554175`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/patchcore_mvtec_wood_k8_seed1_patchcore_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
