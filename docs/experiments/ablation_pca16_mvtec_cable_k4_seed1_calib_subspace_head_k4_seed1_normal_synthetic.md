# Run ablation_pca16_mvtec_cable_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_cable_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9024633720874774`
- `auroc`: `0.8324587706146926`
- `brier`: `0.2785083014491685`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.289453114370505`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0020130287483334543`
- `max_f1`: `0.8148148148148148`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `1.9067368626379289`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_cable_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
