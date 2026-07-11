# Run ablation_pca64_mvtec_capsule_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_capsule_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9744163030801744`
- `auroc`: `0.9006781013163143`
- `brier`: `0.11319924030186473`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.11743573953880881`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0016093720597299662`
- `max_f1`: `0.9411764705882353`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.5493496387538052`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_capsule_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
