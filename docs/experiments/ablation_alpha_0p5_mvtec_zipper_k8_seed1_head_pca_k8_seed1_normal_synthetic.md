# Run ablation_alpha_0p5_mvtec_zipper_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_zipper_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9853649771567985`
- `auroc`: `0.9477415966386554`
- `brier`: `0.17557036662354458`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2804935158088506`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0035647779875835834`
- `max_f1`: `0.9473684210526315`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5402886310388214`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_zipper_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
