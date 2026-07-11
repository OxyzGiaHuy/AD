# Run ablation_alpha_1p0_mvtec_pill_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_pill_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9621462065209553`
- `auroc`: `0.871658483360611`
- `brier`: `0.13859549018897835`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.19712508938269702`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002217341839017982`
- `max_f1`: `0.9491525423728814`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.45464738749222683`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_pill_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
