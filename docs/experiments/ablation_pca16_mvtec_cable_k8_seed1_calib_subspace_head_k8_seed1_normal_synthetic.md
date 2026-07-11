# Run ablation_pca16_mvtec_cable_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_cable_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9022586141897785`
- `auroc`: `0.8332083958020989`
- `brier`: `0.20247609790900475`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.18620034894517937`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0020388606439034145`
- `max_f1`: `0.8076923076923077`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.8675410778259203`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_cable_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
