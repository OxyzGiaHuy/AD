# Run ablation_pca32_mvtec_capsule_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_capsule_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9457198321649424`
- `auroc`: `0.7945751894694855`
- `brier`: `0.13901968796531686`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12779011399569834`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001549498728391799`
- `max_f1`: `0.9184549356223176`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.5824678815468378`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_capsule_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
