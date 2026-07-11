# Run patchcore_mvtec_screw_k8_seed2_patchcore_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_screw_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.8886325597368245`
- `auroc`: `0.7843820455011273`
- `brier`: `0.7116256770161634`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.719504244014388`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012187320820521564`
- `max_f1`: `0.8905660377358491`
- `model_storage_mb`: `6.0`
- `nll`: `2.8738563978025278`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/patchcore_mvtec_screw_k8_seed2_patchcore_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
