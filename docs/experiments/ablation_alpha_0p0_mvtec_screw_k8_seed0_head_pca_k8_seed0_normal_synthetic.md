# Run ablation_alpha_0p0_mvtec_screw_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_screw_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9080342957271241`
- `auroc`: `0.8239393318302931`
- `brier`: `0.24891908223073456`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3209844781085849`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0022489417111501097`
- `max_f1`: `0.9007633587786259`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6909762442516211`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_screw_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
