# Run ablation_alpha_0p25_mvtec_transistor_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_transistor_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8317218972409576`
- `auroc`: `0.86875`
- `brier`: `0.24847951746285699`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.14421622842550275`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002728221546858549`
- `max_f1`: `0.76`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6899819920592978`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_transistor_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
