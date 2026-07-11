# Run subspacead_mvtec_tile_k1_seed3_subspacead_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/subspacead_mvtec_tile_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `subspacead`

## Metrics

- `ap`: `0.9964121218496904`
- `auroc`: `0.9913419913419913`
- `brier`: `0.204596576057201`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3937910138032375`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0012985004796686335`
- `max_f1`: `0.9822485207100592`
- `model_storage_mb`: `0.09521484375`
- `nll`: `0.6012597416667389`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/subspacead_mvtec_tile_k1_seed3_subspacead_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
