# Run ablation_pca64_mvtec_zipper_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_zipper_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.986443079455903`
- `auroc`: `0.9516806722689075`
- `brier`: `0.1063189929010391`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12203654968518982`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.00257369905512854`
- `max_f1`: `0.9512195121951219`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.47694671752728`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_zipper_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
