# Run ablation_alpha_1p0_mvtec_hazelnut_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_hazelnut_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8470808914605703`
- `auroc`: `0.74375`
- `brier`: `0.23881750703430743`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.08617810173468154`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001970208774913441`
- `max_f1`: `0.8045977011494253`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6729829540180673`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_hazelnut_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
