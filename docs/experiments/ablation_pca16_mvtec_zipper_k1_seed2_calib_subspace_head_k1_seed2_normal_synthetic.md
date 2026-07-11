# Run ablation_pca16_mvtec_zipper_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_zipper_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9799297140687011`
- `auroc`: `0.930672268907563`
- `brier`: `0.1413073108834756`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.16166949671822667`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0014112890876878965`
- `max_f1`: `0.9477911646586346`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `1.1996438280370334`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_zipper_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
