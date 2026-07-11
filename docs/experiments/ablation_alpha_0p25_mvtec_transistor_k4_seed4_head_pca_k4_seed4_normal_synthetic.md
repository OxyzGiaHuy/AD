# Run ablation_alpha_0p25_mvtec_transistor_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_transistor_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.928777209869774`
- `auroc`: `0.9383333333333334`
- `brier`: `0.25033028199193147`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.14604986399412162`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0028827894292771817`
- `max_f1`: `0.8470588235294118`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6936854701912004`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_transistor_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
