# Run ablation_pca16_mvtec_zipper_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_zipper_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.975006400364988`
- `auroc`: `0.9138655462184874`
- `brier`: `0.09373757383238414`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.09350492856126053`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002982491368292183`
- `max_f1`: `0.9402390438247012`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.33360514918770934`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_zipper_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
