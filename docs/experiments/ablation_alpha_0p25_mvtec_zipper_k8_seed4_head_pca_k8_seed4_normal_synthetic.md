# Run ablation_alpha_0p25_mvtec_zipper_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_zipper_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9966437591151867`
- `auroc`: `0.9889705882352942`
- `brier`: `0.18656035781215477`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.37056383885295185`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0025816200584765302`
- `max_f1`: `0.9874476987447699`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5645968060507126`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_zipper_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
