# Run patchcore_mvtec_screw_k4_seed1_patchcore_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_screw_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.8986822355725909`
- `auroc`: `0.7946300471408075`
- `brier`: `0.6798816774928239`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.6972046179231256`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.012318702170159668`
- `max_f1`: `0.8659003831417624`
- `model_storage_mb`: `6.0`
- `nll`: `2.3396560627947065`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/patchcore_mvtec_screw_k4_seed1_patchcore_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
