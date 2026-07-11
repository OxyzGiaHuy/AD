# Run ablation_pca128_mvtec_hazelnut_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_hazelnut_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9964005324776817`
- `auroc`: `0.9935714285714285`
- `brier`: `0.28321305857862755`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3095894371921366`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002131547914309935`
- `max_f1`: `0.9655172413793104`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.2693040195470608`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_hazelnut_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
