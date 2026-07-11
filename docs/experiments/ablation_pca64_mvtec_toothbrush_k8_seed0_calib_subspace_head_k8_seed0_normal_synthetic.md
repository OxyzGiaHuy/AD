# Run ablation_pca64_mvtec_toothbrush_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_toothbrush_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9902702275906299`
- `auroc`: `0.975`
- `brier`: `0.10312472124962897`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.13142648833759482`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.00358119708973737`
- `max_f1`: `0.9523809523809523`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.5125996170883668`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_toothbrush_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
