# Run anomalydino_mvtec_bottle_k1_seed0_anomalydino_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_bottle_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9878708593583001`
- `auroc`: `0.9674603174603175`
- `brier`: `0.24096385542168675`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.24096385542168675`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.004725869543042527`
- `max_f1`: `0.9692307692307692`
- `model_storage_mb`: `2.00537109375`
- `nll`: `4.438718257934363`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/anomalydino_mvtec_bottle_k1_seed0_anomalydino_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
