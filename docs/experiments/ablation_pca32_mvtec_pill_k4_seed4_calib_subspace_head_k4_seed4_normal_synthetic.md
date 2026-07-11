# Run ablation_pca32_mvtec_pill_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_pill_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9798578454654365`
- `auroc`: `0.9015275504637207`
- `brier`: `0.09251598474919911`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.09886217761227468`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002657487642711508`
- `max_f1`: `0.9448275862068966`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.4498568104564771`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_pill_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
