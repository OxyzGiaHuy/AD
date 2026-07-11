# Run ablation_alpha_1p0_mvtec_grid_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_grid_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8328066666329219`
- `auroc`: `0.6211361737677528`
- `brier`: `0.1966135642529966`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.006599811407235867`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.005106669444686327`
- `max_f1`: `0.8682170542635659`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5821645092481362`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_grid_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
