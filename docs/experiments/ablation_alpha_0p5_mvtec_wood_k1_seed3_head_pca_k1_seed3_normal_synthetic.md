# Run ablation_alpha_0p5_mvtec_wood_k1_seed3_head_pca_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_wood_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9858546261134749`
- `auroc`: `0.9587719298245614`
- `brier`: `0.19940524378899432`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.18970859729790993`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.005308818119236186`
- `max_f1`: `0.957983193277311`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5900849290102224`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_wood_k1_seed3_head_pca_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
