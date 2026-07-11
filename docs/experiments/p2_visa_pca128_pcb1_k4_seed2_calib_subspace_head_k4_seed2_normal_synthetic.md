# Run p2_visa_pca128_pcb1_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic

- Command: `scripts/run_p2_priority_experiments.py --tasks visa_pca128 shift_aware --run-tag full_visa --visa-classes candle capsules cashew chewinggum fryum macaroni1 macaroni2 pcb1 pcb2 pcb3 pcb4 pipe_fryum --mvtec-classes --k-shots 1 2 4 8 --seeds 0 1 2 3 4 --out-dir outputs/paper_tables --resume`
- Dataset: `visa`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9073719219809147`
- `auroc`: `0.9128`
- `brier`: `0.36872708522856096`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.4069353172183038`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.007239814018830657`
- `max_f1`: `0.8521739130434782`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `2.345551035567535`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/p2_visa_pca128/p2_visa_pca128_pcb1_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
