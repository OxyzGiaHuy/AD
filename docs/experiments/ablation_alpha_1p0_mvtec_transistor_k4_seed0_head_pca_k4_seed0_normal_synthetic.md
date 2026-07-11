# Run ablation_alpha_1p0_mvtec_transistor_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_transistor_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8165898828867221`
- `auroc`: `0.8308333333333333`
- `brier`: `0.3439243493565455`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.33031973063945763`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.004458968359977007`
- `max_f1`: `0.704225352112676`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.8993967981451072`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_transistor_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
