# Run ablation_alpha_1p0_mvtec_transistor_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_transistor_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9400946583561932`
- `auroc`: `0.95625`
- `brier`: `0.328340926575996`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.32668774187564853`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002787676118314266`
- `max_f1`: `0.8717948717948718`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.8622504936618085`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_transistor_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
