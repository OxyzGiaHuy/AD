# Run ablation_alpha_0p75_mvtec_carpet_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_carpet_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9952950802878738`
- `auroc`: `0.9851524879614767`
- `brier`: `0.15618299771390398`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.31107294610422903`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0028325291748484993`
- `max_f1`: `0.9723756906077348`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.49593487252450047`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_carpet_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
