# Run ablation_pca128_mvtec_zipper_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_zipper_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9952271064177891`
- `auroc`: `0.9831932773109243`
- `brier`: `0.047524723123387194`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.06807193472142642`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002190363858610589`
- `max_f1`: `0.9790794979079498`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.18250547103431494`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_zipper_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
