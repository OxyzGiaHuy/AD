# Run ablation_pca128_mvtec_tile_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_tile_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9923226848350553`
- `auroc`: `0.9819624819624819`
- `brier`: `0.08672622301622297`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.11400061992243825`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.00156691004959946`
- `max_f1`: `0.9707602339181286`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.4733904623612555`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_tile_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
