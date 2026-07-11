# Run ablation_pca64_mvtec_hazelnut_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_hazelnut_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9899061310725776`
- `auroc`: `0.9842857142857143`
- `brier`: `0.3387566038060723`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.34857281798666173`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002190169014713981`
- `max_f1`: `0.9645390070921985`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `2.03332868261702`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_hazelnut_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
