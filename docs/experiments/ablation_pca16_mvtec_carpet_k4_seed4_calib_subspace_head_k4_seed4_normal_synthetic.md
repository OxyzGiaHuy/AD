# Run ablation_pca16_mvtec_carpet_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_carpet_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9996268092468068`
- `auroc`: `0.9987961476725522`
- `brier`: `0.019613479043286277`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.04611328742904668`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0035016647834553677`
- `max_f1`: `0.9888888888888889`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.07610632295578149`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_carpet_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
