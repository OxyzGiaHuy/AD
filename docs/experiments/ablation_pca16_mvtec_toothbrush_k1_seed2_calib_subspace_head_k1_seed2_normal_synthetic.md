# Run ablation_pca16_mvtec_toothbrush_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_toothbrush_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9665154938106586`
- `auroc`: `0.9055555555555556`
- `brier`: `0.14859663005297877`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.15813088353856325`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0015042016193980263`
- `max_f1`: `0.90625`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.6691553121792111`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_toothbrush_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
