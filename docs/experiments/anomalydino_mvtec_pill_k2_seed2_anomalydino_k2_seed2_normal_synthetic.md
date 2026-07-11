# Run anomalydino_mvtec_pill_k2_seed2_anomalydino_k2_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_pill_k2_seed2.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.971646628178`
- `auroc`: `0.8685215493726132`
- `brier`: `0.15568862275449102`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.15568862275449102`
- `k_shot`: `2`
- `latency_sec_per_image`: `0.008903908716168946`
- `max_f1`: `0.9423728813559322`
- `model_storage_mb`: `4.0107421875`
- `nll`: `2.867890422886933`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `2738`

## Notes

- Predictions written to outputs/anomalydino_mvtec_pill_k2_seed2_anomalydino_k2_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
