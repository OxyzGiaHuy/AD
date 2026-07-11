# Run ablation_pca32_mvtec_transistor_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_transistor_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7283545704101841`
- `auroc`: `0.7741666666666667`
- `brier`: `0.549140589523947`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.5669488018751144`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001898384727537632`
- `max_f1`: `0.673469387755102`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `3.4482264531983566`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_transistor_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
