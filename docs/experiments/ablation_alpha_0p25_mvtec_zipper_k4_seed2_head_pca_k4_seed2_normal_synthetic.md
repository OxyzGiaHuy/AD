# Run ablation_alpha_0p25_mvtec_zipper_k4_seed2_head_pca_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_zipper_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9794412437730113`
- `auroc`: `0.9264705882352942`
- `brier`: `0.19900319277880874`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.33340716401472786`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0038027747824097313`
- `max_f1`: `0.9407114624505929`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5901352617374439`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_zipper_k4_seed2_head_pca_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
