# Run ablation_calib_upper_mvtec_wood_k4_seed1_calib_subspace_head_k4_seed1_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_wood_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9813705279363787`
- `auroc`: `0.9532163742690059`
- `brier`: `0.08804355486771218`
- `calibration_anomaly_val_count`: `6`
- `ece`: `0.11979216255553779`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0014506949188366328`
- `max_f1`: `0.954954954954955`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.40043695626775055`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_wood_k4_seed1_calib_subspace_head_k4_seed1_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
