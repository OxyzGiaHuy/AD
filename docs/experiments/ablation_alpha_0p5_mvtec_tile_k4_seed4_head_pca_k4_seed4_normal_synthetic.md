# Run ablation_alpha_0p5_mvtec_tile_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_tile_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.992483389183627`
- `auroc`: `0.9823232323232324`
- `brier`: `0.19536444706644476`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.28418259437267596`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002336506007446183`
- `max_f1`: `0.9764705882352941`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5808981064780083`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_tile_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
