# Run subspacead_mvtec_tile_k4_seed4_subspacead_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/subspacead_mvtec_tile_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `subspacead`

## Metrics

- `ap`: `0.9931776691519542`
- `auroc`: `0.9841269841269841`
- `brier`: `0.2405923070454881`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.25861272241315264`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0013132069546442765`
- `max_f1`: `0.9824561403508771`
- `model_storage_mb`: `0.09521484375`
- `nll`: `0.8027436226948478`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/subspacead_mvtec_tile_k4_seed4_subspacead_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
