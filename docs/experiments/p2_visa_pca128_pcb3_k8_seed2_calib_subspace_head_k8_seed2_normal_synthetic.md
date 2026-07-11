# Run p2_visa_pca128_pcb3_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic

- Command: `scripts/run_p2_priority_experiments.py --tasks visa_pca128 shift_aware --run-tag full_visa --visa-classes candle capsules cashew chewinggum fryum macaroni1 macaroni2 pcb1 pcb2 pcb3 pcb4 pipe_fryum --mvtec-classes --k-shots 1 2 4 8 --seeds 0 1 2 3 4 --out-dir outputs/paper_tables --resume`
- Dataset: `visa`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7722896501077875`
- `auroc`: `0.733960396039604`
- `brier`: `0.24869719197073098`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.22663639251731188`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.006378622586602595`
- `max_f1`: `0.6910994764397905`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.8156631785395269`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/p2_visa_pca128/p2_visa_pca128_pcb3_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
