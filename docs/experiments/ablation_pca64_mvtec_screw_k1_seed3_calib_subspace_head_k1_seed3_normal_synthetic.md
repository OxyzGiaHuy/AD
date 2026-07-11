# Run ablation_pca64_mvtec_screw_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_screw_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7445225009300641`
- `auroc`: `0.5080959212953474`
- `brier`: `0.2562487994904383`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2561297010630369`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0020641568233259024`
- `max_f1`: `0.8530465949820788`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `4.206054994391051`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_screw_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
