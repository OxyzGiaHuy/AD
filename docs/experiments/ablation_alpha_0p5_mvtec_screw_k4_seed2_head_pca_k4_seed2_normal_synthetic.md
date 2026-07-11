# Run ablation_alpha_0p5_mvtec_screw_k4_seed2_head_pca_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_screw_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8961426723225829`
- `auroc`: `0.7669604427136708`
- `brier`: `0.19906324530046807`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.11259000971913335`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.003653434768784791`
- `max_f1`: `0.8778625954198473`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5888267734025153`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_screw_k4_seed2_head_pca_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
