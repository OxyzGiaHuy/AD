# Run ablation_alpha_0p0_mvtec_zipper_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_zipper_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9840572265198935`
- `auroc`: `0.9422268907563025`
- `brier`: `0.24636486634677354`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3633093153009351`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0030563434228202367`
- `max_f1`: `0.9444444444444444`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6858652281834512`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_zipper_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
