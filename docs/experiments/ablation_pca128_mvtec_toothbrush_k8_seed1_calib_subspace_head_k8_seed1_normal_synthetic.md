# Run ablation_pca128_mvtec_toothbrush_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_toothbrush_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9888641038543707`
- `auroc`: `0.9722222222222222`
- `brier`: `0.11673941302102235`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.14982531264069537`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.005021759619315465`
- `max_f1`: `0.967741935483871`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.7725712118203246`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_toothbrush_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
