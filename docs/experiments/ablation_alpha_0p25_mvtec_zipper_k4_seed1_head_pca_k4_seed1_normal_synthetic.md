# Run ablation_alpha_0p25_mvtec_zipper_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_zipper_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9857670100752425`
- `auroc`: `0.9490546218487395`
- `brier`: `0.19751750630609669`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3275264860778455`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.004061803998832671`
- `max_f1`: `0.9465020576131687`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5871400073316585`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_zipper_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
