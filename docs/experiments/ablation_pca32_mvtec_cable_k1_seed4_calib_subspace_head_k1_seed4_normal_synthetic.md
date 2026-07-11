# Run ablation_pca32_mvtec_cable_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_cable_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9209968998382528`
- `auroc`: `0.8562593703148426`
- `brier`: `0.32176009575099657`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.33251936256885517`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0019541849692662557`
- `max_f1`: `0.8415300546448088`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `1.594966656228029`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_cable_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
