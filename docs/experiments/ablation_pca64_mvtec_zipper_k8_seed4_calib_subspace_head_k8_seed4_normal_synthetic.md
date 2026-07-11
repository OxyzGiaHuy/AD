# Run ablation_pca64_mvtec_zipper_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_zipper_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9931848610070828`
- `auroc`: `0.9753151260504201`
- `brier`: `0.07561923396495364`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.09570283483750873`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.001409731213225434`
- `max_f1`: `0.9554655870445344`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.2950368090576661`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_zipper_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
