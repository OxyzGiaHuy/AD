# Run ablation_alpha_0p75_mvtec_tile_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_tile_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9785212977405655`
- `auroc`: `0.9383116883116883`
- `brier`: `0.19573195056503923`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.27827415965561175`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.001788346845115352`
- `max_f1`: `0.9454545454545454`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5801103172484867`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_tile_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
