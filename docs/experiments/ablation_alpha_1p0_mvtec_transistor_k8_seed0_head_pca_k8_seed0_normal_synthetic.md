# Run ablation_alpha_1p0_mvtec_transistor_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_transistor_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8171911574935757`
- `auroc`: `0.8541666666666666`
- `brier`: `0.3354696122815282`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.33208883702754977`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0037664271518588065`
- `max_f1`: `0.7368421052631579`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.8806278972857977`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_transistor_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
