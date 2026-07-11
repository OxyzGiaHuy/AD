# Run ablation_pca32_mvtec_zipper_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_zipper_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9838457080709117`
- `auroc`: `0.9419642857142857`
- `brier`: `0.10500289679364051`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12055008732177938`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.003404420782003971`
- `max_f1`: `0.9516129032258065`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.6505717300046959`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_zipper_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
