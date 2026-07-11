# Run ablation_alpha_0p0_mvtec_zipper_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_zipper_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9837283064968109`
- `auroc`: `0.9432773109243697`
- `brier`: `0.24884627533608933`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3724834540032394`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002580567750315003`
- `max_f1`: `0.9477911646586346`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6908275049657808`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_zipper_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
