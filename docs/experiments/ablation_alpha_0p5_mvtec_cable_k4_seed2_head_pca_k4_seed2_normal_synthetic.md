# Run ablation_alpha_0p5_mvtec_cable_k4_seed2_head_pca_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_cable_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9606138154342234`
- `auroc`: `0.9194152923538231`
- `brier`: `0.2293651280249197`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.02383429884910588`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002559964917600155`
- `max_f1`: `0.9142857142857143`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.650747617653879`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_cable_k4_seed2_head_pca_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
