# Run ablation_pca16_mvtec_capsule_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_capsule_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9141178382252146`
- `auroc`: `0.7108097327483047`
- `brier`: `0.1269993365627543`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1411515898565113`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0020470946998984523`
- `max_f1`: `0.9191489361702128`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.4615487331494591`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_capsule_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
