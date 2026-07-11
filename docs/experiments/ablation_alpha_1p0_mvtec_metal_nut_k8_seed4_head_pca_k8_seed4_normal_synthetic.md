# Run ablation_alpha_1p0_mvtec_metal_nut_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_metal_nut_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.993317267001072`
- `auroc`: `0.9726295210166178`
- `brier`: `0.1455292180296626`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.13268736808196357`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.003409324359634648`
- `max_f1`: `0.972972972972973`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.46662451458626175`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_metal_nut_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
