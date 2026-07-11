# Run ablation_alpha_0p5_mvtec_carpet_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_carpet_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9969616854257428`
- `auroc`: `0.9903691813804173`
- `brier`: `0.1573555020108137`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3289759108143995`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002145254873057716`
- `max_f1`: `0.9726775956284153`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5025057293871564`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_carpet_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
