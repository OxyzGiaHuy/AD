# Run ablation_alpha_1p0_mvtec_cable_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_cable_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.93976173995164`
- `auroc`: `0.8862443778110944`
- `brier`: `0.2515928987244501`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1265939211845398`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0023398613184690475`
- `max_f1`: `0.8457142857142858`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.7014482559410579`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_cable_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
