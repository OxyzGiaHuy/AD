# Run p2_visa_pca128_pcb1_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `scripts/run_p2_priority_experiments.py --tasks visa_pca128 shift_aware --run-tag full_visa --visa-classes candle capsules cashew chewinggum fryum macaroni1 macaroni2 pcb1 pcb2 pcb3 pcb4 pipe_fryum --mvtec-classes --k-shots 1 2 4 8 --seeds 0 1 2 3 4 --out-dir outputs/paper_tables --resume`
- Dataset: `visa`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.872395816761176`
- `auroc`: `0.8872`
- `brier`: `0.3632441737043573`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.4000587261188775`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.007593677621334791`
- `max_f1`: `0.8266666666666667`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `2.025666446519504`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/p2_visa_pca128/p2_visa_pca128_pcb1_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
