# Run ablation_pca64_mvtec_zipper_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_zipper_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9850160775000917`
- `auroc`: `0.9459033613445378`
- `brier`: `0.10748547433034697`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12422533129940938`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0030220790414620708`
- `max_f1`: `0.9465020576131687`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.6272902714974972`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_zipper_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
