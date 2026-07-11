# Run p2_visa_pca128_pcb3_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `scripts/run_p2_priority_experiments.py --tasks visa_pca128 shift_aware --run-tag full_visa --visa-classes candle capsules cashew chewinggum fryum macaroni1 macaroni2 pcb1 pcb2 pcb3 pcb4 pipe_fryum --mvtec-classes --k-shots 1 2 4 8 --seeds 0 1 2 3 4 --out-dir outputs/paper_tables --resume`
- Dataset: `visa`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7827054369209017`
- `auroc`: `0.7544554455445545`
- `brier`: `0.31406833115053423`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3106493172397958`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0064053803274584055`
- `max_f1`: `0.7106598984771574`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.1456907379716`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/p2_visa_pca128/p2_visa_pca128_pcb3_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
