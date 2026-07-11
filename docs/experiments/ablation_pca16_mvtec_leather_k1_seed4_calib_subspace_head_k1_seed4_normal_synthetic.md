# Run ablation_pca16_mvtec_leather_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_leather_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `1.0`
- `auroc`: `1.0`
- `brier`: `0.24562205069448503`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2515228294557141`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0023032329345662747`
- `max_f1`: `1.0`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `1.0123411717815638`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_leather_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
