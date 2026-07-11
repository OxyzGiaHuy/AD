# Run ablation_pca64_mvtec_grid_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_grid_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9949224602742585`
- `auroc`: `0.985797827903091`
- `brier`: `0.2692004221294971`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.26921558074462115`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0017111418434442617`
- `max_f1`: `0.9655172413793104`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `3.343046376642429`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_grid_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
