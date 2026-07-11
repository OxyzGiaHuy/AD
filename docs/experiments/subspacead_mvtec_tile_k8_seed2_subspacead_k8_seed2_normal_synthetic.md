# Run subspacead_mvtec_tile_k8_seed2_subspacead_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/subspacead_mvtec_tile_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `subspacead`

## Metrics

- `ap`: `0.9889391911580325`
- `auroc`: `0.974025974025974`
- `brier`: `0.1323650282403511`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.23450640608102846`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.001275874833520661`
- `max_f1`: `0.9651162790697675`
- `model_storage_mb`: `0.09521484375`
- `nll`: `0.4280610163231919`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/subspacead_mvtec_tile_k8_seed2_subspacead_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
