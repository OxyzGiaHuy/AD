# Run ablation_alpha_0p0_mvtec_screw_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_screw_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.7703676600227763`
- `auroc`: `0.5650748104119697`
- `brier`: `0.26345730550270474`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2711117211729288`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0027122601168230176`
- `max_f1`: `0.8603773584905661`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.7200910286055306`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_screw_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
