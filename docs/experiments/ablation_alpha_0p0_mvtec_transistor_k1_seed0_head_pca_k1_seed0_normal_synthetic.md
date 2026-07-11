# Run ablation_alpha_0p0_mvtec_transistor_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_transistor_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.7700436054666121`
- `auroc`: `0.815`
- `brier`: `0.24314533026957905`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.08710435748100276`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0020962305553257465`
- `max_f1`: `0.7216494845360825`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6794301086472586`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_transistor_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
