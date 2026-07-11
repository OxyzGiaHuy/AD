# Run ablation_alpha_0p75_mvtec_transistor_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_transistor_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.918090608361131`
- `auroc`: `0.9320833333333334`
- `brier`: `0.29929245874368143`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.26303020834922797`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002696825284510851`
- `max_f1`: `0.8314606741573034`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.7953323295318252`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_transistor_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
