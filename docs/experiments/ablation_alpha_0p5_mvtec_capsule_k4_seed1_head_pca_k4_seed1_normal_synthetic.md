# Run ablation_alpha_0p5_mvtec_capsule_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_capsule_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9822088684930038`
- `auroc`: `0.9150378938970881`
- `brier`: `0.1682706388189854`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.24182716147466138`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0020685553635385904`
- `max_f1`: `0.9356223175965666`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5250718991670752`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_capsule_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
