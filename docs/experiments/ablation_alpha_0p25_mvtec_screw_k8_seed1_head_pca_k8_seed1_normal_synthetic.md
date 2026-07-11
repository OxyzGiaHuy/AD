# Run ablation_alpha_0p25_mvtec_screw_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_screw_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8863623911516835`
- `auroc`: `0.7517934002869441`
- `brier`: `0.22011240048745212`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.21692661587148904`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.001720380294136703`
- `max_f1`: `0.8638132295719845`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6329979804907526`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_screw_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
