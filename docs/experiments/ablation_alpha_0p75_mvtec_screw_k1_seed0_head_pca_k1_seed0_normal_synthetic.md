# Run ablation_alpha_0p75_mvtec_screw_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_screw_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8092938150948742`
- `auroc`: `0.6286124205779873`
- `brier`: `0.195049501244549`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.06998161301016814`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.003824328235350549`
- `max_f1`: `0.8666666666666667`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5797365972961888`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_screw_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
