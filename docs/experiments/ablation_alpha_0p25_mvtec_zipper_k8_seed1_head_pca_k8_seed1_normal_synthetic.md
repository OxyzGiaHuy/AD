# Run ablation_alpha_0p25_mvtec_zipper_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_zipper_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.985049400604284`
- `auroc`: `0.9461659663865546`
- `brier`: `0.2000181262367226`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3343689317340093`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0029092980610416425`
- `max_f1`: `0.9421487603305785`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.592324293855152`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_zipper_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
