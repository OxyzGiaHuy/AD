# Run ablation_alpha_0p0_mvtec_zipper_k1_seed3_head_pca_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_zipper_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9732151223993105`
- `auroc`: `0.9078256302521008`
- `brier`: `0.24015953479440735`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2846453847079876`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001922395487396133`
- `max_f1`: `0.9402390438247012`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6734501825437398`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_zipper_k1_seed3_head_pca_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
