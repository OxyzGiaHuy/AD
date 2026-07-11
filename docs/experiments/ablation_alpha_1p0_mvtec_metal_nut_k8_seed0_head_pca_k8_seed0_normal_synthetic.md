# Run ablation_alpha_1p0_mvtec_metal_nut_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_metal_nut_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9935115663263079`
- `auroc`: `0.9726295210166178`
- `brier`: `0.14693086796374924`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2777818291083627`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.001988237399769866`
- `max_f1`: `0.967741935483871`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.47153695945881186`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_metal_nut_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
