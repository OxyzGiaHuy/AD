# Run ablation_alpha_1p0_mvtec_zipper_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_zipper_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9905544185137556`
- `auroc`: `0.9661239495798319`
- `brier`: `0.15460037333373203`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2859541189591617`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002839288840822826`
- `max_f1`: `0.957983193277311`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.48858232462469087`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_zipper_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
