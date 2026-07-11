# Run ablation_alpha_1p0_mvtec_hazelnut_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_hazelnut_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9238274622103747`
- `auroc`: `0.8475`
- `brier`: `0.23440013033959137`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.060362128236077006`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0019913855770772155`
- `max_f1`: `0.835820895522388`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.662296214831849`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_hazelnut_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
