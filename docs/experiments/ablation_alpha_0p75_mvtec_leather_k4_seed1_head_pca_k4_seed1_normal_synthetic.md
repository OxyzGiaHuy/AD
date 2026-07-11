# Run ablation_alpha_0p75_mvtec_leather_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_leather_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.996031112883925`
- `auroc`: `0.9860733695652174`
- `brier`: `0.18450736418708194`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.20005532858833194`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0025356070799452644`
- `max_f1`: `0.989010989010989`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5557422672436236`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_leather_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
