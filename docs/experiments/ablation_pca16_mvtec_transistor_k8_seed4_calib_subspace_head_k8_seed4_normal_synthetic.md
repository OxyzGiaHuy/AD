# Run ablation_pca16_mvtec_transistor_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_transistor_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7614086793330068`
- `auroc`: `0.8216666666666667`
- `brier`: `0.1522207948186022`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1178165162075311`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002162571046501398`
- `max_f1`: `0.7272727272727273`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.49927449521955736`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_transistor_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
