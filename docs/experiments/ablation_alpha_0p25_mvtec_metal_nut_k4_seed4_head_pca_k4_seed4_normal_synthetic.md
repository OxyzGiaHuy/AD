# Run ablation_alpha_0p25_mvtec_metal_nut_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_metal_nut_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9779553624001974`
- `auroc`: `0.9213098729227761`
- `brier`: `0.20387829643577618`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3142266486002051`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0017952338184999382`
- `max_f1`: `0.9441624365482234`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6001599602362271`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_metal_nut_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
