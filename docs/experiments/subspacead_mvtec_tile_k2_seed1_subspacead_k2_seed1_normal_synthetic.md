# Run subspacead_mvtec_tile_k2_seed1_subspacead_k2_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/subspacead_mvtec_tile_k2_seed1.yaml`
- Dataset: `mvtec`
- Model: `subspacead`

## Metrics

- `ap`: `0.9913061718158387`
- `auroc`: `0.9787157287157288`
- `brier`: `0.2552286995426915`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.26628355796520525`
- `k_shot`: `2`
- `latency_sec_per_image`: `0.001301408084666627`
- `max_f1`: `0.9585798816568047`
- `model_storage_mb`: `0.09521484375`
- `nll`: `0.9262774824516379`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `2738`

## Notes

- Predictions written to outputs/subspacead_mvtec_tile_k2_seed1_subspacead_k2_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
