# Run subspacead_mvtec_tile_k2_seed4_subspacead_k2_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/subspacead_mvtec_tile_k2_seed4.yaml`
- Dataset: `mvtec`
- Model: `subspacead`

## Metrics

- `ap`: `0.9941746082680379`
- `auroc`: `0.9862914862914863`
- `brier`: `0.10872021884669551`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2423292818741921`
- `k_shot`: `2`
- `latency_sec_per_image`: `0.0012977915601088451`
- `max_f1`: `0.9710982658959537`
- `model_storage_mb`: `0.09521484375`
- `nll`: `0.3829917363418951`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `2738`

## Notes

- Predictions written to outputs/subspacead_mvtec_tile_k2_seed4_subspacead_k2_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
