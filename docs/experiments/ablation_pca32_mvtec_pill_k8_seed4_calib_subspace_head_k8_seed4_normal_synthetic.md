# Run ablation_pca32_mvtec_pill_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_pill_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9854941098701896`
- `auroc`: `0.9293507910529187`
- `brier`: `0.07213347875643318`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.05589140945359576`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0020118436056696725`
- `max_f1`: `0.9477351916376306`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.2451839007776472`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_pill_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
