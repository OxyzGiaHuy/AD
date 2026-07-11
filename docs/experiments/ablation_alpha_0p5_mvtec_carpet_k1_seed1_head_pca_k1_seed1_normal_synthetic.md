# Run ablation_alpha_0p5_mvtec_carpet_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_carpet_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9858320368848147`
- `auroc`: `0.949438202247191`
- `brier`: `0.18503936623138673`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.32330510504225385`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002526372320886351`
- `max_f1`: `0.935672514619883`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5606072224497882`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_carpet_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
