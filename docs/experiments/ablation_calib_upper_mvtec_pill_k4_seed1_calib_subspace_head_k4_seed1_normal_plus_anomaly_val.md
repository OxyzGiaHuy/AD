# Run ablation_calib_upper_mvtec_pill_k4_seed1_calib_subspace_head_k4_seed1_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_pill_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9822019181401527`
- `auroc`: `0.9209569957601453`
- `brier`: `0.07875354735766676`
- `calibration_anomaly_val_count`: `14`
- `ece`: `0.07579059404582758`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002370031794009645`
- `max_f1`: `0.9384615384615385`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.2657150074042183`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_pill_k4_seed1_calib_subspace_head_k4_seed1_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
