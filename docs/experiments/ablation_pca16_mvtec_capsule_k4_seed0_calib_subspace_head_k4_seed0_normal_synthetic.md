# Run ablation_pca16_mvtec_capsule_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_capsule_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8940055043095665`
- `auroc`: `0.679297965696051`
- `brier`: `0.12641229707905816`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1247524605273749`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0013083238436868696`
- `max_f1`: `0.9145299145299145`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.4821707558386087`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_capsule_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
