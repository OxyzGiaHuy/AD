# Run ablation_alpha_0p5_mvtec_hazelnut_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_hazelnut_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9596721945404064`
- `auroc`: `0.9139285714285714`
- `brier`: `0.22843680320307924`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.032917796481739446`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.00279001517390663`
- `max_f1`: `0.8920863309352518`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6492287423377551`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_hazelnut_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
