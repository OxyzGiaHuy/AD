# Run ablation_alpha_0p75_mvtec_zipper_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_zipper_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9840582376966277`
- `auroc`: `0.9424894957983193`
- `brier`: `0.16125902339880976`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1691165503287157`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0036324709160438437`
- `max_f1`: `0.9392712550607287`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5055092538366152`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_zipper_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
