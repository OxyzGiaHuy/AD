# Run ablation_alpha_1p0_mvtec_zipper_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_zipper_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9770328763229369`
- `auroc`: `0.9225315126050421`
- `brier`: `0.15960171368079704`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.24949519721088032`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0018083829901471044`
- `max_f1`: `0.943089430894309`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5001709020087276`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_zipper_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
