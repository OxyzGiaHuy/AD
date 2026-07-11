# Run ablation_pca32_mvtec_capsule_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_capsule_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.947528352569364`
- `auroc`: `0.7997606701236538`
- `brier`: `0.136102732351928`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.14889812286723603`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001548676977329182`
- `max_f1`: `0.9170305676855895`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.6374581487675708`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_capsule_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
