# Run p2_visa_pca128_capsules_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `scripts/run_p2_priority_experiments.py --tasks visa_pca128 shift_aware --run-tag full_visa --visa-classes candle capsules cashew chewinggum fryum macaroni1 macaroni2 pcb1 pcb2 pcb3 pcb4 pipe_fryum --mvtec-classes --k-shots 1 2 4 8 --seeds 0 1 2 3 4 --out-dir outputs/paper_tables --resume`
- Dataset: `visa`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9850988545091326`
- `auroc`: `0.9733333333333334`
- `brier`: `0.09186466862369183`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.11004621351603414`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.005498190363869071`
- `max_f1`: `0.9393939393939394`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.39955429946041165`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/p2_visa_pca128/p2_visa_pca128_capsules_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
