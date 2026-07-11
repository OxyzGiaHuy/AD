# Run ablation_pca128_mvtec_metal_nut_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_metal_nut_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9911760278866463`
- `auroc`: `0.9628543499511242`
- `brier`: `0.18769244114346695`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1893177996511045`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0021310315507909526`
- `max_f1`: `0.956989247311828`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.328613799560346`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_metal_nut_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
