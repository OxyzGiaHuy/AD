# Run ablation_alpha_0p75_mvtec_metal_nut_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_metal_nut_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9763100414206815`
- `auroc`: `0.9203323558162267`
- `brier`: `0.16284130464107177`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.18690900543461675`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0026667497242274492`
- `max_f1`: `0.9518716577540107`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.510467286064683`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_metal_nut_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
