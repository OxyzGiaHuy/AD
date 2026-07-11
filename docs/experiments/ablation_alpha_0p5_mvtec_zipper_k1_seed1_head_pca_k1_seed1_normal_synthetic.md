# Run ablation_alpha_0p5_mvtec_zipper_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_zipper_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9917104261287453`
- `auroc`: `0.970063025210084`
- `brier`: `0.1872920706559312`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.24482685327529913`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002297997425328817`
- `max_f1`: `0.9626556016597511`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5649862348086647`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_zipper_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
