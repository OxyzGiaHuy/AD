# Run ablation_alpha_0p5_mvtec_pill_k1_seed3_head_pca_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_pill_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.972541228336525`
- `auroc`: `0.8687943262411347`
- `brier`: `0.1788133665105689`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2238322125223582`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002143130654435672`
- `max_f1`: `0.9455782312925171`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5479785577728868`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_pill_k1_seed3_head_pca_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
