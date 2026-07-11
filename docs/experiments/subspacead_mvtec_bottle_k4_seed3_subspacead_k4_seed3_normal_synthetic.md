# Run subspacead_mvtec_bottle_k4_seed3_subspacead_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/subspacead_mvtec_bottle_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `subspacead`

## Metrics

- `ap`: `0.9857582192139502`
- `auroc`: `0.9634920634920635`
- `brier`: `0.5799474713490781`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.6250761301223055`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0013352930096976728`
- `max_f1`: `0.9612403100775194`
- `model_storage_mb`: `0.09521484375`
- `nll`: `1.5913606670347102`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/subspacead_mvtec_bottle_k4_seed3_subspacead_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
