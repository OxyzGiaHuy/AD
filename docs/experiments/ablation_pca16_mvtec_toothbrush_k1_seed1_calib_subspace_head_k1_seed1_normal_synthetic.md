# Run ablation_pca16_mvtec_toothbrush_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_toothbrush_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9768025465266845`
- `auroc`: `0.9388888888888889`
- `brier`: `0.21206012671676425`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.23208433389663694`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.003623654356315022`
- `max_f1`: `0.9206349206349206`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `1.1000248296759139`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_toothbrush_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
