# Run anomalydino_mvtec_zipper_k8_seed4_anomalydino_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_zipper_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9980681503536194`
- `auroc`: `0.9926470588235294`
- `brier`: `0.7518817531807211`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.759449760984654`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.01348010529548127`
- `max_f1`: `0.9747899159663865`
- `model_storage_mb`: `6.0`
- `nll`: `3.0034137390984155`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_mvtec_zipper_k8_seed4_anomalydino_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
