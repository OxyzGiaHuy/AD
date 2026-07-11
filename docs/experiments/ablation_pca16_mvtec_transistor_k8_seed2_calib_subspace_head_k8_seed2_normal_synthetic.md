# Run ablation_pca16_mvtec_transistor_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_transistor_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7239409679543967`
- `auroc`: `0.7866666666666666`
- `brier`: `0.20200104086105294`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.17640609848840544`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.001744214054197073`
- `max_f1`: `0.6732673267326733`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.794615067782127`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_transistor_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
