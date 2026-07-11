# Run ablation_pca64_mvtec_toothbrush_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_toothbrush_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9835788218296043`
- `auroc`: `0.9583333333333334`
- `brier`: `0.2856286873640022`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2856714526812235`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0037921788614420663`
- `max_f1`: `0.9375`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `4.111218552062472`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_toothbrush_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
