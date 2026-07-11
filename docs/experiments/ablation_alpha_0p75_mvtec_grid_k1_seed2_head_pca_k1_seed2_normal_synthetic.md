# Run ablation_alpha_0p75_mvtec_grid_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_grid_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9469292902282576`
- `auroc`: `0.8688387635756056`
- `brier`: `0.19527424241893251`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.22732564883354378`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002479094510468153`
- `max_f1`: `0.8983050847457628`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5797821020879232`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_grid_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
