# Run ablation_pca64_mvtec_metal_nut_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_metal_nut_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9950370483013878`
- `auroc`: `0.978494623655914`
- `brier`: `0.07832981280882291`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.08482325178692515`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.00209860024244889`
- `max_f1`: `0.9633507853403142`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.3537614639294834`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_metal_nut_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
