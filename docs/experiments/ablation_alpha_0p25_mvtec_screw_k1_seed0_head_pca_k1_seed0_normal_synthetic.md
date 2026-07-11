# Run ablation_alpha_0p25_mvtec_screw_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_screw_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8068137783846392`
- `auroc`: `0.617339618774339`
- `brier`: `0.23212723702934523`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.20664547272026543`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0017962145968340338`
- `max_f1`: `0.8717948717948718`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6573296908148157`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_screw_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
