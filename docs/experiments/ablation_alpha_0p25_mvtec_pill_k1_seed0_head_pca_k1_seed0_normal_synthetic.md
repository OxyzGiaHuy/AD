# Run ablation_alpha_0p25_mvtec_pill_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_pill_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9815763015970989`
- `auroc`: `0.9113475177304965`
- `brier`: `0.21052034457671182`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2874695619423232`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002801815549770515`
- `max_f1`: `0.9527027027027027`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6137875705068517`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_pill_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
