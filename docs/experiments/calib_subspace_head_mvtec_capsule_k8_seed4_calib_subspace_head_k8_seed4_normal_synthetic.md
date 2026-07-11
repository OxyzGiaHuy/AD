# Run calib_subspace_head_mvtec_capsule_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/calib_subspace_head_mvtec_capsule_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9662191927438469`
- `auroc`: `0.8747506980454727`
- `brier`: `0.11833299638122938`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.13462657441744924`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0012773665825300145`
- `max_f1`: `0.9422222222222222`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.5929285004009034`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/calib_subspace_head_mvtec_capsule_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
