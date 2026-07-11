# Run ablation_pca128_mvtec_wood_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_wood_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9868446702132384`
- `auroc`: `0.9614035087719298`
- `brier`: `0.18686981785443743`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.20895971829378152`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002792351749501651`
- `max_f1`: `0.9508196721311475`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.138059332604431`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_wood_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
