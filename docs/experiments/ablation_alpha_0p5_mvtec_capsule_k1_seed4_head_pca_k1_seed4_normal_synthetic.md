# Run ablation_alpha_0p5_mvtec_capsule_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_capsule_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9577740382814566`
- `auroc`: `0.8169126445951336`
- `brier`: `0.18473638557177804`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.23600113075790982`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0026225169386827583`
- `max_f1`: `0.9045643153526971`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5601171503057225`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_capsule_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
