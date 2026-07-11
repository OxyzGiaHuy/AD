# Run subspacead_mvtec_carpet_k8_seed1_subspacead_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/subspacead_mvtec_carpet_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `subspacead`

## Metrics

- `ap`: `0.9974594188000838`
- `auroc`: `0.9919743178170144`
- `brier`: `0.10704524273963549`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.16809416122925586`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0012816619287189255`
- `max_f1`: `0.9834254143646409`
- `model_storage_mb`: `0.09521484375`
- `nll`: `0.3075048225205406`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/subspacead_mvtec_carpet_k8_seed1_subspacead_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
