# Run anomalydino_mvtec_toothbrush_k8_seed2_anomalydino_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_toothbrush_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9415191940515726`
- `auroc`: `0.8861111111111111`
- `brier`: `0.7092070035908957`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7085381217905143`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.01247841842649948`
- `max_f1`: `0.9523809523809523`
- `model_storage_mb`: `6.0`
- `nll`: `4.0779569862466865`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_mvtec_toothbrush_k8_seed2_anomalydino_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
