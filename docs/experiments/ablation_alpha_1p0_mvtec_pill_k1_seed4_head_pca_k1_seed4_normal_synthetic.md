# Run ablation_alpha_1p0_mvtec_pill_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_pill_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.89836595964343`
- `auroc`: `0.5834697217675942`
- `brier`: `0.14742159002554098`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1263005615708357`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001988901193448883`
- `max_f1`: `0.9155844155844156`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.47681240902073513`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_pill_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
