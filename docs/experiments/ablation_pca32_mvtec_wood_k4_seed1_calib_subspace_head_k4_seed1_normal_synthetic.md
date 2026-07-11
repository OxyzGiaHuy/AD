# Run ablation_pca32_mvtec_wood_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_wood_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.985900357085687`
- `auroc`: `0.9596491228070175`
- `brier`: `0.13235332740720043`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.14413790338778795`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.001520213635661934`
- `max_f1`: `0.9586776859504132`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `1.3488106053484554`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_wood_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
