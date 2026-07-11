# Run anomalydino_mvtec_carpet_k8_seed4_anomalydino_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_carpet_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9987564275672564`
- `auroc`: `0.9959871589085072`
- `brier`: `0.7569178913641061`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7550080948589871`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012621420555007763`
- `max_f1`: `0.9887640449438202`
- `model_storage_mb`: `6.0`
- `nll`: `4.686610051860776`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_mvtec_carpet_k8_seed4_anomalydino_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
