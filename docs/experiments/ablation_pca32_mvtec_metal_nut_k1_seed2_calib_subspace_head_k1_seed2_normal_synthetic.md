# Run ablation_pca32_mvtec_metal_nut_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_metal_nut_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9799957328422803`
- `auroc`: `0.9217986314760508`
- `brier`: `0.1727687126715266`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1780267416135125`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0017010191698437153`
- `max_f1`: `0.9533678756476683`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `2.0213136991195877`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_metal_nut_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
