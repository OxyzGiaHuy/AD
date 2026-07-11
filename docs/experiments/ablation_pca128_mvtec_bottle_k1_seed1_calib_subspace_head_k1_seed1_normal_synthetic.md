# Run ablation_pca128_mvtec_bottle_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_bottle_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.978789585045843`
- `auroc`: `0.9365079365079365`
- `brier`: `0.24069430701179576`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2408209435911064`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0018695716084126967`
- `max_f1`: `0.9312977099236641`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `2.1429752874665575`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_bottle_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
