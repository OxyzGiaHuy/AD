# Run ablation_alpha_0p5_mvtec_cable_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_cable_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8888773365544855`
- `auroc`: `0.8090329835082459`
- `brier`: `0.2345227200753438`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.0019417750835418746`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0021624613429109254`
- `max_f1`: `0.7946428571428571`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.66166780669186`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_cable_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
