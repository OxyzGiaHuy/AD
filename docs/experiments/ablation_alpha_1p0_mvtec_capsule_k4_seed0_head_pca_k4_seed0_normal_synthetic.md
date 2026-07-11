# Run ablation_alpha_1p0_mvtec_capsule_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_capsule_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9636613192924569`
- `auroc`: `0.8476266453928999`
- `brier`: `0.14401800838038656`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.16335122603358643`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002645845976517056`
- `max_f1`: `0.9251101321585903`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.46599066095829056`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_capsule_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
