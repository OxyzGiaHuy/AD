# Run subspacead_mvtec_hazelnut_k8_seed3_subspacead_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/subspacead_mvtec_hazelnut_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `subspacead`

## Metrics

- `ap`: `0.9917371298914426`
- `auroc`: `0.9875`
- `brier`: `0.36270212102874616`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.36314417557282885`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0012929305095564236`
- `max_f1`: `0.9784172661870504`
- `model_storage_mb`: `0.09521484375`
- `nll`: `2.5360352581395644`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/subspacead_mvtec_hazelnut_k8_seed3_subspacead_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
