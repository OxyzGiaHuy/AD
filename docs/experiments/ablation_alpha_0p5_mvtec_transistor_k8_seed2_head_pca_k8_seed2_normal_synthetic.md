# Run ablation_alpha_0p5_mvtec_transistor_k8_seed2_head_pca_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_transistor_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.864572039623581`
- `auroc`: `0.8979166666666667`
- `brier`: `0.26749418379534423`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.20787721216678617`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0025508226454257965`
- `max_f1`: `0.8045977011494253`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.7281577130608724`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_transistor_k8_seed2_head_pca_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
