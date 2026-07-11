# Run ablation_alpha_1p0_mvtec_capsule_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_capsule_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9779795684146992`
- `auroc`: `0.8994814519345832`
- `brier`: `0.14375888810674123`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.15994672703020502`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002444306840047692`
- `max_f1`: `0.9344978165938864`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.4648944264816849`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_capsule_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
