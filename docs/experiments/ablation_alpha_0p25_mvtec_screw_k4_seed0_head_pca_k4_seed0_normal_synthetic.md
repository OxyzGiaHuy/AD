# Run ablation_alpha_0p25_mvtec_screw_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_screw_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8665876568335923`
- `auroc`: `0.7276081164172986`
- `brier`: `0.22666669792270805`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.23211709950119255`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0018403346883133053`
- `max_f1`: `0.8828125`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6463313322993176`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_screw_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
