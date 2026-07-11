# Run ablation_alpha_0p5_mvtec_wood_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_wood_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9967909697980775`
- `auroc`: `0.9894736842105263`
- `brier`: `0.19989409911051276`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.32800023012523405`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.004891324906220919`
- `max_f1`: `0.9672131147540983`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5913564737033168`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_wood_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
