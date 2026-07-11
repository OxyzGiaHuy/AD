# Run ablation_pca128_mvtec_tile_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_tile_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9958072388377271`
- `auroc`: `0.9906204906204906`
- `brier`: `0.03715842914224567`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.057195152311275414`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0024698742657390414`
- `max_f1`: `0.9880952380952381`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.1794146700720217`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_tile_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
