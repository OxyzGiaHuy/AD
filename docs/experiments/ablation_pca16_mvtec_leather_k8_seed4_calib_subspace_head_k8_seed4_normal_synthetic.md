# Run ablation_pca16_mvtec_leather_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_leather_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `1.0`
- `auroc`: `1.0`
- `brier`: `0.08411541785353371`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12336316287908106`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0028120737162328534`
- `max_f1`: `1.0`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.23838384338079827`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_leather_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
