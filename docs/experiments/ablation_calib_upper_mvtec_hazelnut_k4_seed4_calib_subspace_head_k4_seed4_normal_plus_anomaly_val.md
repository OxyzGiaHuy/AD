# Run ablation_calib_upper_mvtec_hazelnut_k4_seed4_calib_subspace_head_k4_seed4_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_hazelnut_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9933258054105298`
- `auroc`: `0.9900793650793651`
- `brier`: `0.16357113792808062`
- `calibration_anomaly_val_count`: `7`
- `ece`: `0.2300678614563155`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0017311556933863649`
- `max_f1`: `0.9767441860465116`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.4722419812595562`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_hazelnut_k4_seed4_calib_subspace_head_k4_seed4_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
