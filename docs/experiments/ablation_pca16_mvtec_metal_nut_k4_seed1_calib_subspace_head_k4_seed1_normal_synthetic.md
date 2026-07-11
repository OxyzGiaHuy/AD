# Run ablation_pca16_mvtec_metal_nut_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_metal_nut_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9343647843495948`
- `auroc`: `0.8000977517106549`
- `brier`: `0.1627140565691036`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.14963909335758369`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002304636687040329`
- `max_f1`: `0.9319371727748691`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.5577120382406145`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_metal_nut_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
