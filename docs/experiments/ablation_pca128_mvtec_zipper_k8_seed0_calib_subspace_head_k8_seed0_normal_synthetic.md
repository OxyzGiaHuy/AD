# Run ablation_pca128_mvtec_zipper_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_zipper_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9820877673942381`
- `auroc`: `0.9380252100840336`
- `brier`: `0.08206579392309468`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.09146940512798535`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0018259431328007717`
- `max_f1`: `0.9516129032258065`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.3554984889393558`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_zipper_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
