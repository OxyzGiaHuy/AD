# Run ablation_alpha_0p25_mvtec_hazelnut_k4_seed2_head_pca_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_hazelnut_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9906595507960213`
- `auroc`: `0.9821428571428571`
- `brier`: `0.22557569304863362`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.08285261609337555`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.00234245898371393`
- `max_f1`: `0.9583333333333334`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6438192337385025`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_hazelnut_k4_seed2_head_pca_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
