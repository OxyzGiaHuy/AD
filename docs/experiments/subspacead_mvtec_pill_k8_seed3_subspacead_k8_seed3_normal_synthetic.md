# Run subspacead_mvtec_pill_k8_seed3_subspacead_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/subspacead_mvtec_pill_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `subspacead`

## Metrics

- `ap`: `0.9896800173063391`
- `auroc`: `0.9509001636661211`
- `brier`: `0.1511999976010916`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.15194822214320747`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0013323589980959178`
- `max_f1`: `0.9577464788732394`
- `model_storage_mb`: `0.09521484375`
- `nll`: `0.7045806273006814`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/subspacead_mvtec_pill_k8_seed3_subspacead_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
