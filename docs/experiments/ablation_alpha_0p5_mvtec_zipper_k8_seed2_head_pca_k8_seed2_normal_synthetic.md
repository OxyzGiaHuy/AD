# Run ablation_alpha_0p5_mvtec_zipper_k8_seed2_head_pca_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_zipper_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9829052113328854`
- `auroc`: `0.9385504201680672`
- `brier`: `0.17411890680653652`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2567154946706153`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002255219275390865`
- `max_f1`: `0.9477911646586346`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5368097485406547`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_zipper_k8_seed2_head_pca_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
