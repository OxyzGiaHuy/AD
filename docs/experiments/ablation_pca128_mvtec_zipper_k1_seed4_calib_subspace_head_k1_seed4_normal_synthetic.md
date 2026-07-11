# Run ablation_pca128_mvtec_zipper_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_zipper_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9684367192540072`
- `auroc`: `0.8933823529411765`
- `brier`: `0.19780360721079823`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.20383221424178571`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002689925361646722`
- `max_f1`: `0.9407114624505929`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.1870684135467604`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_zipper_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
