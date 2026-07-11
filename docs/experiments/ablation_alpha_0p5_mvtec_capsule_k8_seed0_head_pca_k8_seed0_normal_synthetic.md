# Run ablation_alpha_0p5_mvtec_capsule_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_capsule_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9514496971249683`
- `auroc`: `0.7981651376146789`
- `brier`: `0.17638829259604766`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2032123670885057`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0032775175447265306`
- `max_f1`: `0.9098712446351931`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.542310363273527`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_capsule_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
