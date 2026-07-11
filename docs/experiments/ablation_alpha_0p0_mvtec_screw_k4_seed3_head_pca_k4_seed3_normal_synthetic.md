# Run ablation_alpha_0p0_mvtec_screw_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_screw_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8719180259137462`
- `auroc`: `0.7526132404181185`
- `brier`: `0.2588339019180886`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.27032665871083733`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0021410675719380377`
- `max_f1`: `0.8784313725490196`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.710824738097281`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_screw_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
