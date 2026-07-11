# Run ablation_alpha_0p5_mvtec_zipper_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_zipper_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9848638504375234`
- `auroc`: `0.9461659663865546`
- `brier`: `0.17239740143356053`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.29493680201618877`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0024427532014862593`
- `max_f1`: `0.9554655870445344`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5332237655148964`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_zipper_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
