# Run p2_visa_pca128_capsules_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `scripts/run_p2_priority_experiments.py --tasks visa_pca128 shift_aware --run-tag full_visa --visa-classes candle capsules cashew chewinggum fryum macaroni1 macaroni2 pcb1 pcb2 pcb3 pcb4 pipe_fryum --mvtec-classes --k-shots 1 2 4 8 --seeds 0 1 2 3 4 --out-dir outputs/paper_tables --resume`
- Dataset: `visa`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.968979866084992`
- `auroc`: `0.9446666666666667`
- `brier`: `0.35985268700763673`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3667217612266541`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.01087021587882191`
- `max_f1`: `0.9081632653061225`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `2.2555177393294787`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/p2_visa_pca128/p2_visa_pca128_capsules_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
