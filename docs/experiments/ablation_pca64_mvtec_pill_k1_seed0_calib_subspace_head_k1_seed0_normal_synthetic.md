# Run ablation_pca64_mvtec_pill_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_pill_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9820660333432175`
- `auroc`: `0.9129841789416258`
- `brier`: `0.15534258511358234`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.15551141529026147`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0022434170530763217`
- `max_f1`: `0.9488054607508533`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.6465230330397338`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_pill_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
