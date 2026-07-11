# Run ablation_alpha_1p0_mvtec_pill_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_pill_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9661309186122957`
- `auroc`: `0.8532460447354064`
- `brier`: `0.14496533918176613`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.13035970783519168`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0020814528633020593`
- `max_f1`: `0.9256756756756757`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.4708510052647014`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_pill_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
