# Run ablation_pca64_mvtec_wood_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_wood_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9860991705479036`
- `auroc`: `0.9605263157894737`
- `brier`: `0.24024345948525358`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.24037453720841218`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0025466902629484103`
- `max_f1`: `0.957983193277311`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `2.7431108014937022`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_wood_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
