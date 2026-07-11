# Run ablation_alpha_0p75_mvtec_toothbrush_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_toothbrush_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9676082768941581`
- `auroc`: `0.9138888888888889`
- `brier`: `0.2042514798023436`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.25077813154175177`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0025617259865005813`
- `max_f1`: `0.896551724137931`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5987770182172415`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_toothbrush_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
