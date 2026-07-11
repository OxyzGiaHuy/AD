# Run ablation_pca16_mvtec_capsule_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_capsule_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9093738109344931`
- `auroc`: `0.6972477064220184`
- `brier`: `0.1050688509633041`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.08559888640813752`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0028749452057209883`
- `max_f1`: `0.9170305676855895`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.3678221916761664`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_capsule_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
