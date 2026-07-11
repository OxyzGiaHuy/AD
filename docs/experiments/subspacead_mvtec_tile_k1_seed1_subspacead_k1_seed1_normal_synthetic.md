# Run subspacead_mvtec_tile_k1_seed1_subspacead_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/subspacead_mvtec_tile_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `subspacead`

## Metrics

- `ap`: `0.9946211188685307`
- `auroc`: `0.9862914862914863`
- `brier`: `0.20335835231615357`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3734239890025212`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0012835021266061016`
- `max_f1`: `0.9655172413793104`
- `model_storage_mb`: `0.09521484375`
- `nll`: `0.5986452953901837`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/subspacead_mvtec_tile_k1_seed1_subspacead_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
