# Run ablation_pca16_mvtec_leather_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_leather_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9858113589213617`
- `auroc`: `0.9602581521739131`
- `brier`: `0.23302655921888998`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2420935635605166`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002150945801047548`
- `max_f1`: `0.9528795811518325`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `3.297398985589007`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_leather_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
