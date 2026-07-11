# Run ablation_alpha_0p25_mvtec_zipper_k8_seed2_head_pca_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_zipper_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9823103861191113`
- `auroc`: `0.936186974789916`
- `brier`: `0.1979052794774077`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.33959075236162606`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0027611308441256844`
- `max_f1`: `0.944`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5878709732657434`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_zipper_k8_seed2_head_pca_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
