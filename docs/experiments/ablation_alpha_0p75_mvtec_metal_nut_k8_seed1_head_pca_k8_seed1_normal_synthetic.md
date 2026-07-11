# Run ablation_alpha_0p75_mvtec_metal_nut_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_metal_nut_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9925867844686552`
- `auroc`: `0.9711632453567938`
- `brier`: `0.16840957298294562`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.20365392125171167`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002638285979628563`
- `max_f1`: `0.9732620320855615`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5241456826503587`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_metal_nut_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
