# Run ablation_pca128_mvtec_pill_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_pill_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9872922855720299`
- `auroc`: `0.9421713038734315`
- `brier`: `0.08583033326295428`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.09433975565933189`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002411321117849407`
- `max_f1`: `0.9611307420494699`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.3390257333802222`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_pill_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
