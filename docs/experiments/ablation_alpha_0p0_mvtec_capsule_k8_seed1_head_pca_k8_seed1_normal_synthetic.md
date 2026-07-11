# Run ablation_alpha_0p0_mvtec_capsule_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_capsule_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9837893389543083`
- `auroc`: `0.9242122058236937`
- `brier`: `0.2467254639624847`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.39986087043177`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0020084315205387998`
- `max_f1`: `0.9427312775330396`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6865793998941219`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_capsule_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
