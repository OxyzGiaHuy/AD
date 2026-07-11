# Run ablation_pca128_mvtec_transistor_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_transistor_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7851148247666401`
- `auroc`: `0.81625`
- `brier`: `0.39210199570454124`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.44454134449362753`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002199721001088619`
- `max_f1`: `0.7058823529411765`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.6439528652954187`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_transistor_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
