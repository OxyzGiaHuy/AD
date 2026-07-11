# Run ablation_pca32_mvtec_bottle_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_bottle_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.978938404851157`
- `auroc`: `0.9555555555555556`
- `brier`: `0.081917258555164`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.10873505082935184`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002512555995798973`
- `max_f1`: `0.9618320610687023`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.4907712963443071`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_bottle_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
