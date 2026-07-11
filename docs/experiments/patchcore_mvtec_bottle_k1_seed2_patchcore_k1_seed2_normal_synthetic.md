# Run patchcore_mvtec_bottle_k1_seed2_patchcore_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_bottle_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.9826596933159123`
- `auroc`: `0.9563492063492064`
- `brier`: `0.24096385542168675`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.24096385542168675`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002941935379282538`
- `max_f1`: `0.9692307692307692`
- `model_storage_mb`: `2.00537109375`
- `nll`: `4.438718257934363`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/patchcore_mvtec_bottle_k1_seed2_patchcore_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
