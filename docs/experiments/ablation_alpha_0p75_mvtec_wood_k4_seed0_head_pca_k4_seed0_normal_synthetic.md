# Run ablation_alpha_0p75_mvtec_wood_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_wood_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9978300553959006`
- `auroc`: `0.9929824561403509`
- `brier`: `0.17950340983596036`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.11264882359323625`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0018839299490180197`
- `max_f1`: `0.975609756097561`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5450184980676186`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_wood_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
