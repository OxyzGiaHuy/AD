# Run ablation_alpha_0p75_mvtec_transistor_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_transistor_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9126103066894679`
- `auroc`: `0.92875`
- `brier`: `0.2901481280129301`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.25779266357421876`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.004121559262275695`
- `max_f1`: `0.8`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.7756301229246709`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_transistor_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
