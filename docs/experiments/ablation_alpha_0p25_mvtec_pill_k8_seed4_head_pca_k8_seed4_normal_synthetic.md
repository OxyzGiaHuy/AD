# Run ablation_alpha_0p25_mvtec_pill_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_pill_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9835108132333423`
- `auroc`: `0.925531914893617`
- `brier`: `0.20402798323367996`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.35236933006497917`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.003703932383817113`
- `max_f1`: `0.9530685920577617`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6006205980720785`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_pill_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
