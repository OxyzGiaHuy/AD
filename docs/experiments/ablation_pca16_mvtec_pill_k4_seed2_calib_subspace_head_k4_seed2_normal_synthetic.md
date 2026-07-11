# Run ablation_pca16_mvtec_pill_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_pill_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9715777720652438`
- `auroc`: `0.8611565739225314`
- `brier`: `0.08103309821503238`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.0698210473735622`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002654736080837107`
- `max_f1`: `0.9423728813559322`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.2659752236883472`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_pill_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
