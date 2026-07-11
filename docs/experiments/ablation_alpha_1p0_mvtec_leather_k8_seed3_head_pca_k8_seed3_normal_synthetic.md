# Run ablation_alpha_1p0_mvtec_leather_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_leather_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9980364941795518`
- `auroc`: `0.993546195652174`
- `brier`: `0.16903797696349868`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.11514652183940327`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0030061055515562336`
- `max_f1`: `0.9837837837837838`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5158139091769691`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_leather_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
