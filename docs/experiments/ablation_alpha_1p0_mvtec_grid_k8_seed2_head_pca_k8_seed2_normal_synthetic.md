# Run ablation_alpha_1p0_mvtec_grid_k8_seed2_head_pca_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_grid_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9969202332441824`
- `auroc`: `0.9916457811194653`
- `brier`: `0.191281493001258`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.05271935845032717`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.003148645950624576`
- `max_f1`: `0.9827586206896551`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5678188848760114`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_grid_k8_seed2_head_pca_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
