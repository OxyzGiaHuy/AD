# Run ablation_pca128_mvtec_cable_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_cable_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9520644265398179`
- `auroc`: `0.9109820089955023`
- `brier`: `0.193795749315951`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.19527368014057475`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002101967434088389`
- `max_f1`: `0.8715083798882681`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.8056041011986572`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_cable_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
