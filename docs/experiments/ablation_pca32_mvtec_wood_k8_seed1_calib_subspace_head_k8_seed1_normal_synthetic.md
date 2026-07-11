# Run ablation_pca32_mvtec_wood_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_wood_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9903213428580242`
- `auroc`: `0.9701754385964912`
- `brier`: `0.11719623013655449`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12890483639969297`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0014793480263103412`
- `max_f1`: `0.9586776859504132`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.6848434004718464`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_wood_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
