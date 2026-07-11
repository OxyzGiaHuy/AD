# Run ablation_pca16_mvtec_hazelnut_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_hazelnut_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9153828954069902`
- `auroc`: `0.8539285714285715`
- `brier`: `0.29535516873054063`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.289136604829268`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0013794428245587783`
- `max_f1`: `0.8427672955974843`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.8867079517549413`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_hazelnut_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
