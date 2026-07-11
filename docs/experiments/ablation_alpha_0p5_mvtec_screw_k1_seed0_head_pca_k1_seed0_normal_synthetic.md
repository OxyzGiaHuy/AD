# Run ablation_alpha_0p5_mvtec_screw_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_screw_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8099751246080438`
- `auroc`: `0.625128100020496`
- `brier`: `0.20866309607745803`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.18462531827390188`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0041149139637127515`
- `max_f1`: `0.8708487084870848`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6093198672014151`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_screw_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
