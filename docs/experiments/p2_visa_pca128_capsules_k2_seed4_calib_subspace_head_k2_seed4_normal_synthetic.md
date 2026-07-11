# Run p2_visa_pca128_capsules_k2_seed4_calib_subspace_head_k2_seed4_normal_synthetic

- Command: `scripts/run_p2_priority_experiments.py --tasks visa_pca128 shift_aware --run-tag full_visa --visa-classes candle capsules cashew chewinggum fryum macaroni1 macaroni2 pcb1 pcb2 pcb3 pcb4 pipe_fryum --mvtec-classes --k-shots 1 2 4 8 --seeds 0 1 2 3 4 --out-dir outputs/paper_tables --resume`
- Dataset: `visa`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9775895824117435`
- `auroc`: `0.9618333333333333`
- `brier`: `0.25814377605851746`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3024558370932936`
- `k_shot`: `2`
- `latency_sec_per_image`: `0.00886227588634938`
- `max_f1`: `0.9313725490196079`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.9992724120425359`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `2738`

## Notes

- Predictions written to outputs/p2_visa_pca128/p2_visa_pca128_capsules_k2_seed4_calib_subspace_head_k2_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
