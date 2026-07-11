# Run ablation_pca128_mvtec_metal_nut_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_metal_nut_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9975540353403017`
- `auroc`: `0.989247311827957`
- `brier`: `0.11883345917411701`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1364281865565673`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0024713388117759126`
- `max_f1`: `0.9787234042553191`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.5112984735104839`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_metal_nut_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
