# Run ablation_alpha_0p75_mvtec_hazelnut_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_hazelnut_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.95588113339908`
- `auroc`: `0.9085714285714286`
- `brier`: `0.22863929658282692`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.22491626360199668`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0028654414144429294`
- `max_f1`: `0.8805970149253731`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.649290871335114`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_hazelnut_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
