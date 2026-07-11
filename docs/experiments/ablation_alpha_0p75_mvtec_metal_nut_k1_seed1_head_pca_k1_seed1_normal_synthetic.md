# Run ablation_alpha_0p75_mvtec_metal_nut_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_metal_nut_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9788695861910923`
- `auroc`: `0.9071358748778103`
- `brier`: `0.17150757657925775`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2344700569691865`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001823504722636679`
- `max_f1`: `0.9166666666666666`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5304436798208431`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_metal_nut_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
