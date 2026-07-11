# Run ablation_pca16_mvtec_wood_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_wood_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9690895104037819`
- `auroc`: `0.9078947368421053`
- `brier`: `0.2405049046584241`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.24050560254084907`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0015679382825199563`
- `max_f1`: `0.928`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `3.904116627037984`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_wood_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
