# Run ablation_pca32_mvtec_transistor_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_transistor_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8575119111816631`
- `auroc`: `0.8779166666666667`
- `brier`: `0.1650606239674582`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.17710265149740737`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0018111160025000572`
- `max_f1`: `0.7560975609756098`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.5478181347139307`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_transistor_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
