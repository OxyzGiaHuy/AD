# Run ablation_pca16_mvtec_cable_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_cable_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8883250097093879`
- `auroc`: `0.8125937031484258`
- `brier`: `0.23511808013763277`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.228356369237105`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.003401444045205911`
- `max_f1`: `0.8144329896907216`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.727569716334705`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_cable_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
