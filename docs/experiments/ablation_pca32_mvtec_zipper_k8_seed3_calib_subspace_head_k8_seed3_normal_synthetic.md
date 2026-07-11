# Run ablation_pca32_mvtec_zipper_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_zipper_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9862408856928837`
- `auroc`: `0.9498424369747899`
- `brier`: `0.08014884643370085`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.08178542137909436`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0038330978683091157`
- `max_f1`: `0.9512195121951219`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.43526256021313325`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_zipper_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
