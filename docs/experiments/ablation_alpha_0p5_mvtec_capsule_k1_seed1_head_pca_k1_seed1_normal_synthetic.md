# Run ablation_alpha_0p5_mvtec_capsule_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_capsule_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8421796774865877`
- `auroc`: `0.6019146390107698`
- `brier`: `0.18381357393701492`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.22797047504872986`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0018548894758251581`
- `max_f1`: `0.9152542372881356`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5582572314121859`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_capsule_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
