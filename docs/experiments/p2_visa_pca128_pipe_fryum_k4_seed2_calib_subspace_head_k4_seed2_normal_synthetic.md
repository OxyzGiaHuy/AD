# Run p2_visa_pca128_pipe_fryum_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic

- Command: `scripts/run_p2_priority_experiments.py --tasks visa_pca128 shift_aware --run-tag full_visa --visa-classes candle capsules cashew chewinggum fryum macaroni1 macaroni2 pcb1 pcb2 pcb3 pcb4 pipe_fryum --mvtec-classes --k-shots 1 2 4 8 --seeds 0 1 2 3 4 --out-dir outputs/paper_tables --resume`
- Dataset: `visa`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9879989639547592`
- `auroc`: `0.9762`
- `brier`: `0.2815084894455317`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2989765149851639`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.004625335820019245`
- `max_f1`: `0.9560975609756097`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.6544944197561378`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/p2_visa_pca128/p2_visa_pca128_pipe_fryum_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
