# Run ablation_alpha_0p75_mvtec_zipper_k4_seed2_head_pca_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_zipper_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9794673719616142`
- `auroc`: `0.926733193277311`
- `brier`: `0.16474073815698762`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.21435484349332906`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0025394894799451954`
- `max_f1`: `0.9397590361445783`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5138023569454577`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_zipper_k4_seed2_head_pca_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
