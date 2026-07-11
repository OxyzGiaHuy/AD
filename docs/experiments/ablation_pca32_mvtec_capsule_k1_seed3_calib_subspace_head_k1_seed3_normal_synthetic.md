# Run ablation_pca32_mvtec_capsule_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_capsule_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9245341420783617`
- `auroc`: `0.7518946948544076`
- `brier`: `0.16600638137081491`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1722546028481289`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0018116562260371265`
- `max_f1`: `0.9251101321585903`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `1.9320686827076088`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_capsule_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
