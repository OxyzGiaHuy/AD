# Run ablation_alpha_0p5_mvtec_capsule_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_capsule_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9430752854113111`
- `auroc`: `0.7933785400877543`
- `brier`: `0.18273889261274806`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.21268591239596862`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0019045994250160275`
- `max_f1`: `0.9137931034482759`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5559293862099793`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_capsule_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
