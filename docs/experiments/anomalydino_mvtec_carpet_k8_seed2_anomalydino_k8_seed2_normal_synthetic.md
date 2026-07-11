# Run anomalydino_mvtec_carpet_k8_seed2_anomalydino_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_carpet_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9987588361587736`
- `auroc`: `0.9959871589085072`
- `brier`: `0.7606788057628615`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7606416259633234`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012557195181138495`
- `max_f1`: `0.9830508474576272`
- `model_storage_mb`: `6.0`
- `nll`: `10.056757116207587`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_mvtec_carpet_k8_seed2_anomalydino_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
