# Run ablation_pca32_mvtec_toothbrush_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_toothbrush_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9902980865383536`
- `auroc`: `0.975`
- `brier`: `0.11964217885299908`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.14858465748173852`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.005569231119893846`
- `max_f1`: `0.9523809523809523`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.3880977328475295`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_toothbrush_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
