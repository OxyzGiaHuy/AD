# Run ablation_pca16_mvtec_pill_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_pill_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9670895109624729`
- `auroc`: `0.8423349699945445`
- `brier`: `0.13813367128751394`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.14453597839720952`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0015838571272031989`
- `max_f1`: `0.9391891891891891`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `1.097725380887541`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_pill_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
