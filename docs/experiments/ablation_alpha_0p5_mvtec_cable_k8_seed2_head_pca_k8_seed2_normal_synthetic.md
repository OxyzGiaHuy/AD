# Run ablation_alpha_0p5_mvtec_cable_k8_seed2_head_pca_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_cable_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9636213256393608`
- `auroc`: `0.9226011994002998`
- `brier`: `0.2269053493409344`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2805023388067881`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002442154971261819`
- `max_f1`: `0.9257142857142857`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6457246425646805`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_cable_k8_seed2_head_pca_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
