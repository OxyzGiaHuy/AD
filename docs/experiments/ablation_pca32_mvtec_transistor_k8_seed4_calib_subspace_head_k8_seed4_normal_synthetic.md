# Run ablation_pca32_mvtec_transistor_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_transistor_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8631499361984712`
- `auroc`: `0.88625`
- `brier`: `0.14045710574510165`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.13118340896675365`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002164309900254011`
- `max_f1`: `0.7764705882352941`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.4405485624381567`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_transistor_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
