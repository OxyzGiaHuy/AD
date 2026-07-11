# Run ablation_alpha_1p0_mvtec_transistor_k4_seed2_head_pca_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_transistor_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.83439722131399`
- `auroc`: `0.85`
- `brier`: `0.3398917425524198`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3290390765666962`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0019670541770756243`
- `max_f1`: `0.75`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.8899632941843666`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_transistor_k4_seed2_head_pca_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
