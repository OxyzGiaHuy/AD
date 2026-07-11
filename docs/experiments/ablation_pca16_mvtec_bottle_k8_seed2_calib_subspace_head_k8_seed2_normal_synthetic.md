# Run ablation_pca16_mvtec_bottle_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_bottle_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9541764958685663`
- `auroc`: `0.9095238095238095`
- `brier`: `0.11296593502068246`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1302323940109058`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.004970863169754844`
- `max_f1`: `0.9457364341085271`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.3736342947887488`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_bottle_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
