# Run ablation_pca128_mvtec_bottle_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_bottle_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9997519841269841`
- `auroc`: `0.9992063492063492`
- `brier`: `0.06436587473494751`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.09246405412678618`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002579483057720115`
- `max_f1`: `0.9921259842519685`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.193471900875652`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_bottle_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
