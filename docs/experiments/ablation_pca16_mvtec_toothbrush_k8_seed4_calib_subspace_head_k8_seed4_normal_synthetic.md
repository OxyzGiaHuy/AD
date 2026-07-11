# Run ablation_pca16_mvtec_toothbrush_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_toothbrush_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9812067965559346`
- `auroc`: `0.9527777777777777`
- `brier`: `0.08254317241210872`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.11480743899231861`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.004001569756794544`
- `max_f1`: `0.9354838709677419`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.2727355528427949`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_toothbrush_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
