# Run patchcore_mvtec_tile_k1_seed4_patchcore_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_tile_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.9994296097320307`
- `auroc`: `0.9985569985569985`
- `brier`: `0.28205128205128205`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.28205128205128205`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.005036288776840919`
- `max_f1`: `0.9940828402366864`
- `model_storage_mb`: `2.00537109375`
- `nll`: `5.195576625851375`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/patchcore_mvtec_tile_k1_seed4_patchcore_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
