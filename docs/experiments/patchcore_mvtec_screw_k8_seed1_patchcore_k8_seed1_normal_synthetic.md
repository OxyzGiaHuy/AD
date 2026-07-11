# Run patchcore_mvtec_screw_k8_seed1_patchcore_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_screw_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.8698192986439338`
- `auroc`: `0.7911457265833163`
- `brier`: `0.7437479801592812`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7437479109886495`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012264604726806284`
- `max_f1`: `0.8835341365461847`
- `model_storage_mb`: `6.0`
- `nll`: `10.576331011077468`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/patchcore_mvtec_screw_k8_seed1_patchcore_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
