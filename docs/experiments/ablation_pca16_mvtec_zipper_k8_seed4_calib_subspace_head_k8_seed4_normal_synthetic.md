# Run ablation_pca16_mvtec_zipper_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_zipper_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9813532967957981`
- `auroc`: `0.9327731092436975`
- `brier`: `0.10727437379473814`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.10972783686999862`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0016019794448519384`
- `max_f1`: `0.9392712550607287`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.34487409125600604`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_zipper_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
