# Run ablation_alpha_1p0_mvtec_toothbrush_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_toothbrush_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9498552360850626`
- `auroc`: `0.8041666666666667`
- `brier`: `0.20336276124775207`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.00664797283354257`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0037436047568917274`
- `max_f1`: `0.8823529411764706`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5965182771065081`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_toothbrush_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
