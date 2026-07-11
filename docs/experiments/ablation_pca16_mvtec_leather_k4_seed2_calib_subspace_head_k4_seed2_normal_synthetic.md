# Run ablation_pca16_mvtec_leather_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_leather_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9889469914354158`
- `auroc`: `0.9690896739130435`
- `brier`: `0.188742599593594`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.19180877146220973`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0024644901014624103`
- `max_f1`: `0.9528795811518325`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.6033434511351634`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_leather_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
