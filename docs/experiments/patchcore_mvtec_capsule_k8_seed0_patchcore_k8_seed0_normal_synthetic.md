# Run patchcore_mvtec_capsule_k8_seed0_patchcore_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_capsule_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.9740481824350828`
- `auroc`: `0.8903071400079776`
- `brier`: `0.7050012678440254`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7459211492572317`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012309716562881615`
- `max_f1`: `0.9411764705882353`
- `model_storage_mb`: `6.0`
- `nll`: `2.1390773132549055`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/patchcore_mvtec_capsule_k8_seed0_patchcore_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
