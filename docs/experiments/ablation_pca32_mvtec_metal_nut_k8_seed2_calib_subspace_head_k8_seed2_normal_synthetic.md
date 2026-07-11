# Run ablation_pca32_mvtec_metal_nut_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_metal_nut_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9822277316556652`
- `auroc`: `0.9310850439882697`
- `brier`: `0.10182150688087374`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.11820448350323279`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0029896889205860053`
- `max_f1`: `0.9489795918367347`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.39853936828083797`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_metal_nut_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
