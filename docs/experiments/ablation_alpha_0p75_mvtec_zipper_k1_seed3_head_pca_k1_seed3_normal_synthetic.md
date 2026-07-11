# Run ablation_alpha_0p75_mvtec_zipper_k1_seed3_head_pca_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_zipper_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9863848790766405`
- `auroc`: `0.9548319327731093`
- `brier`: `0.1716178211451622`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2838888736750116`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0023778387844957264`
- `max_f1`: `0.967479674796748`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5296694540564937`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_zipper_k1_seed3_head_pca_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
