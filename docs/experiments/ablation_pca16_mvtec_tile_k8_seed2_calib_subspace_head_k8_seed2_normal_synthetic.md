# Run ablation_pca16_mvtec_tile_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_tile_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9921613353226733`
- `auroc`: `0.9812409812409812`
- `brier`: `0.09860799459362489`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.13131260459558067`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002209142614633609`
- `max_f1`: `0.9655172413793104`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.4434068656190499`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_tile_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
