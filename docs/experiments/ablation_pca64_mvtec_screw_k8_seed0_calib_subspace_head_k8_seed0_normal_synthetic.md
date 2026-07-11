# Run ablation_pca64_mvtec_screw_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_screw_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9080342957271241`
- `auroc`: `0.8239393318302931`
- `brier`: `0.14490467338579543`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.09942454919219017`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002908618829678744`
- `max_f1`: `0.9007633587786259`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.4777732136035544`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_screw_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
