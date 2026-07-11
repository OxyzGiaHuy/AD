# Run ablation_pca32_mvtec_transistor_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_transistor_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7787393189960866`
- `auroc`: `0.8170833333333334`
- `brier`: `0.1979694859128281`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.16800763259758245`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0014107000082731248`
- `max_f1`: `0.7216494845360825`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.6302318669593077`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_transistor_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
