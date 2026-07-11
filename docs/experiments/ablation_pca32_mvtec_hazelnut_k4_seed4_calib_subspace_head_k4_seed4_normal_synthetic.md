# Run ablation_pca32_mvtec_hazelnut_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_hazelnut_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9676030765381001`
- `auroc`: `0.9514285714285714`
- `brier`: `0.33567596769910313`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.34450891072099854`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.00226718011227521`
- `max_f1`: `0.9230769230769231`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `1.267216360622667`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_hazelnut_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
