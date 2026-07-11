# Run p2_visa_pca128_pcb3_k2_seed2_calib_subspace_head_k2_seed2_normal_synthetic

- Command: `scripts/run_p2_priority_experiments.py --tasks visa_pca128 shift_aware --run-tag full_visa --visa-classes candle capsules cashew chewinggum fryum macaroni1 macaroni2 pcb1 pcb2 pcb3 pcb4 pipe_fryum --mvtec-classes --k-shots 1 2 4 8 --seeds 0 1 2 3 4 --out-dir outputs/paper_tables --resume`
- Dataset: `visa`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.6875588613138437`
- `auroc`: `0.6666336633663367`
- `brier`: `0.4578347721100966`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.46261789238274986`
- `k_shot`: `2`
- `latency_sec_per_image`: `0.007402153268678865`
- `max_f1`: `0.6787330316742082`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `2.289667151128524`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `2738`

## Notes

- Predictions written to outputs/p2_visa_pca128/p2_visa_pca128_pcb3_k2_seed2_calib_subspace_head_k2_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
