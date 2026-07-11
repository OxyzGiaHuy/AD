# Run ablation_pca32_mvtec_bottle_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_bottle_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9888512846948729`
- `auroc`: `0.9722222222222222`
- `brier`: `0.06939761285767967`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1024216999081019`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.003149525026779577`
- `max_f1`: `0.9767441860465116`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.3693810092556519`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_bottle_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
