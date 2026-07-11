# Run p2_visa_pca128_pcb2_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `scripts/run_p2_priority_experiments.py --tasks visa_pca128 shift_aware --run-tag full_visa --visa-classes candle capsules cashew chewinggum fryum macaroni1 macaroni2 pcb1 pcb2 pcb3 pcb4 pipe_fryum --mvtec-classes --k-shots 1 2 4 8 --seeds 0 1 2 3 4 --out-dir outputs/paper_tables --resume`
- Dataset: `visa`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.6489239084409939`
- `auroc`: `0.6282`
- `brier`: `0.49574911318315046`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.49747507542371744`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.007645037863403559`
- `max_f1`: `0.6959706959706959`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `4.055987496531583`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/p2_visa_pca128/p2_visa_pca128_pcb2_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
