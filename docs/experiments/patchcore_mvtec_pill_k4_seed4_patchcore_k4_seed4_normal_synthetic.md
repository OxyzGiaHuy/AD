# Run patchcore_mvtec_pill_k4_seed4_patchcore_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_pill_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.9870692315405909`
- `auroc`: `0.9432624113475178`
- `brier`: `0.8345737228438916`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.8371767823376642`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.012004654475314888`
- `max_f1`: `0.9574468085106383`
- `model_storage_mb`: `6.0`
- `nll`: `4.446514733837977`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/patchcore_mvtec_pill_k4_seed4_patchcore_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
