# Run ablation_alpha_0p5_mvtec_toothbrush_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_toothbrush_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9632832191465355`
- `auroc`: `0.9083333333333333`
- `brier`: `0.20356480714098177`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.11102412286258875`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0018781577458693867`
- `max_f1`: `0.9206349206349206`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5979722012636648`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_toothbrush_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
