# Run ablation_pca32_mvtec_toothbrush_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_toothbrush_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9825206175388731`
- `auroc`: `0.9555555555555556`
- `brier`: `0.28569189657210714`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2857030885560172`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0027292536216832345`
- `max_f1`: `0.9375`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `4.719504176232209`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_toothbrush_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
