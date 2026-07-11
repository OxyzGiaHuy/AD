# Run ablation_pca64_mvtec_screw_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_screw_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9049698330711072`
- `auroc`: `0.7895060463209674`
- `brier`: `0.16632759549748427`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1631820051115938`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0018431369331665336`
- `max_f1`: `0.8796680497925311`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.622013570684124`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_screw_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
