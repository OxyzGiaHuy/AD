# Run patchcore_mvtec_screw_k8_seed0_patchcore_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_screw_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.8908218361747933`
- `auroc`: `0.8253740520598484`
- `brier`: `0.46523228360247587`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.5347296805121005`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012282044859603047`
- `max_f1`: `0.8949416342412452`
- `model_storage_mb`: `6.0`
- `nll`: `1.1909275730557438`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/patchcore_mvtec_screw_k8_seed0_patchcore_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
