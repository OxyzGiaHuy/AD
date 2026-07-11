# Run anomalydino_mvtec_metal_nut_k8_seed4_anomalydino_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_metal_nut_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9701405021000186`
- `auroc`: `0.9081133919843597`
- `brier`: `0.7956397124539094`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7985191899493499`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012283711718476337`
- `max_f1`: `0.9489795918367347`
- `model_storage_mb`: `6.0`
- `nll`: `3.935163796457465`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_mvtec_metal_nut_k8_seed4_anomalydino_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
