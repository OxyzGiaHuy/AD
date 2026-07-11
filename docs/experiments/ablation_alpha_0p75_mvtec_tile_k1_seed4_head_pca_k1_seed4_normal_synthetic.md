# Run ablation_alpha_0p75_mvtec_tile_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_tile_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9739782556614441`
- `auroc`: `0.9224386724386724`
- `brier`: `0.19875188141943095`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3113570860308459`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0018513249312965279`
- `max_f1`: `0.9156626506024096`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5867930490156177`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_tile_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
