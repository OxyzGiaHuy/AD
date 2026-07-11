# Run ablation_alpha_0p75_mvtec_capsule_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_capsule_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.982360328899899`
- `auroc`: `0.9158356601515756`
- `brier`: `0.14662630553861064`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1812943296902107`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0025939010224784865`
- `max_f1`: `0.9356223175965666`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.47446237781689277`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_capsule_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
