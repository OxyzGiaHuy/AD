# Run anomalydino_mvtec_bottle_k2_seed1_anomalydino_k2_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_bottle_k2_seed1.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9840192946626533`
- `auroc`: `0.9611111111111111`
- `brier`: `0.24096385542168675`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.24096385542168675`
- `k_shot`: `2`
- `latency_sec_per_image`: `0.008555555805922991`
- `max_f1`: `0.9692307692307692`
- `model_storage_mb`: `4.0107421875`
- `nll`: `4.438718257934363`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `2738`

## Notes

- Predictions written to outputs/anomalydino_mvtec_bottle_k2_seed1_anomalydino_k2_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
