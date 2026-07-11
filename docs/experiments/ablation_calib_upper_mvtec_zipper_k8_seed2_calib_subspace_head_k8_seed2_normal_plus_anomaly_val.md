# Run ablation_calib_upper_mvtec_zipper_k8_seed2_calib_subspace_head_k8_seed2_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_zipper_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9840853015334653`
- `auroc`: `0.9470486111111112`
- `brier`: `0.09190765137456333`
- `calibration_anomaly_val_count`: `11`
- `ece`: `0.10769763074682227`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0015807760879397391`
- `max_f1`: `0.9411764705882353`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.33181060510990934`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_zipper_k8_seed2_calib_subspace_head_k8_seed2_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
