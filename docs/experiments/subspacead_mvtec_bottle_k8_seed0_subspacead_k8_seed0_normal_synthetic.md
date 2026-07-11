# Run subspacead_mvtec_bottle_k8_seed0_subspacead_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/subspacead_mvtec_bottle_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `subspacead`

## Metrics

- `ap`: `0.9953837495276107`
- `auroc`: `0.9865079365079366`
- `brier`: `0.23154305895403776`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.23568736645112554`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0013185046747865446`
- `max_f1`: `0.984375`
- `model_storage_mb`: `0.09521484375`
- `nll`: `1.0188831204114828`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/subspacead_mvtec_bottle_k8_seed0_subspacead_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
