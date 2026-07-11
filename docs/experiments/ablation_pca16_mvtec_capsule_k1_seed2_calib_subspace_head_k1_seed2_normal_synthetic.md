# Run ablation_pca16_mvtec_capsule_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_capsule_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9233528931170502`
- `auroc`: `0.72317510969286`
- `brier`: `0.3959334370567812`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.4182559406791839`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0014519428015884125`
- `max_f1`: `0.9177489177489178`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `1.3963210886355062`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_capsule_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
