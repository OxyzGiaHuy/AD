# Run ablation_pca16_mvtec_screw_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_screw_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7878229050949288`
- `auroc`: `0.5224431235908997`
- `brier`: `0.27364349412116795`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2902557511086343`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0020390119287185373`
- `max_f1`: `0.8530465949820788`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `1.8682137398548655`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_screw_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
