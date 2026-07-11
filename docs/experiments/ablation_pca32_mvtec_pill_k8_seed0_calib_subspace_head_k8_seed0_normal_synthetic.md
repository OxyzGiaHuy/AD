# Run ablation_pca32_mvtec_pill_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_pill_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9806172942128523`
- `auroc`: `0.9020731042007638`
- `brier`: `0.0873887768100868`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.07420438767583692`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.007701427636746161`
- `max_f1`: `0.9427609427609428`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.29033724965164664`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_pill_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
