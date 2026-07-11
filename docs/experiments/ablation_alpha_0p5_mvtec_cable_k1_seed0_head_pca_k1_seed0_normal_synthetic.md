# Run ablation_alpha_0p5_mvtec_cable_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_cable_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9302942066343576`
- `auroc`: `0.860944527736132`
- `brier`: `0.23341603248356696`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.0002818691730498424`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0020971076687177023`
- `max_f1`: `0.8433734939759037`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.659347282614037`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_cable_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
