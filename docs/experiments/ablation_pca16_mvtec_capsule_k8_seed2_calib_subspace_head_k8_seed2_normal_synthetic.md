# Run ablation_pca16_mvtec_capsule_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_capsule_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9166948171505207`
- `auroc`: `0.713203031511767`
- `brier`: `0.11307885915464497`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.08190336400134994`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.003139498403690981`
- `max_f1`: `0.9191489361702128`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.3591196513358625`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_capsule_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
