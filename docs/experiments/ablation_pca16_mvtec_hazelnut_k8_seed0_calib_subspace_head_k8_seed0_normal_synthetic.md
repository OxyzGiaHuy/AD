# Run ablation_pca16_mvtec_hazelnut_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_hazelnut_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8986937846388274`
- `auroc`: `0.8314285714285714`
- `brier`: `0.2557793258462503`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2646785313432866`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0021411794153126805`
- `max_f1`: `0.8441558441558441`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.9105525887409003`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_hazelnut_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
