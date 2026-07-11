# Run ablation_alpha_0p0_mvtec_pill_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_pill_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9862785245409285`
- `auroc`: `0.9318057828696127`
- `brier`: `0.24264282951721844`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.34107458734226803`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.003675321518571791`
- `max_f1`: `0.9494949494949495`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.678425394035429`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_pill_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
