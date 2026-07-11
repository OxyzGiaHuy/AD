# Run ablation_pca32_mvtec_capsule_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_capsule_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8900741201165852`
- `auroc`: `0.6824890307140008`
- `brier`: `0.13204184945240866`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.136185368156117`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002582910414220709`
- `max_f1`: `0.9251101321585903`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.49385164091352046`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_capsule_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
