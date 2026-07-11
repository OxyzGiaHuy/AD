# Run p2_visa_pca128_pcb4_k2_seed3_calib_subspace_head_k2_seed3_normal_synthetic

- Command: `scripts/run_p2_priority_experiments.py --tasks visa_pca128 shift_aware --run-tag full_visa --visa-classes candle capsules cashew chewinggum fryum macaroni1 macaroni2 pcb1 pcb2 pcb3 pcb4 pipe_fryum --mvtec-classes --k-shots 1 2 4 8 --seeds 0 1 2 3 4 --out-dir outputs/paper_tables --resume`
- Dataset: `visa`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8806956798654173`
- `auroc`: `0.9010891089108911`
- `brier`: `0.4140319165508691`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.4457767467519537`
- `k_shot`: `2`
- `latency_sec_per_image`: `0.0058972245054458505`
- `max_f1`: `0.8597285067873304`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `2.1128533807020906`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `2738`

## Notes

- Predictions written to outputs/p2_visa_pca128/p2_visa_pca128_pcb4_k2_seed3_calib_subspace_head_k2_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
