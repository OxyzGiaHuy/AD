# Run ablation_pca32_mvtec_screw_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_screw_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8630706676765455`
- `auroc`: `0.6767780282844845`
- `brier`: `0.22843514125751807`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2168798500671983`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002089278562925756`
- `max_f1`: `0.8582089552238806`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.9252972776895246`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_screw_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
