# Run ablation_alpha_0p25_mvtec_pill_k8_seed2_head_pca_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_pill_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9871922586694737`
- `auroc`: `0.94189852700491`
- `brier`: `0.19763467195044554`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.33872405283465357`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002978990835968606`
- `max_f1`: `0.9619377162629758`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5875180612988308`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_pill_k8_seed2_head_pca_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
