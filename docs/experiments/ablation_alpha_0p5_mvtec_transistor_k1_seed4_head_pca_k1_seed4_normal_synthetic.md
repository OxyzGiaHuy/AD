# Run ablation_alpha_0p5_mvtec_transistor_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_transistor_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8083024777875032`
- `auroc`: `0.8608333333333333`
- `brier`: `0.28206897436649425`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.21357985854148867`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0026910225860774517`
- `max_f1`: `0.7777777777777778`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.7584012768090709`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_transistor_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
