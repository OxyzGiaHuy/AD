# Run ablation_alpha_1p0_mvtec_pill_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_pill_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9657144724391863`
- `auroc`: `0.8806601200218221`
- `brier`: `0.13773324394608966`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1615715037562889`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.004602094409530034`
- `max_f1`: `0.936026936026936`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.45241698484017295`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_pill_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
