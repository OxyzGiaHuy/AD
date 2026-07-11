# Run ablation_alpha_1p0_mvtec_metal_nut_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_metal_nut_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9353058328988346`
- `auroc`: `0.7575757575757576`
- `brier`: `0.16195874163924337`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.08899573346842893`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.003076782547261404`
- `max_f1`: `0.8975609756097561`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5076716366201423`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_metal_nut_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
