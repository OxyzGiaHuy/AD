# Run ablation_alpha_0p0_mvtec_bottle_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_bottle_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9951440148892859`
- `auroc`: `0.9865079365079366`
- `brier`: `0.24924980128477994`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.4221607759056321`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0032260037779089914`
- `max_f1`: `0.9921259842519685`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6915765800518184`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_bottle_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
