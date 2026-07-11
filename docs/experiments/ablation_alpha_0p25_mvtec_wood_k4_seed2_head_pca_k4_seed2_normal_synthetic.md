# Run ablation_alpha_0p25_mvtec_wood_k4_seed2_head_pca_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_wood_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9856600899807066`
- `auroc`: `0.956140350877193`
- `brier`: `0.21807572860140756`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.36953231088722804`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.003694955377450472`
- `max_f1`: `0.9448818897637795`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6290202410301824`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_wood_k4_seed2_head_pca_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
