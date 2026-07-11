# Run ablation_pca128_mvtec_zipper_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_zipper_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9827145605596048`
- `auroc`: `0.9385504201680672`
- `brier`: `0.08789515278473559`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.10086491176032075`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002017616658218649`
- `max_f1`: `0.944`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.42268998389593543`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_zipper_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
