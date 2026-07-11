# Run ablation_alpha_1p0_mvtec_screw_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_screw_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.7849281289384799`
- `auroc`: `0.6109858577577373`
- `brier`: `0.1909045543402123`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.019379533082246825`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002729554532561451`
- `max_f1`: `0.8561151079136691`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5699103525878693`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_screw_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
