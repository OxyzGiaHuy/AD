# Run subspacead_mvtec_grid_k1_seed0_subspacead_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/subspacead_mvtec_grid_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `subspacead`

## Metrics

- `ap`: `0.9846803503966466`
- `auroc`: `0.9598997493734336`
- `brier`: `0.17696939059348288`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.15153843240860185`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0013275146484375`
- `max_f1`: `0.9421487603305785`
- `model_storage_mb`: `0.09521484375`
- `nll`: `0.5358361291826295`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/subspacead_mvtec_grid_k1_seed0_subspacead_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
