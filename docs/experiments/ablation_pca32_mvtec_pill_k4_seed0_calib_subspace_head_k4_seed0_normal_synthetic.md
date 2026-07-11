# Run ablation_pca32_mvtec_pill_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_pill_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9826121656799169`
- `auroc`: `0.9132569558101473`
- `brier`: `0.08670612569864226`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.09867154923049826`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0013341570529573693`
- `max_f1`: `0.9480968858131488`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.36844122803628576`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_pill_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
