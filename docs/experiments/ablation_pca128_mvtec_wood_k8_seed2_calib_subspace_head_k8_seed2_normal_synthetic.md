# Run ablation_pca128_mvtec_wood_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_wood_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9862700556737016`
- `auroc`: `0.9570175438596491`
- `brier`: `0.1467159074671857`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.17354497690744042`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0030553573624619956`
- `max_f1`: `0.9448818897637795`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.0256415280057811`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_wood_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
