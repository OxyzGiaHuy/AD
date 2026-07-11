# Run ablation_pca16_mvtec_zipper_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_zipper_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9763264169863949`
- `auroc`: `0.9199054621848739`
- `brier`: `0.15503186989911608`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.17213768541615532`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001474195375841185`
- `max_f1`: `0.9477911646586346`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.8722944772025455`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_zipper_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
