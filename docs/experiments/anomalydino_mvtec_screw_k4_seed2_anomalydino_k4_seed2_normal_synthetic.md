# Run anomalydino_mvtec_screw_k4_seed2_anomalydino_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_screw_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.8796490755056877`
- `auroc`: `0.7323221971715516`
- `brier`: `0.7292416648091413`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7328191361404607`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.012167939369101077`
- `max_f1`: `0.8676470588235294`
- `model_storage_mb`: `6.0`
- `nll`: `3.495805179483611`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_mvtec_screw_k4_seed2_anomalydino_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
