# Run ablation_pca16_mvtec_pill_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_pill_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9644793009668455`
- `auroc`: `0.845608292416803`
- `brier`: `0.12762120678132935`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.09647826038434833`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0018859582055293157`
- `max_f1`: `0.9494949494949495`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.42579614466046234`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_pill_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
