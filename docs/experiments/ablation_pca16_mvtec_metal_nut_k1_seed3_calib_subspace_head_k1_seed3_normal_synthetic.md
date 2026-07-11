# Run ablation_pca16_mvtec_metal_nut_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_metal_nut_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9309545599510848`
- `auroc`: `0.7961876832844574`
- `brier`: `0.13352382492986345`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.14198681922666226`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0013504384976366292`
- `max_f1`: `0.9238578680203046`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `1.4725038405028723`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_metal_nut_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
