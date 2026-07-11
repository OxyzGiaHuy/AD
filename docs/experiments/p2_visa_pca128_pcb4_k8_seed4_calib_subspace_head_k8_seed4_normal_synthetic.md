# Run p2_visa_pca128_pcb4_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `scripts/run_p2_priority_experiments.py --tasks visa_pca128 shift_aware --run-tag full_visa --visa-classes candle capsules cashew chewinggum fryum macaroni1 macaroni2 pcb1 pcb2 pcb3 pcb4 pipe_fryum --mvtec-classes --k-shots 1 2 4 8 --seeds 0 1 2 3 4 --out-dir outputs/paper_tables --resume`
- Dataset: `visa`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9212156290191476`
- `auroc`: `0.9280198019801981`
- `brier`: `0.13410442224295552`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.14370583158811154`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.008037723730600889`
- `max_f1`: `0.8732394366197183`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.5009239944693703`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/p2_visa_pca128/p2_visa_pca128_pcb4_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
