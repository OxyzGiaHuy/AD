# Run ablation_alpha_0p5_mvtec_transistor_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_transistor_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.810044465465152`
- `auroc`: `0.8220833333333334`
- `brier`: `0.28234831872847993`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2126842254400253`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002971217725425959`
- `max_f1`: `0.7341772151898734`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.7589911108766019`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_transistor_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
