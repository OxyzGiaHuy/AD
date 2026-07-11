# Run ablation_pca16_mvtec_transistor_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_transistor_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7224817828739507`
- `auroc`: `0.7883333333333333`
- `brier`: `0.5003230661785749`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.5284784631431103`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0023754834197461604`
- `max_f1`: `0.6818181818181818`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `3.4333932400297345`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_transistor_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
