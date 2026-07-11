# Run anomalydino_mvtec_hazelnut_k2_seed4_anomalydino_k2_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_hazelnut_k2_seed4.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9809936148051878`
- `auroc`: `0.9682142857142857`
- `brier`: `0.36363636363636365`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.36363636363636365`
- `k_shot`: `2`
- `latency_sec_per_image`: `0.008660829524424943`
- `max_f1`: `0.9436619718309859`
- `model_storage_mb`: `4.0107421875`
- `nll`: `6.698429365973675`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `2738`

## Notes

- Predictions written to outputs/anomalydino_mvtec_hazelnut_k2_seed4_anomalydino_k2_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
