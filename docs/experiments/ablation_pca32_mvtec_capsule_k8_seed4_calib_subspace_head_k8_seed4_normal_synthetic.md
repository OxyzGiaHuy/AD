# Run ablation_pca32_mvtec_capsule_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_capsule_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.924899246049953`
- `auroc`: `0.7451136816912645`
- `brier`: `0.1079563041350534`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.08912835168567569`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002110927323387428`
- `max_f1`: `0.9217391304347826`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.36416558951038824`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_capsule_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
