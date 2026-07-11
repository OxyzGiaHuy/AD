# Run ablation_alpha_0p25_mvtec_screw_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_screw_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9128495604416671`
- `auroc`: `0.7893010862881739`
- `brier`: `0.2199636970949775`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.20930431038141253`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0017923280014656485`
- `max_f1`: `0.8613138686131386`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6326991087283579`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_screw_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
