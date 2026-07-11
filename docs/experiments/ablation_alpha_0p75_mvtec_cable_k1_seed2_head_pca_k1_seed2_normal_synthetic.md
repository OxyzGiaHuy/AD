# Run ablation_alpha_0p75_mvtec_cable_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_cable_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9236920672940272`
- `auroc`: `0.8616941529235382`
- `brier`: `0.23855986899594636`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.17515278140703838`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0016878789414962133`
- `max_f1`: `0.8290155440414507`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6702331471430405`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_cable_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
