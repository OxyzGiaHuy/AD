# Run ablation_pca128_mvtec_transistor_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_transistor_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9397107109816789`
- `auroc`: `0.9545833333333333`
- `brier`: `0.15438378286875165`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2137901950441301`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.004368471596390009`
- `max_f1`: `0.8717948717948718`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.5449979636567686`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_transistor_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
