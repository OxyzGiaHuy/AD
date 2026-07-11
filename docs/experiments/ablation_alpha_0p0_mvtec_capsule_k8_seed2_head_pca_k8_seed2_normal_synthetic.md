# Run ablation_alpha_0p0_mvtec_capsule_k8_seed2_head_pca_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_capsule_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9744163030801744`
- `auroc`: `0.9006781013163143`
- `brier`: `0.23756796554591852`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3180507674361721`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002572808809804194`
- `max_f1`: `0.9411764705882353`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6682478796760193`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_capsule_k8_seed2_head_pca_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
