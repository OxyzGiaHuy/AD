# Run ablation_pca16_mvtec_grid_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_grid_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9959050108874103`
- `auroc`: `0.9883040935672515`
- `brier`: `0.17883870287139592`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2319764907543476`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.003482049641509851`
- `max_f1`: `0.9649122807017544`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.5137449443505868`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_grid_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
