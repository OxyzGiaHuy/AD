# Run ablation_alpha_1p0_mvtec_bottle_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_bottle_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9980016875079012`
- `auroc`: `0.9936507936507937`
- `brier`: `0.16041835297828325`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.24436672337083926`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0028754474752279648`
- `max_f1`: `0.9767441860465116`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.4985093760121979`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_bottle_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
