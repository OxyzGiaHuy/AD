# Run ablation_alpha_0p25_mvtec_zipper_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_zipper_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.976356601208641`
- `auroc`: `0.9204306722689075`
- `brier`: `0.20906976387773082`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.31127818353128744`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0024122000850786435`
- `max_f1`: `0.9477911646586346`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6107393403901884`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_zipper_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
