# Run p2_visa_pca128_cashew_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `scripts/run_p2_priority_experiments.py --tasks visa_pca128 shift_aware --run-tag full_visa --visa-classes candle capsules cashew chewinggum fryum macaroni1 macaroni2 pcb1 pcb2 pcb3 pcb4 pipe_fryum --mvtec-classes --k-shots 1 2 4 8 --seeds 0 1 2 3 4 --out-dir outputs/paper_tables --resume`
- Dataset: `visa`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9635821726997402`
- `auroc`: `0.93`
- `brier`: `0.3314744809682052`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3323446114857992`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.004856248733898004`
- `max_f1`: `0.9142857142857143`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `2.4112272304642137`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/p2_visa_pca128/p2_visa_pca128_cashew_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
