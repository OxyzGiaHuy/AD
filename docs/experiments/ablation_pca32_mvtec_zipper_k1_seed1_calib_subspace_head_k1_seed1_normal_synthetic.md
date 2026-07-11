# Run ablation_pca32_mvtec_zipper_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_zipper_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9855338775642308`
- `auroc`: `0.9503676470588235`
- `brier`: `0.18024992570006762`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.18991899441014853`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0015223102138334553`
- `max_f1`: `0.9516129032258065`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `1.3674170047496115`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_zipper_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
