# Run ablation_alpha_0p0_mvtec_metal_nut_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_metal_nut_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9918051280094828`
- `auroc`: `0.9652981427174976`
- `brier`: `0.2500181260621095`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.333688584877097`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002038183047071747`
- `max_f1`: `0.9528795811518325`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6931773083660488`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_metal_nut_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
