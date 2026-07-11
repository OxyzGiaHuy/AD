# Run ablation_alpha_1p0_mvtec_capsule_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_capsule_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9369530969664264`
- `auroc`: `0.749900279218189`
- `brier`: `0.139521099188777`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.09392377734184262`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002552918666465716`
- `max_f1`: `0.9113924050632911`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.4530190536714146`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_capsule_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
