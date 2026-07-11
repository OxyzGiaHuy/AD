# Run ablation_pca16_mvtec_capsule_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_capsule_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9219922174526375`
- `auroc`: `0.7267650578380535`
- `brier`: `0.1259495025086963`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.09604775634678928`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0019120741212232547`
- `max_f1`: `0.9152542372881356`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.40677005494630003`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_capsule_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
