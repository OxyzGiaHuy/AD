# Run ablation_alpha_0p5_mvtec_cable_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_cable_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9230575759732929`
- `auroc`: `0.8528860569715142`
- `brier`: `0.23408476105295192`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.011758105357488044`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002218858003616333`
- `max_f1`: `0.8176795580110497`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6607767541747451`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_cable_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
