# Run ablation_alpha_1p0_mvtec_screw_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_screw_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8305967466164695`
- `auroc`: `0.6489034638245542`
- `brier`: `0.18776789128504195`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.06712576001882553`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.00171391642652452`
- `max_f1`: `0.8561151079136691`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5622343760206799`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_screw_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
