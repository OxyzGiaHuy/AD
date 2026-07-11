# Run ablation_alpha_0p25_mvtec_tile_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_tile_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9927648182852808`
- `auroc`: `0.983044733044733`
- `brier`: `0.2194202601990838`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.27243454155758917`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002393621839901321`
- `max_f1`: `0.9764705882352941`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.631794072112792`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_tile_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
