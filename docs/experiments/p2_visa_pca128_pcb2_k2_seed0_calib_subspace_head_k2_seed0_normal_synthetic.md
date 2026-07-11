# Run p2_visa_pca128_pcb2_k2_seed0_calib_subspace_head_k2_seed0_normal_synthetic

- Command: `scripts/run_p2_priority_experiments.py --tasks visa_pca128 shift_aware --run-tag full_visa --visa-classes candle capsules cashew chewinggum fryum macaroni1 macaroni2 pcb1 pcb2 pcb3 pcb4 pipe_fryum --mvtec-classes --k-shots 1 2 4 8 --seeds 0 1 2 3 4 --out-dir outputs/paper_tables --resume`
- Dataset: `visa`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7417380443915096`
- `auroc`: `0.7219`
- `brier`: `0.432237610540308`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.45197316169738777`
- `k_shot`: `2`
- `latency_sec_per_image`: `0.006522864680737257`
- `max_f1`: `0.7265917602996255`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.9779377979351236`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `2738`

## Notes

- Predictions written to outputs/p2_visa_pca128/p2_visa_pca128_pcb2_k2_seed0_calib_subspace_head_k2_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
