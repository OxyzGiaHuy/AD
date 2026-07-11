# Run ablation_alpha_0p5_mvtec_zipper_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_zipper_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.988219316326262`
- `auroc`: `0.9590336134453782`
- `brier`: `0.1739583249180885`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2485656876437712`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0035894133693335074`
- `max_f1`: `0.9586776859504132`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.536473147302836`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_zipper_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
