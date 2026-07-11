# Run ablation_pca64_mvtec_bottle_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_bottle_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9951440148892859`
- `auroc`: `0.9865079365079366`
- `brier`: `0.07591641393336755`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1013795698274779`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.00331265728426985`
- `max_f1`: `0.9921259842519685`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.4343362185543566`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_bottle_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
