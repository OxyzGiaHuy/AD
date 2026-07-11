# Run ablation_alpha_1p0_mvtec_toothbrush_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_toothbrush_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9623018227758939`
- `auroc`: `0.8958333333333334`
- `brier`: `0.20100846263539016`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.04514937031836734`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.005400019830891064`
- `max_f1`: `0.8823529411764706`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5911639394841958`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_toothbrush_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
