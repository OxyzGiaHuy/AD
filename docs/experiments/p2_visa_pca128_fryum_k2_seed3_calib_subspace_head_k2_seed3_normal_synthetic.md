# Run p2_visa_pca128_fryum_k2_seed3_calib_subspace_head_k2_seed3_normal_synthetic

- Command: `scripts/run_p2_priority_experiments.py --tasks visa_pca128 shift_aware --run-tag full_visa --visa-classes candle capsules cashew chewinggum fryum macaroni1 macaroni2 pcb1 pcb2 pcb3 pcb4 pipe_fryum --mvtec-classes --k-shots 1 2 4 8 --seeds 0 1 2 3 4 --out-dir outputs/paper_tables --resume`
- Dataset: `visa`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9868293192708731`
- `auroc`: `0.9692`
- `brier`: `0.2958215614760266`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.30960714677969614`
- `k_shot`: `2`
- `latency_sec_per_image`: `0.00441840057571729`
- `max_f1`: `0.9424083769633508`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.4226680610141806`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `2738`

## Notes

- Predictions written to outputs/p2_visa_pca128/p2_visa_pca128_fryum_k2_seed3_calib_subspace_head_k2_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
