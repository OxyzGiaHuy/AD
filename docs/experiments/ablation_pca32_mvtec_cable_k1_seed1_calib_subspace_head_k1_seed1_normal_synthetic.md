# Run ablation_pca32_mvtec_cable_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_cable_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8932180525972283`
- `auroc`: `0.8240254872563718`
- `brier`: `0.382913910833421`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.38445143620173133`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0018161963919798533`
- `max_f1`: `0.8082901554404145`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `3.5958913378132222`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_cable_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
