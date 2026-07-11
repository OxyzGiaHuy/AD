# Run ablation_alpha_0p5_mvtec_cable_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_cable_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9524475107525346`
- `auroc`: `0.907608695652174`
- `brier`: `0.22356479034116628`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12439868052800496`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002395211358865102`
- `max_f1`: `0.8977272727272727`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6383970071879945`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_cable_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
