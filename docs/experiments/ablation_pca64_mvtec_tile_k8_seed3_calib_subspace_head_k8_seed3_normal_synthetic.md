# Run ablation_pca64_mvtec_tile_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_tile_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9927998982583275`
- `auroc`: `0.9834054834054834`
- `brier`: `0.07832475374530959`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.09329096584990781`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0015162586783751464`
- `max_f1`: `0.9764705882352941`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.3905007249617761`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_tile_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
