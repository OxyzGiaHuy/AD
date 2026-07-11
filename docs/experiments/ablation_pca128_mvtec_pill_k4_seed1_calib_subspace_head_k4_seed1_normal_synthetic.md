# Run ablation_pca128_mvtec_pill_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_pill_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9835700290214754`
- `auroc`: `0.9208947081287506`
- `brier`: `0.12031289751587745`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12769692509384928`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.001633942707213099`
- `max_f1`: `0.9452054794520548`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.65075037470454`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_pill_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
