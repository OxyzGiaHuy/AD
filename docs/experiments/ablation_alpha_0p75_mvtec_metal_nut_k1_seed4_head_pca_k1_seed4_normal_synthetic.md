# Run ablation_alpha_0p75_mvtec_metal_nut_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_metal_nut_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9597527266424134`
- `auroc`: `0.832355816226784`
- `brier`: `0.17229188019345595`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1945360344389211`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002625711116453876`
- `max_f1`: `0.8975609756097561`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5322256933734537`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_metal_nut_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
