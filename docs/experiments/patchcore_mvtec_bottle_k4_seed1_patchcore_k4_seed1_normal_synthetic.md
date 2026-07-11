# Run patchcore_mvtec_bottle_k4_seed1_patchcore_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_bottle_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.9977665294965602`
- `auroc`: `0.9928571428571429`
- `brier`: `0.7347295551070627`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7380179517161864`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.012693627367177641`
- `max_f1`: `0.9767441860465116`
- `model_storage_mb`: `6.0`
- `nll`: `3.1652821984340664`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/patchcore_mvtec_bottle_k4_seed1_patchcore_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
