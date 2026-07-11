# Run ablation_alpha_1p0_mvtec_carpet_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_carpet_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9804579506998917`
- `auroc`: `0.9281701444622793`
- `brier`: `0.15731323041911532`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2371865095745804`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0018554174492501805`
- `max_f1`: `0.9257142857142857`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.4951038431786719`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_carpet_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
