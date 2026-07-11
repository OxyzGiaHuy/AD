# Run anomalydino_mvtec_hazelnut_k4_seed1_anomalydino_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_hazelnut_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9903513402590367`
- `auroc`: `0.9821428571428571`
- `brier`: `0.5993403096645014`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.6012591783295979`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.012548449364575472`
- `max_f1`: `0.9645390070921985`
- `model_storage_mb`: `6.0`
- `nll`: `2.252608716850855`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_mvtec_hazelnut_k4_seed1_anomalydino_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
