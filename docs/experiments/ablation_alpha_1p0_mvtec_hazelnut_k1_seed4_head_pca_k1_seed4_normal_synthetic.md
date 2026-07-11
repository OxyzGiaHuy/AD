# Run ablation_alpha_1p0_mvtec_hazelnut_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_hazelnut_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8885407448337276`
- `auroc`: `0.7819642857142857`
- `brier`: `0.23903019964980904`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.08749111565676604`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0028180203315886585`
- `max_f1`: `0.8157894736842105`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6735142229137449`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_hazelnut_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
