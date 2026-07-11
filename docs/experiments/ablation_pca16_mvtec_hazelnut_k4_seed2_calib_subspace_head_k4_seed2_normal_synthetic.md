# Run ablation_pca16_mvtec_hazelnut_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_hazelnut_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9271593699075262`
- `auroc`: `0.8757142857142857`
- `brier`: `0.32025014201406`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3026509165763855`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002897294678471305`
- `max_f1`: `0.847682119205298`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `1.041877941305553`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_hazelnut_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
