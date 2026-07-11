# Run ablation_alpha_0p5_mvtec_bottle_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_bottle_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9688975383718842`
- `auroc`: `0.9103174603174603`
- `brier`: `0.20011594261829901`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.14323883243353974`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002130359186824546`
- `max_f1`: `0.9264705882352942`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.591536249343552`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_bottle_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
