# Run ablation_alpha_0p5_mvtec_pill_k4_seed2_head_pca_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_pill_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9859559781799488`
- `auroc`: `0.9350791052918712`
- `brier`: `0.16698894623501148`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2570158946299981`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0022132777369129443`
- `max_f1`: `0.9591836734693877`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5226310785123369`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_pill_k4_seed2_head_pca_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
