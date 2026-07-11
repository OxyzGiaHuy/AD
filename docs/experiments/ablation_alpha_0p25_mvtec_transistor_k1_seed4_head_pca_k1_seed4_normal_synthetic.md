# Run ablation_alpha_0p25_mvtec_transistor_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_transistor_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.7824133236168922`
- `auroc`: `0.8295833333333333`
- `brier`: `0.25725625586587575`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.14863434135913844`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002561716679483652`
- `max_f1`: `0.735632183908046`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.7076491637758631`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_transistor_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
