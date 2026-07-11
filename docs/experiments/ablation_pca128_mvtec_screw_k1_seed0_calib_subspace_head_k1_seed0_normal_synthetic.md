# Run ablation_pca128_mvtec_screw_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_screw_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7489822005535152`
- `auroc`: `0.5620004099200656`
- `brier`: `0.2558365958979295`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.25601166263222697`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0018101614201441406`
- `max_f1`: `0.8838951310861424`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `2.8256839838194314`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_screw_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
