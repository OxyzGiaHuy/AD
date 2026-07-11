# Run ablation_alpha_1p0_mvtec_capsule_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_capsule_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9537482054422775`
- `auroc`: `0.8583964898284803`
- `brier`: `0.13607924028947654`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.17581974963347116`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.003519044935025952`
- `max_f1`: `0.935064935064935`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.446303086023943`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_capsule_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
