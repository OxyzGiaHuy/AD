# Run ablation_pca128_mvtec_screw_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_screw_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9130705084820965`
- `auroc`: `0.7929903668784587`
- `brier`: `0.21902887076995414`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2217402655631304`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0020368607249110935`
- `max_f1`: `0.8793774319066148`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.2280923004127446`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_screw_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
