# Run ablation_alpha_0p5_mvtec_capsule_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_capsule_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9705037232941633`
- `auroc`: `0.8719585161547666`
- `brier`: `0.17373705214304141`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2301825817787286`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0032428333705121822`
- `max_f1`: `0.9174311926605505`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5365354609391689`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_capsule_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
