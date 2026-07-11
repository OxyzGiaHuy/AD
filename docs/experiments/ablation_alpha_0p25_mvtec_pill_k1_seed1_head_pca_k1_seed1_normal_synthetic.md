# Run ablation_alpha_0p25_mvtec_pill_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_pill_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9845634877314412`
- `auroc`: `0.9288052373158756`
- `brier`: `0.20405406359064748`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2844493724628837`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002389427519843964`
- `max_f1`: `0.9527027027027027`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6006222266805502`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_pill_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
