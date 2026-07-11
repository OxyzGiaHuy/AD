# Run ablation_pca128_mvtec_cable_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_cable_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9593383471476943`
- `auroc`: `0.9196026986506747`
- `brier`: `0.19529381037787483`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.21337937039633587`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.001581355556845665`
- `max_f1`: `0.8901734104046243`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.7140124261804385`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_cable_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
