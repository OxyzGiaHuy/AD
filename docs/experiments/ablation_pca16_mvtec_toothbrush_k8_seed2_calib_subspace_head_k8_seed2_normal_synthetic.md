# Run ablation_pca16_mvtec_toothbrush_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_toothbrush_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9753993935350493`
- `auroc`: `0.9361111111111111`
- `brier`: `0.1576575652855057`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.19560110786516727`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.004029739958544572`
- `max_f1`: `0.9333333333333333`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.6787672656220574`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_toothbrush_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
