# Run ablation_pca32_mvtec_zipper_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_zipper_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9846830286980547`
- `auroc`: `0.9453781512605042`
- `brier`: `0.09861499889642185`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1112445778713025`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002378131195113359`
- `max_f1`: `0.9516129032258065`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.4612879317079232`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_zipper_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
