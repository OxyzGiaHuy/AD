# Run ablation_alpha_0p75_mvtec_pill_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_pill_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9830673312810914`
- `auroc`: `0.920076377523186`
- `brier`: `0.15128335931532957`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.19545309557886184`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0023229061486478336`
- `max_f1`: `0.946236559139785`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.4866019423864567`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_pill_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
