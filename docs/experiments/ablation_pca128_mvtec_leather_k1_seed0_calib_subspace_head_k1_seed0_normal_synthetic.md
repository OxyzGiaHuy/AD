# Run ablation_pca128_mvtec_leather_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_leather_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9986561141073974`
- `auroc`: `0.9962635869565217`
- `brier`: `0.24710650537181617`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.25230427326694616`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0019055657509353854`
- `max_f1`: `0.989247311827957`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.7164798430872745`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_leather_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
