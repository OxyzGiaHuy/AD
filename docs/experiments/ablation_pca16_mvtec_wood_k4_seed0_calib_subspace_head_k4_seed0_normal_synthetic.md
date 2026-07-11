# Run ablation_pca16_mvtec_wood_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_wood_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.985091691338088`
- `auroc`: `0.9578947368421052`
- `brier`: `0.1384334997127043`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.15687879549834552`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.00357362679854224`
- `max_f1`: `0.9586776859504132`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.8909014952935853`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_wood_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
