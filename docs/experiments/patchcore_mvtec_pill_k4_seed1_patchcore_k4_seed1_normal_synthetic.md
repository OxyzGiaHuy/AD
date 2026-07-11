# Run patchcore_mvtec_pill_k4_seed1_patchcore_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_pill_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.9783491120902461`
- `auroc`: `0.8968903436988543`
- `brier`: `0.8167771844598503`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.8265306368459038`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.01290225693788714`
- `max_f1`: `0.9370629370629371`
- `model_storage_mb`: `6.0`
- `nll`: `3.4920673646813993`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/patchcore_mvtec_pill_k4_seed1_patchcore_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
