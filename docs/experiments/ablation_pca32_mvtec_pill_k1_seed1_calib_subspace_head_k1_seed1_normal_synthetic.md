# Run ablation_pca32_mvtec_pill_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_pill_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9812820943774783`
- `auroc`: `0.914620840152755`
- `brier`: `0.15335625603287342`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1544116888931411`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0013107631444752572`
- `max_f1`: `0.9507042253521126`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `1.597939377989003`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_pill_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
