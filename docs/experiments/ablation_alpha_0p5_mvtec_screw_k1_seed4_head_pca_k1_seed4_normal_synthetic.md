# Run ablation_alpha_0p5_mvtec_screw_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_screw_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.764479208652535`
- `auroc`: `0.569583931133429`
- `brier`: `0.21040111075289775`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1422977235168219`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0028106701443903147`
- `max_f1`: `0.8530465949820788`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6129498822883631`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_screw_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
