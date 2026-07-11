# Run ablation_alpha_0p75_mvtec_tile_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_tile_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9887318146742912`
- `auroc`: `0.9696969696969697`
- `brier`: `0.1991813727188211`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1551498592409314`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0028362079467783626`
- `max_f1`: `0.9585798816568047`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5886457360173266`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_tile_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
