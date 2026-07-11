# Run ablation_pca32_mvtec_toothbrush_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_toothbrush_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9890635186371189`
- `auroc`: `0.9722222222222222`
- `brier`: `0.11017727453586439`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.15423135104633512`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0033569268970972017`
- `max_f1`: `0.9523809523809523`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.374759144648733`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_toothbrush_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
