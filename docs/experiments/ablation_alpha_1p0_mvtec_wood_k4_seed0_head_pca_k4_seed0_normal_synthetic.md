# Run ablation_alpha_1p0_mvtec_wood_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_wood_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9686139962750064`
- `auroc`: `0.9618421052631579`
- `brier`: `0.17826413944415395`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1653507668760758`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.003073566840796531`
- `max_f1`: `0.9836065573770492`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.540845848785406`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_wood_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
