# Run ablation_alpha_1p0_mvtec_leather_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_leather_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9996567505720825`
- `auroc`: `0.9989809782608695`
- `brier`: `0.16864927483863426`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.183481972544424`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.001994390416169359`
- `max_f1`: `0.994535519125683`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5132445296548087`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_leather_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
