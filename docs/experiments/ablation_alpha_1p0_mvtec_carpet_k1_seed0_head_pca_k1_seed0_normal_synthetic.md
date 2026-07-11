# Run ablation_alpha_1p0_mvtec_carpet_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_carpet_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9842137840092948`
- `auroc`: `0.9470304975922953`
- `brier`: `0.17449565750434168`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.09805721808702518`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0025798650856456184`
- `max_f1`: `0.9485714285714286`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5333652709161552`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_carpet_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
