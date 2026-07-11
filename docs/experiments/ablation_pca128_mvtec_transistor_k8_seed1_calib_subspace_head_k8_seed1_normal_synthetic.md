# Run ablation_pca128_mvtec_transistor_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_transistor_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.898705058897287`
- `auroc`: `0.9229166666666667`
- `brier`: `0.19195953497143703`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2522370417043567`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.001636705994606018`
- `max_f1`: `0.8292682926829268`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.7003444418742533`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_transistor_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
